#!/usr/bin/env bash

# This script provides a unified local build process that mirrors our CI pipeline.
# It ensures that code quality checks, tests, and build artifacts are all generated
# and validated locally before pushing to the remote repository.

# ---
# SCRIPT CONFIGURATION
# ---
set -e  # Exit immediately if a command exits with a non-zero status.
set -o pipefail # Return exit status of the last command in the pipe that failed.
set -u # Treat unset variables as an error.

# ---
# HELPER FUNCTIONS
# ---
info() {
    echo "✅ [INFO] $1"
}

error() {
    echo "❌ [ERROR] $1" >&2
    exit 1
}

# ---
# MAIN BUILD LOGIC
# ---
main() {
    info "Starting local build process..."

    # Step 1: Check Dependency Health
    info "Checking for dependency conflicts..."
    pip check || error "Dependency check failed. Please resolve conflicts before proceeding."
    info "Dependencies are healthy."

    # Step 2: Run Tests
    info "Running test suite with pytest..."
    # We use 'set +e' to temporarily allow pytest to exit with a non-zero status
    # without terminating the script. Pytest exits with status 5 if no tests are
    # found, which is a success case for a new project.
    set +e
    pytest
    PYTEST_EXIT_CODE=$?
    set -e

    if [ $PYTEST_EXIT_CODE -eq 0 ]; then
        info "All tests passed."
    elif [ $PYTEST_EXIT_CODE -eq 5 ]; then
        info "No tests found, which is acceptable. Continuing build."
    else
        error "Tests failed with exit code $PYTEST_EXIT_CODE. Please fix them before building."
    fi

    # Step 3: Build Documentation Website
    info "Building documentation website with MkDocs..."
    mkdocs build || error "MkDocs build failed."
    info "Documentation website built successfully in 'site/' directory."

    # Step 4: Build Python Package (Wheel and sdist)
    info "Building Python package..."
    # Ensure build tool is installed
    pip install -q build
    python -m build || error "Python package build failed."
    info "Python package built successfully in 'dist/' directory."

    # Optional Step 5: Build Docker Image (if Docker is available)
    if ! command -v docker &> /dev/null
    then
        info "Docker not found, skipping Docker image build."
    else
        info "Building Docker image..."
        docker build -t codecraftai:latest . || error "Docker image build failed."
        info "Docker image 'codecraftai:latest' built successfully."
    fi

    echo ""
    info "🎉 Local build process completed successfully! 🎉"
    info "Artifacts generated:"
    info "  - Documentation: ./site/"
    info "  - Python Package: ./dist/"
    if command -v docker &> /dev/null; then
        info "  - Docker Image: codecraftai:latest"
    fi
}

# ---
# SCRIPT EXECUTION
# ---
main "$@"
