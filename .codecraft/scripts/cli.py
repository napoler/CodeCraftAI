#!/usr/bin/env python
import datetime
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
LOCAL_CONFIG_PATH = PROJECT_ROOT / ".codecraft" / ".local_config.yml"
TRASH_DIR = PROJECT_ROOT / ".trash"


# ---
# Helper Functions
# ---
def load_yaml_config(config_path: Path, default: dict = None) -> dict:
    """Loads a YAML configuration file."""
    if not config_path.exists():
        if default is not None:
            return default
        click.echo(
            click.style(f"Error: Config file not found at {config_path}", fg="red")
        )
        raise click.Abort()
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        click.echo(
            click.style(
                f"Error: Could not parse config file {config_path}: {e}", fg="red"
            )
        )
        raise click.Abort()


def save_local_config(config: dict):
    """Saves the local configuration."""
    with open(LOCAL_CONFIG_PATH, "w", encoding="utf-8") as f:
        yaml.dump(config, f, default_flow_style=False)


CONFIG = load_yaml_config(WORKFLOW_CONFIG_PATH)
LOCAL_CONFIG = load_yaml_config(LOCAL_CONFIG_PATH, default={})
PROTECTED_PATHS = load_yaml_config(PROTECTED_PATHS_CONFIG_PATH).get("protected", [])


def get_user_lang() -> str:
    """Gets the user's preferred language, falling back to the default."""
    return LOCAL_CONFIG.get("language", CONFIG["languages"]["default"])


def is_protected(path: Path) -> bool:
    """Checks if a given path is in the protected list."""
    try:
        relative_path_str = str(path.relative_to(PROJECT_ROOT))
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


def run_command(
    command: list[str], cwd: Path | None = PROJECT_ROOT, quiet: bool = False
) -> str:
    """Runs a command and handles errors."""
    try:
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
            cwd=cwd,
            encoding="utf-8",
        )
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
    """CodeCraftAI CLI: Manages workflows, tools, and configuration."""
    pass


@cli.group()
def task():
    """Commands for managing tasks."""
    pass


@cli.group()
def ai():
    """Smart commands for AI-assisted code optimization."""
    pass


@cli.group()
def trash():
    """Commands for managing the trash can."""
    pass


@cli.group()
def config():
    """Manages local project configuration."""
    pass


@cli.group()
def docs():
    """Commands for interacting with project documentation."""
    pass


