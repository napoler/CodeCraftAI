import subprocess
import sys
import time
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# ---
# Configuration
# ---
PROJECT_ROOT = Path(__file__).parent.parent.parent
SRC_PATH = PROJECT_ROOT / "src"
TESTS_PATH = PROJECT_ROOT / "tests"
LOG_FILE = PROJECT_ROOT / "guardian.log"

# Commands to run
LINT_COMMAND = ["ruff", "check", "--fix", "."]
FORMAT_COMMAND = ["black", "."]
TEST_COMMAND = ["pytest"]
TYPE_CHECK_COMMAND = ["mypy", "src"]


# ---
# Helper Functions
# ---
def log(message):
    """Logs a message to the console and a file."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}"
    print(log_message)
    with open(LOG_FILE, "a") as f:
        f.write(log_message + "\n")


def run_command(command, path):
    """Runs a command and logs its output."""
    log(f"Running '{' '.join(command)}' on '{path}'...")
    try:
        result = subprocess.run(
            command,
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        if result.stdout:
            log(f"Output:\n{result.stdout}")
        if result.stderr:
            log(f"Errors:\n{result.stderr}")
        log(f"✅ Success: '{' '.join(command)}' finished.")
        return True
    except subprocess.CalledProcessError as e:
        log(
            f"❌ Error running '{' '.join(command)}'. Exit code: {e.returncode}\n"
            f"Output:\n{e.stdout}\n"
            f"Errors:\n{e.stderr}"
        )
        return False


# ---
# Event Handler
# ---
class PythonFileEventHandler(FileSystemEventHandler):
    """Handles events for .py files."""

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(".py"):
            log(f"File modified: {event.src_path}")
            path = Path(event.src_path).relative_to(PROJECT_ROOT)

            # Run formatters and linters on the specific file
            run_command(["ruff", "check", "--fix", str(path)], path)
            run_command(["black", str(path)], path)

            # Run type checking and tests on the whole project
            run_command(TYPE_CHECK_COMMAND, PROJECT_ROOT)
            run_command(TEST_COMMAND, PROJECT_ROOT)
            log("-" * 20)


# ---
# Main Execution
# ---
if __name__ == "__main__":
    # Clear log file on start
    with open(LOG_FILE, "w") as f:
        f.write("Guardian Log\n" + "=" * 12 + "\n")

    log("Starting Guardian: Watching for Python file changes...")
    log(f"Watching directories: '{SRC_PATH}' and '{TESTS_PATH}'")

    observer = Observer()
    observer.schedule(PythonFileEventHandler(), str(SRC_PATH), recursive=True)
    observer.schedule(PythonFileEventHandler(), str(TESTS_PATH), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        log("Guardian stopped.")
    observer.join()
