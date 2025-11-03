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

    # Step 2: Run Static Type Checking
    info "Running static type checking with Mypy..."
    mypy src/ || error "Static type checking failed. Please fix the type errors."
    info "No type errors found."

    # Step 3: Run Tests with Coverage
    info "Running test suite with coverage..."
    set +e
    pytest --cov=src
    PYTEST_EXIT_CODE=$?
    set -e

    if [ $PYTEST_EXIT_CODE -eq 0 ]; then
        info "All tests passed."
    elif [ $PYTEST_EXIT_CODE -eq 5 ]; then
        info "No tests found, which is acceptable. Continuing build."
    else
        error "Tests failed with exit code $PYTEST_EXIT_CODE. Please fix them before building."
    fi

    # Step 4: Build Documentation Website
    info "Preparing files for MkDocs build..."
    cp README.md .codecraft/docs/README.md
    cp CONTRIBUTING.md .codecraft/docs/CONTRIBUTING.md
    cp -r specs .codecraft/docs/specs
    cp -r .codecraft/adr .codecraft/docs/adr

    info "Building documentation website with MkDocs..."
    mkdocs build || error "MkDocs build failed."
    info "Documentation website built successfully in 'site/' directory."

    info "Cleaning up temporary files from MkDocs build..."
    rm .codecraft/docs/README.md
    rm .codecraft/docs/CONTRIBUTING.md
    rm -rf .codecraft/docs/specs
    rm -rf .codecraft/docs/adr

    # Step 5: Build Python Package
    info "Building Python package..."
    pip install -q build
    python -m build || error "Python package build failed."
    info "Python package built successfully in 'dist/' directory."

    # Step 6: Build Docker Image
    info "Building Docker image..."
    sudo docker build -t codecraftai:latest . || error "Docker image build failed."
    info "Docker image 'codecraftai:latest' built successfully."

    echo ""
    info "🎉 Local build process completed successfully! 🎉"
}

# ---
# SCRIPT EXECUTION
# ---
main "$@"
