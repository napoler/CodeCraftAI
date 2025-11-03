#!/usr/bin/env python
import datetime
import os
import shutil
import subprocess
from pathlib import Path

import click
import yaml

# ---
# Configuration and Constants
# ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
WORKFLOW_CONFIG_PATH = PROJECT_ROOT / ".codecraft" / "workflow.yml"
PROTECTED_PATHS_CONFIG_PATH = PROJECT_ROOT / ".codecraft" / "protected_paths.yml"
TRASH_DIR = PROJECT_ROOT / ".trash"


# ---
# Helper Functions
# ---
def load_yaml_config(config_path: Path, error_msg: str) -> dict:
    """Loads a YAML configuration file."""
    try:
        with open(config_path, "r") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        click.echo(click.style(f"Error: {error_msg} not found at {config_path}", fg="red"))
        raise click.Abort()
    except yaml.YAMLError as e:
        click.echo(click.style(f"Error: Could not parse {error_msg}: {e}", fg="red"))
        raise click.Abort()


CONFIG = load_yaml_config(WORKFLOW_CONFIG_PATH, "Workflow config")
PROTECTED_PATHS = load_yaml_config(PROTECTED_PATHS_CONFIG_PATH, "Protected paths config").get("protected", [])


def is_protected(path: Path) -> bool:
    """Checks if a given path is in the protected list."""
    try:
        relative_path_str = str(path.relative_to(PROJECT_ROOT))
        # Check against individual files and parent directories
        for protected_path in PROTECTED_PATHS:
            if relative_path_str.startswith(protected_path):
                return True
        return False
    except ValueError:
        return False


def find_task_file(task_title: str) -> Path | None:
    """Finds a task file across all status directories."""
    task_filename = f"{task_title}.md"
    for status_dir in CONFIG["tasks"]["status_map"].values():
        task_path = PROJECT_ROOT / status_dir / task_filename
        if task_path.exists():
            return task_path
    return None


def run_command(command: list[str], cwd: Path | None = PROJECT_ROOT, quiet: bool = False) -> str:
    """Runs a command and handles errors."""
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True, cwd=cwd)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        if not quiet:
            error_msg = e.stderr.strip() or e.stdout.strip()
            click.echo(click.style(f"Command failed: {error_msg}", fg="red"))
        raise click.Abort()


def run_git_command(command: list[str], quiet: bool = False):
    return run_command(["git"] + command, quiet=quiet)


# ---
# Click Command Groups
# ---
@click.group()
def cli():
    """CodeCraftAI CLI: A helper to manage the project workflow & AI tasks."""
    pass


@cli.group()
def task():
    """Commands for managing tasks."""
    pass


@cli.group()
def ai():
    """Smart commands for AI-assisted code optimization."""
    pass