# ---
# Core Commands
# ---
@cli.command()
@click.argument("path", type=click.Path(exists=True, path_type=Path))
def delete(path: Path):
    """Safely deletes a file or directory by moving it to the .trash."""
    absolute_path = path.resolve()
    if is_protected(absolute_path):
        click.echo(
            click.style(
                f"Error: Path '{path}' is protected and cannot be deleted.", fg="red"
            )
        )
        raise click.Abort()

    click.echo(f"Preparing to delete: {path}")
    q1 = "1. What is the purpose of this file/directory?"
    a1 = click.prompt(q1)
    q2 = "2. Why does it need to be deleted?"
    a2 = click.prompt(q2)
    q3 = "3. What are the potential negative consequences of deleting it?"
    a3 = click.prompt(q3)

    if not click.confirm(
        click.style("\nAre you sure you want to move this to the trash?", fg="yellow")
    ):
        raise click.Abort()

    TRASH_DIR.mkdir(exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    trash_path = TRASH_DIR / f"{timestamp}_{path.name}"

    shutil.move(str(path), trash_path)

    log_file_path = CONFIG["directories"]["project_logs"]
    if not log_file_path.endswith("/"):
        log_file_path += "/"
    log_file = PROJECT_ROOT / log_file_path / "ai_interactions.md"

    with open(log_file, "a", encoding="utf-8") as f:
        f.write("\n---\n")
        f.write(f"### File Deletion Log: {datetime.datetime.now().isoformat()}\n")
        f.write(f"- **File:** `{path}`\n")
        f.write("- **Action:** Moved to trash.\n")
        f.write(f"- **Q1 (Purpose):** {a1}\n")
        f.write(f"- **Q2 (Reason):** {a2}\n")
        f.write(f"- **Q3 (Consequences):** {a3}\n")

    click.echo(click.style(f"✅ Successfully moved '{path}' to the trash.", fg="green"))


@trash.command(name="list")
def trash_list():
    """Lists all items in the trash can."""
    TRASH_DIR.mkdir(exist_ok=True)
    items = list(TRASH_DIR.iterdir())
    if not items:
        click.echo("The trash can is empty.")
        return
    click.echo("Items in trash:")
    for item in sorted(items):
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
        click.echo(
            click.style(f"Error: Path '{restore_path}' already exists.", fg="red")
        )
        raise click.Abort()

    shutil.move(str(trash_path), restore_path)
    click.echo(
        click.style(f"✅ Successfully restored to '{restore_path}'.", fg="green")
    )


@trash.command(name="empty")
def trash_empty():
    """Permanently deletes all items from the trash can."""
    if not click.confirm(
        click.style(
            "This will permanently delete all items in the trash. Are you sure?",
            fg="red",
        )
    ):
        raise click.Abort()

    TRASH_DIR.mkdir(exist_ok=True)
    for item in TRASH_DIR.iterdir():
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()
    click.echo(click.style("🗑️ Trash can has been emptied.", fg="green"))


@task.command(name="new")
@click.argument("title")
def task_new(title: str):
    """Creates a new task in the backlog using the configured language."""
    lang = get_user_lang()
    click.echo(
        click.style(f"🚀 Creating new task: '{title}' (Language: {lang})...", fg="cyan")
    )

    try:
        template_path_str = CONFIG["tasks"]["templates"][lang]
    except KeyError:
        default_lang = CONFIG["languages"]["default"]
        click.echo(
            click.style(
                f"Warning: No '{lang}' task template found. Falling back to default '{default_lang}'.",
                fg="yellow",
            )
        )
        template_path_str = CONFIG["tasks"]["templates"][default_lang]

    template_path = PROJECT_ROOT / template_path_str
    task_dirs = CONFIG["tasks"]["status_map"]
    backlog_dir = PROJECT_ROOT / task_dirs["backlog"]
    backlog_dir.mkdir(parents=True, exist_ok=True)
    new_task_filename = f"{title}.md"
    new_task_path = backlog_dir / new_task_filename

    if new_task_path.exists():
        click.echo(
            click.style(f"⚠️  Warning: Task '{title}' already exists.", fg="yellow")
        )
        return

    try:
        shutil.copy(template_path, new_task_path)
    except FileNotFoundError:
        click.echo(
            click.style(
                f"Error: Task template not found at '{template_path}'", fg="red"
            )
        )
        raise click.Abort()

    with open(new_task_path, "r+", encoding="utf-8") as f:
        content = f.read()
        human_readable_title = title.replace("-", " ").capitalize()
        content = content.replace("[请在这里填写任务的简明标题]", human_readable_title)
        content = content.replace(
            "[Enter a concise title for the task here]", human_readable_title
        )
        f.seek(0)
        f.write(content)
        f.truncate()
    click.echo(
        click.style(
            f"✅ Success! New task created at: {new_task_path.relative_to(PROJECT_ROOT)}",
            fg="green",
        )
    )


@task.command(name="start")
@click.argument("title")
@click.option(
    "--type",
    "-t",
    "branch_type",
    default="feat",
    help="The type of branch (e.g., feat, fix, chore).",
)
def task_start(title: str, branch_type: str):
    """Starts a task: creates a new branch and moves the task to 'in_progress'."""
    click.echo(click.style(f"🚀 Starting task: '{title}'...", fg="cyan"))
    task_path = find_task_file(title)
    if not task_path:
        click.echo(click.style(f"Error: Task '{title}' not found.", fg="red"))
        raise click.Abort()

    in_progress_dir = PROJECT_ROOT / CONFIG["tasks"]["status_map"]["in_progress"]
    in_progress_dir.mkdir(parents=True, exist_ok=True)
    new_task_path = in_progress_dir / task_path.name
    branch_name = f"{branch_type}/{title}"

    click.echo("  - Ensuring main branch is up-to-date...")
    run_git_command(["checkout", "main"])
    run_git_command(["pull"])

    click.echo(f"  - Creating and switching to branch '{branch_name}'...")
    run_git_command(["checkout", "-b", branch_name])

    click.echo("  - Moving task to 'in_progress'...")
    run_git_command(
        [
            "mv",
            str(task_path.relative_to(PROJECT_ROOT)),
            str(new_task_path.relative_to(PROJECT_ROOT)),
        ]
    )

    click.echo("  - Committing status change...")
    commit_message = f"chore(tasks): Start work on task '{title}'"
    run_git_command(["add", str(new_task_path.relative_to(PROJECT_ROOT))])
    run_git_command(["commit", "-m", commit_message])
    click.echo(
        click.style(
            f"\n✅ Success! You are now on branch '{branch_name}' and task '{title}' is in progress.",
            fg="green",
        )
    )
    click.echo("   You can now start coding!")


@task.command(name="complete")
@click.argument("title")
def task_complete(title: str):
    """Completes a task on the current branch."""
    click.echo(click.style(f"🎉 Completing task: '{title}'...", fg="cyan"))
    task_path = find_task_file(title)
    if not task_path:
        click.echo(click.style(f"Error: Task '{title}' not found.", fg="red"))
        raise click.Abort()

    in_progress_dir_str = str(
        PROJECT_ROOT / CONFIG["tasks"]["status_map"]["in_progress"]
    )
    if str(task_path.parent) != in_progress_dir_str:
        click.echo(
            click.style(
                f"Error: Task '{title}' is not in progress. Cannot complete.", fg="red"
            )
        )
        raise click.Abort()

    done_dir = PROJECT_ROOT / CONFIG["tasks"]["status_map"]["done"]
    done_dir.mkdir(parents=True, exist_ok=True)
    new_task_path = done_dir / task_path.name

    click.echo("  - Moving task to 'done'...")
    run_git_command(
        [
            "mv",
            str(task_path.relative_to(PROJECT_ROOT)),
            str(new_task_path.relative_to(PROJECT_ROOT)),
        ]
    )

    click.echo("  - Committing status change...")
    commit_message = f"chore(tasks): Complete task '{title}'"
    run_git_command(["add", str(new_task_path.relative_to(PROJECT_ROOT))])
    run_git_command(["commit", "-m", commit_message])
    click.echo(
        click.style(
            f"\n✅ Success! Task '{title}' has been moved to the done folder on the current branch.",
            fg="green",
        )
    )
    click.echo("   You can now merge this branch into main.")


@ai.command(name="lint-fix")
@click.argument("path", type=click.Path(exists=True, path_type=Path))
def ai_lint_fix(path: Path):
    """Automatically fixes linting errors in a file with Ruff."""
    click.echo(click.style(f"⚡ Running lint-fix on '{path}'...", fg="cyan"))
    run_command(["ruff", "check", str(path), "--fix", "--exit-zero"])
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

    run_command(["ruff", "check", str(path), "--fix", "--exit-zero"], quiet=True)
    run_command(["black", str(path)], quiet=True)
    click.echo("  - Auto-formatting and lint fixing applied.")

    click.echo("  - Running static type check with Mypy...")
    mypy_result = subprocess.run(
        ["mypy", str(path)],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
        encoding="utf-8",
    )
    mypy_output = mypy_result.stdout

    if "Success: no issues found" in mypy_output:
        click.echo(
            click.style(
                "\n✨ Doctor found no remaining issues. The code is healthy!",
                fg="green",
            )
        )
        return

    click.echo(
        click.style("\n  - ⚠️  Mypy found issues. Generating AI prompt...", fg="yellow")
    )
    with open(path, "r", encoding="utf-8") as f:
        file_content = f.read()

    prompt = f"""---
**AI TASK: FIX STATIC TYPE ERRORS**
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
1. Analyze the Mypy errors.
2. Modify the code to fix all type errors.
3. Provide the complete, corrected file content in your response.
---"""
    click.echo(prompt)


@config.command(name="set")
@click.argument("key")
@click.argument("value")
def config_set(key: str, value: str):
    """Sets a configuration key. e.g., 'set language zh'"""
    if key == "language":
        supported = CONFIG["languages"]["supported"]
        if value not in supported:
            click.echo(
                click.style(
                    f"Warning: '{value}' is not an officially supported language ({supported}).",
                    fg="yellow",
                )
            )
    LOCAL_CONFIG[key] = value
    save_local_config(LOCAL_CONFIG)
    click.echo(click.style(f"✅ Config set: {key} = {value}", fg="green"))


@config.command(name="get")
@click.argument("key")
def config_get(key: str):
    """Gets a configuration key."""
    value = LOCAL_CONFIG.get(key)
    click.echo(f"{key} = {value}" if value else f"Key '{key}' not set.")


@docs.command(name="get")
@click.argument("doc_name")
def docs_get(doc_name: str):
    """Gets the path to a document, respecting the user's language preference."""
    lang = get_user_lang()
    default_lang = CONFIG["languages"]["default"]

    # Simple case: doc_name.lang.md or doc_name.md
    base_name = Path(doc_name).stem

    # Search for language-specific version first
    for ext in [".md", ""]:
        # Construct path like "README.zh.md"
        path_lang = Path(f"{base_name}.{lang}{ext}")
        if path_lang.exists():
            click.echo(str(path_lang))
            return

    # Fall back to default language version
    for ext in [".md", ""]:
        path_default = Path(f"{base_name}{ext}")
        if path_default.exists():
            if lang != default_lang:
                click.echo(
                    click.style(
                        f"Note: '{lang}' version not found. Falling back to default '{default_lang}'.",
                        fg="yellow",
                    ),
                    err=True,
                )
            click.echo(str(path_default))
            return

    click.echo(
        click.style(f"Error: Document '{doc_name}' not found.", fg="red"), err=True
    )
    raise click.Abort()


if __name__ == "__main__":
    cli()
