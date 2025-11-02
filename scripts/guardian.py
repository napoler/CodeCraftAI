"""
Guardian: Your Real-Time Development Assistant

This script acts as a "guardian" for your project, continuously monitoring your
codebase for changes and automatically triggering a suite of quality checks,
tests, and build processes in real-time.

It provides a rapid feedback loop, allowing developers (both human and AI) to
catch and fix issues the moment they arise, directly within their development
environment.

Core Features:
1.  **Monitors Python Code**: Watches `src/` and `tests/` directories. On any
    change to a `.py` file, it automatically runs:
    - `ruff check` (Linting)
    - `black` (Formatting)
    - `pytest` (Unit Testing)
2.  **Monitors Documentation**: Watches `docs/` and `specs/` directories. On any
    change to a `.md` file, it automatically runs `mkdocs build` to ensure
    the documentation site is always up-to-date.
3.  **Monitors Dependencies**: Watches `pyproject.toml`. If a new dependency is
    added, it intelligently runs `scripts/generate_api_docs.py` for that specific
    new library, automating the creation of API reference material.

Usage:
    python scripts/guardian.py
"""

import subprocess
import time
import sys
from pathlib import Path

import toml
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- Configuration ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_PATHS = [PROJECT_ROOT / "src", PROJECT_ROOT / "tests"]
DOC_PATHS = [PROJECT_ROOT / "docs", PROJECT_ROOT / "specs"]
PYPROJECT_PATH = PROJECT_ROOT / "pyproject.toml"

# --- Helper Functions ---

def run_command(command, cwd=PROJECT_ROOT):
    """Executes a command and prints its output in a formatted block."""
    print(f"--- Running: `{' '.join(command)}` ---", flush=True)
    try:
        process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            cwd=cwd
        )
        print(process.stdout, end='', flush=True)

        # Special handling for pytest exit code 5 (no tests found)
        is_pytest = command[0] == "pytest"
        is_success = (process.returncode == 0) or (is_pytest and process.returncode == 5)

        if is_success:
            if is_pytest and process.returncode == 5:
                print("--- Success (No tests found): `pytest` ---", flush=True)
            else:
                print(f"--- Success: `{' '.join(command)}` ---\n", flush=True)
        else:
            print(f"--- Failed (Code {process.returncode}): `{' '.join(command)}` ---\n", flush=True)

    except FileNotFoundError:
        print(f"--- Error: Command not found: {command[0]} ---\n", flush=True)
    except Exception as e:
        print(f"--- An unexpected error occurred: {e} ---\n", flush=True)

def get_project_deps():
    """Parses pyproject.toml to get the list of dev dependencies."""
    try:
        data = toml.load(PYPROJECT_PATH)
        deps = data.get("project", {}).get("optional-dependencies", {}).get("dev", [])
        # Handle format like "mkdocstrings[python]" -> "mkdocstrings"
        return {dep.split('[')[0] for dep in deps}
    except Exception as e:
        print(f"⚠️  Could not parse {PYPROJECT_PATH}: {e}")
        return set()

# --- Event Handlers ---

class PyFileHandler(FileSystemEventHandler):
    """Handler for Python file changes."""
    def on_modified(self, event):
        if event.is_directory or not event.src_path.endswith(".py"):
            return
        print(f"🐍 Python file modified: {Path(event.src_path).relative_to(PROJECT_ROOT)}")
        run_command(["ruff", "check", "."])
        run_command(["black", "."])
        run_command(["pytest"])

class DocFileHandler(FileSystemEventHandler):
    """Handler for Markdown file changes."""
    def on_modified(self, event):
        if event.is_directory or not event.src_path.endswith(".md"):
            return
        print(f"📖 Doc file modified: {Path(event.src_path).relative_to(PROJECT_ROOT)}")
        run_command(["mkdocs", "build"])

class DependencyFileHandler(FileSystemEventHandler):
    """Handler for pyproject.toml changes."""
    def __init__(self):
        self.known_deps = get_project_deps()

    def on_modified(self, event):
        if event.is_directory or Path(event.src_path) != PYPROJECT_PATH:
            return

        print(f"📦 Dependencies file modified: {Path(event.src_path).relative_to(PROJECT_ROOT)}")
        new_deps = get_project_deps()

        added_deps = new_deps - self.known_deps
        if added_deps:
            print(f"✨ New dependencies detected: {', '.join(added_deps)}")
            for dep in added_deps:
                run_command([sys.executable, str(PROJECT_ROOT / "scripts/generate_api_docs.py"), dep])
            self.known_deps = new_deps
        else:
            print("📦 No new dependencies detected.")


# --- Main Execution ---

def main():
    """Starts the file system observer."""
    print("🛡️ Starting Guardian in Live Development Mode...")
    print("Watching for changes. Press Ctrl+C to stop.")

    observer = Observer()

    # Schedule Python file monitoring
    for path in SRC_PATHS:
        observer.schedule(PyFileHandler(), path, recursive=True)

    # Schedule Documentation file monitoring
    for path in DOC_PATHS:
        observer.schedule(DocFileHandler(), path, recursive=True)

    # Schedule Dependency file monitoring
    observer.schedule(DependencyFileHandler(), PYPROJECT_PATH.parent, recursive=False)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛡️ Guardian stopped. Goodbye!")
    observer.join()

if __name__ == "__main__":
    main()