@cli.command()
@click.argument("path", type=click.Path(exists=True, path_type=Path))
def delete(path: Path):
    """Safely deletes a file or directory by moving it to the .trash."""
    absolute_path = path.resolve()
    if is_protected(absolute_path):
        click.echo(click.style(f"Error: Path '{path}' is protected and cannot be deleted.", fg="red"))
        raise click.Abort()

    click.echo(f"Preparing to delete: {path}")
    q1 = "1. What is the purpose of this file/directory?"
    a1 = click.prompt(q1)
    q2 = "2. Why does it need to be deleted?"
    a2 = click.prompt(q2)
    q3 = "3. What are the potential negative consequences of deleting it?"
    a3 = click.prompt(q3)

    if not click.confirm(click.style("\nAre you sure you want to move this to the trash?", fg="yellow")):
        raise click.Abort()

    TRASH_DIR.mkdir(exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    trash_path = TRASH_DIR / f"{timestamp}_{path.name}"

    shutil.move(str(path), trash_path)

    log_file = PROJECT_ROOT / CONFIG['directories']['project_logs'] / "ai_interactions.md"
    with open(log_file, "a") as f:
        f.write("\n---\n")
        f.write(f"### File Deletion Log: {datetime.datetime.now().isoformat()}\n")
        f.write(f"- **File:** `{path}`\n")
        f.write(f"- **Action:** Moved to trash.\n")
        f.write(f"- **Q1 (Purpose):** {a1}\n")
        f.write(f"- **Q2 (Reason):** {a2}\n")
        f.write(f"- **Q3 (Consequences):** {a3}\n")

    click.echo(click.style(f"✅ Successfully moved '{path}' to the trash.", fg="green"))


@cli.group()
def trash():
    """Commands for managing the trash can."""
    pass


@trash.command(name="list")
def trash_list():
    """Lists all items in the trash can."""
    TRASH_DIR.mkdir(exist_ok=True)
    items = list(TRASH_DIR.iterdir())
    if not items:
        click.echo("The trash can is empty.")
        return
    click.echo("Items in trash:")
    for item in items:
        click.echo(f"- {item.name}")


@trash.command(name="restore")
@click.argument("item_name")
def trash_restore(item_name: str):
    """Restores an item from the trash can to its original location."""
    trash_path = TRASH_DIR / item_name
    if not trash_path.exists():
        click.echo(click.style(f"Error: '{item_name}' not found in trash.", fg="red"))
        raise click.Abort()

    original_name = "_".join(item_name.split("_")[1:])
    restore_path = PROJECT_ROOT / original_name

    if restore_path.exists():
        click.echo(click.style(f"Error: Path '{restore_path}' already exists.", fg="red"))
        raise click.Abort()

    shutil.move(str(trash_path), restore_path)
    click.echo(click.style(f"✅ Successfully restored to '{restore_path}'.", fg="green"))


@trash.command(name="empty")
def trash_empty():
    """Permanently deletes all items from the trash can."""
    if not click.confirm(click.style("This will permanently delete all items in the trash. Are you sure?", fg="red")):
        raise click.Abort()

    TRASH_DIR.mkdir(exist_ok=True)
    for item in TRASH_DIR.iterdir():
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()
    click.echo(click.style("🗑️ Trash can has been emptied.", fg="green"))


# ---
# 'task' Subcommands
# ---
@task.command(name="new")
@click.argument("title")
def task_new(title: str):
    """Creates a new task in the backlog."""
    # ... (implementation is the same)
    click.echo(click.style(f"🚀 Creating new task: '{title}'...", fg="cyan"))
    task_dirs = CONFIG["tasks"]["status_map"]
    backlog_dir = PROJECT_ROOT / task_dirs["backlog"]
    template_path = PROJECT_ROOT / CONFIG["tasks"]["template"]
    backlog_dir.mkdir(parents=True, exist_ok=True)
    new_task_filename = f"{title}.md"
    new_task_path = backlog_dir / new_task_filename
    if new_task_path.exists():
        click.echo(click.style(f"⚠️  Warning: Task '{title}' already exists.", fg="yellow"))
        return
    shutil.copy(template_path, new_task_path)
    with open(new_task_path, "r+") as f:
        content = f.read()
        human_readable_title = title.replace("-", " ").capitalize()
        content = content.replace("[请在这里填写任务的简明标题]", human_readable_title)
        f.seek(0)
        f.write(content)
        f.truncate()
    click.echo(click.style(f"✅ Success! New task created at: {new_task_path.relative_to(PROJECT_ROOT)}", fg="green"))


@task.command(name="start")
@click.argument("title")
@click.option("--type", "-t", "branch_type", default="feat", help="The type of branch (e.g., feat, fix, chore).")
def task_start(title: str, branch_type: str):
    """Starts a task: creates a new branch and moves the task to 'in_progress'."""
    # ... (implementation is the same)
    click.echo(click.style(f"🚀 Starting task: '{title}'...", fg="cyan"))
    task_path = find_task_file(title)
    if not task_path:
        click.echo(click.style(f"Error: Task '{title}' not found.", fg="red"))
        raise click.Abort()
    in_progress_dir = PROJECT_ROOT / CONFIG["tasks"]["status_map"]["in_progress"]
    in_progress_dir.mkdir(parents=True, exist_ok=True)
    new_task_path = in_progress_dir / task_path.name
    branch_name = f"{branch_type}/{title}"
    click.echo(f"  - Creating and switching to branch '{branch_name}'...")
    run_git_command(["checkout", "main"])
    run_git_command(["pull"])
    run_git_command(["checkout", "-b", branch_name])
    click.echo(f"  - Moving task to 'in_progress'...")
    run_git_command(["mv", str(task_path.relative_to(PROJECT_ROOT)), str(new_task_path.relative_to(PROJECT_ROOT))])
    click.echo("  - Committing status change...")
    commit_message = f"chore(tasks): Start work on task '{title}'"
    run_git_command(["commit", "-m", commit_message])
    click.echo(click.style(f"\n✅ Success! You are now on branch '{branch_name}' and task '{title}' is in progress.", fg="green"))
    click.echo("   You can now start coding!")


@task.command(name="complete")
@click.argument("title")
def task_complete(title: str):
    """Completes a task on the current branch."""
    # ... (corrected implementation)
    click.echo(click.style(f"🎉 Completing task: '{title}'...", fg="cyan"))
    task_path = find_task_file(title)
    if not task_path:
        click.echo(click.style(f"Error: Task '{title}' not found.", fg="red"))
        raise click.Abort()
    in_progress_dir_str = str(PROJECT_ROOT / CONFIG["tasks"]["status_map"]["in_progress"])
    if str(task_path.parent) != in_progress_dir_str:
        click.echo(click.style(f"Error: Task '{title}' is not in progress. Cannot complete.", fg="red"))
        raise click.Abort()
    done_dir = PROJECT_ROOT / CONFIG["tasks"]["status_map"]["done"]
    done_dir.mkdir(parents=True, exist_ok=True)
    new_task_path = done_dir / task_path.name
    click.echo(f"  - Moving task to 'done'...")
    run_git_command(["mv", str(task_path.relative_to(PROJECT_ROOT)), str(new_task_path.relative_to(PROJECT_ROOT))])
    click.echo("  - Committing status change...")
    commit_message = f"chore(tasks): Complete task '{title}'"
    run_git_command(["commit", "-m", commit_message])
    click.echo(click.style(f"\n✅ Success! Task '{title}' has been moved to the done folder on the current branch.", fg="green"))
    click.echo("   You can now merge this branch into main.")


# ---
# 'ai' Subcommands
# ---
@ai.command(name="lint-fix")
@click.argument("path", type=click.Path(exists=True, path_type=Path))
def ai_lint_fix(path: Path):
    """Automatically fixes linting errors in a file with Ruff."""
    click.echo(click.style(f"⚡ Running lint-fix on '{path}'...", fg="cyan"))
    run_command(["ruff", "check", str(path), "--fix"])
    click.echo(click.style("✅ Lint-fix complete.", fg="green"))


@ai.command(name="format")
@click.argument("path", type=click.Path(exists=True, path_type=Path))
def ai_format(path: Path):
    """Automatically formats a Python file with Black."""
    click.echo(click.style(f"🎨 Running format on '{path}'...", fg="cyan"))
    run_command(["black", str(path)])
    click.echo(click.style("✅ Formatting complete.", fg="green"))


@ai.command(name="doctor")
@click.argument("path", type=click.Path(exists=True, path_type=Path))
def ai_doctor(path: Path):
    """Runs a full suite of checks and provides a prompt for AI to fix issues."""
    click.echo(click.style(f"🩺 Running doctor on '{path}'...", fg="cyan"))

    # 1. Run safe auto-fixes first
    run_command(["ruff", "check", str(path), "--fix"], quiet=True)
    run_command(["black", str(path)], quiet=True)
    click.echo("  - Auto-formatting and lint fixing applied.")

    # 2. Run static type checking
    click.echo("  - Running static type check with Mypy...")
    try:
        mypy_output = run_command(["mypy", str(path)], quiet=True)
        click.echo(click.style("  - ✅ Mypy found no issues.", fg="green"))
    except click.Abort:
        # Mypy returns a non-zero exit code on errors, which run_command catches.
        # We need to re-run it to capture the output for the prompt.
        mypy_output = subprocess.run(["mypy", str(path)], capture_output=True, text=True, cwd=PROJECT_ROOT).stdout

    if "Success: no issues found" in mypy_output:
        click.echo(click.style("\n✨ Doctor found no remaining issues. The code is healthy!", fg="green"))
        return

    # 3. Generate a prompt for the AI
    click.echo(click.style("\n  - ⚠️  Mypy found issues. Generating AI prompt...", fg="yellow"))

    with open(path, "r") as f:
        file_content = f.read()

    prompt = f"""
---
**AI TASK: FIX STATIC TYPE ERRORS**

**Context:**
The 'doctor' command was run on the following file, and after auto-formatting, static type errors were found. Your task is to analyze the errors and the code, and provide a corrected version of the file.

**File Path:** `{path}`

**Mypy Errors:**
```
{mypy_output.strip()}
```

**File Content:**
```python
{file_content}
```

**Instructions:**
1.  Carefully analyze the Mypy errors.
2.  Modify the Python code to fix all the type errors.
3.  Provide the complete, corrected content of the file in your response.
---
"""
    click.echo(prompt)


if __name__ == "__main__":
    cli()
