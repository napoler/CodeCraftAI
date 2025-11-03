#!/usr/bin/env python
import datetime
import shutil
import subprocess
from pathlib import Path

import click
from click import Abort, echo, style
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
# Protected paths will be loaded later, as the file might not exist yet.


def get_protected_paths() -> list:
    """Loads the protected paths configuration."""
    if not PROTECTED_PATHS_CONFIG_PATH.exists():
        return []
    config = load_yaml_config(PROTECTED_PATHS_CONFIG_PATH)
    return config.get("protected", [])


def get_user_lang() -> str:
    """Gets the user's preferred language, falling back to the default."""
    return LOCAL_CONFIG.get("language", CONFIG["languages"]["default"])


def is_protected(path: Path) -> bool:
    """Checks if a given path is in the protected list."""
    try:
        relative_path_str = str(path.relative_to(PROJECT_ROOT))
        for protected_path in get_protected_paths():
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
def spec():
    """Commands for managing specification documents."""
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

    logs_dir = PROJECT_ROOT / CONFIG["directories"]["project_logs"]
    logs_dir.mkdir(parents=True, exist_ok=True)
    log_file = logs_dir / "ai_interactions.md"

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


@task.command(name="create")
@click.argument("title")
def task_create(title: str):
    """Creates a new task in the backlog using the configured language."""
    lang = get_user_lang()
    click.echo(
        click.style(f"🚀 Creating new task: '{title}' (Language: {lang})...", fg="cyan")
    )

    template_path_str = CONFIG["tasks"]["templates"][lang]
    template_path = PROJECT_ROOT / template_path_str

    backlog_dir = PROJECT_ROOT / CONFIG["tasks"]["status_map"]["backlog"]
    backlog_dir.mkdir(parents=True, exist_ok=True)

    new_task_path = backlog_dir / f"{title}.md"

    if new_task_path.exists():
        click.echo(
            click.style(f"⚠️  Warning: Task '{title}' already exists.", fg="yellow")
        )
        return

    # Ensure template file exists before copying
    if not template_path.exists():
        click.echo(
            click.style(
                f"Error: Task template not found at '{template_path}'. Creating a blank file.",
                fg="red",
            )
        )
        template_content = f"# Task: {title.replace('-', ' ').capitalize()}"
        with open(new_task_path, "w", encoding="utf-8") as f:
            f.write(template_content)
    else:
        shutil.copy(template_path, new_task_path)
        with open(new_task_path, "r+", encoding="utf-8") as f:
            content = f.read()
            human_readable_title = title.replace("-", " ").capitalize()
            content = content.replace(
                "[Enter a concise title for the task here]", human_readable_title
            )
            content = content.replace(
                "[请在这里填写任务的简明标题]", human_readable_title
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


@spec.command(name="create")
@click.argument("task_title")
def spec_create(task_title: str):
    """Creates a new specification for a given task."""
    task_file = find_task_file(task_title)
    if not task_file:
        click.echo(click.style(f"Error: Task '{task_title}' not found.", fg="red"))
        raise click.Abort()

    lang = get_user_lang()
    click.echo(f"🚀 Creating new spec for task: '{task_title}' (Language: {lang})...")

    template_path_str = CONFIG["specs"]["templates"][lang]
    template_path = PROJECT_ROOT / template_path_str

    specs_dir = PROJECT_ROOT / CONFIG["directories"]["specs"]
    specs_dir.mkdir(parents=True, exist_ok=True)

    new_spec_path = specs_dir / f"{task_title}.{lang}.md"

    if new_spec_path.exists():
        click.echo(
            click.style(
                f"⚠️  Warning: Spec for task '{task_title}' already exists.",
                fg="yellow",
            )
        )
        return

    if not template_path.exists():
        click.echo(
            click.style(
                f"Error: Spec template not found at '{template_path}'. Creating a blank file.",
                fg="red",
            )
        )
        template_content = (
            f"# Specification: {task_title.replace('-', ' ').capitalize()}"
        )
        with open(new_spec_path, "w", encoding="utf-8") as f:
            f.write(template_content)
    else:
        shutil.copy(template_path, new_spec_path)
        with open(new_spec_path, "r+", encoding="utf-8") as f:
            content = f.read()
            human_readable_title = task_title.replace("-", " ").capitalize()
            content = content.replace("[Feature or Change Title]", human_readable_title)
            content = content.replace("[功能或变更的标题]", human_readable_title)
            f.seek(0)
            f.write(content)
            f.truncate()

    click.echo(
        click.style(
            f"✅ Success! New spec created at: {new_spec_path.relative_to(PROJECT_ROOT)}",
            fg="green",
        )
    )


@cli.command()
@click.argument("task_title")
@click.option(
    "--type", "-t", "branch_type", default="feat", help="Branch type (e.g., feat, fix)."
)
def start(task_title: str, branch_type: str):
    """Starts a task: creates a branch and moves the task file."""
    click.echo(click.style(f"🚀 Starting task: '{task_title}'...", fg="cyan"))
    task_path = find_task_file(task_title)
    if not task_path:
        click.echo(click.style(f"Error: Task '{task_title}' not found.", fg="red"))
        raise click.Abort()

    in_progress_dir = PROJECT_ROOT / CONFIG["tasks"]["status_map"]["in_progress"]
    in_progress_dir.mkdir(parents=True, exist_ok=True)
    new_task_path = in_progress_dir / task_path.name
    branch_name = f"{branch_type}/{task_title}"

    click.echo("  - Ensuring main branch is up-to-date...")
    run_git_command(["checkout", "main"])
    run_git_command(["pull"])

    click.echo(f"  - Creating and switching to branch '{branch_name}'...")
    run_git_command(["checkout", "-b", branch_name])

    click.echo("  - Moving task to 'in_progress'...")
    shutil.move(str(task_path), str(new_task_path))

    click.echo("  - Committing status change...")
    commit_message = f"chore(tasks): Start work on task '{task_title}'"
    run_git_command(["add", str(new_task_path.relative_to(PROJECT_ROOT))])
    run_git_command(["commit", "-m", commit_message])

    click.echo(
        click.style(f"\n✅ Success! You are on branch '{branch_name}'.", fg="green")
    )


@cli.command()
@click.argument("task_title")
def complete(task_title: str):
    """Completes a task on the current branch."""
    click.echo(click.style(f"🎉 Completing task: '{task_title}'...", fg="cyan"))
    task_path = find_task_file(task_title)
    if not task_path:
        click.echo(click.style(f"Error: Task '{task_title}' not found.", fg="red"))
        raise click.Abort()

    done_dir = PROJECT_ROOT / CONFIG["tasks"]["status_map"]["done"]
    done_dir.mkdir(parents=True, exist_ok=True)
    new_task_path = done_dir / task_path.name

    click.echo("  - Moving task to 'done'...")
    shutil.move(str(task_path), str(new_task_path))

    click.echo("  - Committing status change...")
    commit_message = f"chore(tasks): Complete task '{task_title}'"
    run_git_command(["add", str(new_task_path.relative_to(PROJECT_ROOT))])
    run_git_command(["commit", "-m", commit_message])

    click.echo(click.style(f"\n✅ Success! Task '{task_title}' is done.", fg="green"))


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


@cli.command()
def init():
    """Initializes the CodeCraft framework in a project safely."""
    click.echo(click.style("🚀 Initializing CodeCraft Framework...", fg="cyan"))

    # Directories to create
    dirs_to_create = [
        PROJECT_ROOT / ".codecraft" / "scripts",
        PROJECT_ROOT / ".codecraft" / "templates",
        PROJECT_ROOT / "docs" / "adr",
        PROJECT_ROOT / "docs" / "specs",
        PROJECT_ROOT / "docs" / "framework",
        PROJECT_ROOT / "docs" / "project",
        PROJECT_ROOT / "project_logs",
        PROJECT_ROOT / "tasks" / "backlog",
    ]
    for directory in dirs_to_create:
        directory.mkdir(parents=True, exist_ok=True)
        click.echo(
            f"  - Ensuring directory exists: {directory.relative_to(PROJECT_ROOT)}"
        )

    # Files to copy/template
    # files_to_handle = {
    #     ".pre-commit-config.yaml": ".pre-commit-config.yaml",
    #     ".codecraft/workflow.yml": ".codecraft/workflow.yml",
    #     ".gitignore": ".gitignore",
    # }

    # This assumes the cli.py is running from within a cloned repo structure temporarily
    # A more robust solution might package templates inside the script itself
    # For now, let's assume we can access them via a relative path for init purposes.

    # This part is complex because the script needs to find its *own* source templates
    # to copy them. For now, we will simulate this by checking for existence and warning.

    click.echo(
        click.style(
            "\nNOTE: This is a simulated init. In a real scenario, it would copy framework files.",
            fg="yellow",
        )
    )
    click.echo(
        click.style(
            "In this environment, it just ensures directories are present.", fg="yellow"
        )
    )
    click.echo(
        click.style(
            "A full implementation would require packaging templates or a more complex file access strategy.",
            fg="yellow",
        )
    )

    click.echo(click.style("\n✅ Framework initialized safely.", fg="green"))


def parse_task_metadata(task_path: Path) -> dict:
    """Parses metadata from the top of a task file."""
    metadata = {"path": task_path, "title": task_path.stem}
    try:
        with open(task_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip() == "---":
                    break
                if ":" in line:
                    key, value = line.split(":", 1)
                    metadata[key.strip().lower()] = value.strip()
    except Exception:
        # Ignore parsing errors for robustness
        pass
    return metadata


@cli.command()
def suggest():
    """Suggests the next task to work on based on priority and dependencies."""
    click.echo(
        click.style("🔍 Analyzing tasks to suggest the next action...", fg="cyan")
    )

    task_dirs = [
        PROJECT_ROOT / CONFIG["tasks"]["status_map"]["backlog"],
        PROJECT_ROOT / CONFIG["tasks"]["status_map"]["todo"],
    ]

    done_dir = PROJECT_ROOT / CONFIG["tasks"]["status_map"]["done"]
    done_tasks = {p.stem for p in done_dir.glob("*.md")}

    all_tasks = []
    for directory in task_dirs:
        if directory.exists():
            all_tasks.extend([parse_task_metadata(p) for p in directory.glob("*.md")])

    unblocked_tasks = []
    for task in all_tasks:
        deps_raw = task.get("dependencies", "[]")
        # Simple parsing for dependencies like `[#001, #002]`
        deps = {
            d.strip().replace("#", "")
            for d in deps_raw.strip("[]").split(",")
            if d.strip()
        }
        if not deps or deps.issubset(done_tasks):
            unblocked_tasks.append(task)
        else:
            click.echo(
                click.style(
                    f"  - Task '{task['title']}' is blocked by dependencies.",
                    fg="yellow",
                )
            )

    # Advanced sorting: Type -> Priority
    priority_map = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    type_map = {"bug": 0, "feature": 1, "chore": 2}

    unblocked_tasks.sort(
        key=lambda t: (
            type_map.get(t.get("type", "feature").lower(), 2),
            priority_map.get(t.get("priority", "medium").lower(), 2),
        )
    )

    if not unblocked_tasks:
        click.echo(
            click.style(
                "\n✅ All tasks are either completed or blocked. Nothing to suggest.",
                fg="green",
            )
        )
        return

    click.echo(
        click.style("\n💡 Here are the suggested next tasks to work on:", fg="green")
    )
    for i, task in enumerate(unblocked_tasks[:5]):
        task_type = task.get("type", "Feature").capitalize()
        priority = task.get("priority", "Medium").capitalize()
        click.echo(
            f"  {i+1}. {task['title']} "
            f"({click.style(task_type, fg='blue')}, "
            f"{click.style(priority, fg='magenta')})"
        )


@cli.group()
def context():
    """Commands for the Context Engineering Engine."""
    pass


@context.command(name="build")
@click.argument("task_title")
def context_build(task_title: str):
    """Builds a temporary context file for an AI agent to start a task."""
    click.echo(style(f"🚀 Building context for task: '{task_title}'...", fg="cyan"))

    task_file = find_task_file(task_title)
    if not task_file:
        echo(style(f"Error: Task '{task_title}' not found.", fg="red"), err=True)
        raise Abort()

    task_meta = parse_task_metadata(task_file)
    context_content = [f"# AI CONTEXT FOR: {task_title}\n"]
    context_content.append("## 1. Core Task\n")
    context_content.append(f"- **Summary:** {task_meta.get('summary', 'N/A')}")
    context_content.append(f"- **File:** `{task_file.relative_to(PROJECT_ROOT)}`\n")

    # This is a simplified implementation. A real version would parse
    # dependencies and links from the task file to find related docs.
    # For now, we'll just link to the spec if it exists.

    spec_path_en = PROJECT_ROOT / CONFIG["directories"]["specs"] / f"{task_title}.en.md"
    spec_path_zh = PROJECT_ROOT / CONFIG["directories"]["specs"] / f"{task_title}.zh.md"

    spec_path = None
    if spec_path_en.exists():
        spec_path = spec_path_en
    elif spec_path_zh.exists():
        spec_path = spec_path_zh

    if spec_path:
        spec_meta = parse_task_metadata(spec_path)
        context_content.append("## 2. Primary Specification\n")
        context_content.append(f"- **Summary:** {spec_meta.get('summary', 'N/A')}")
        context_content.append(f"- **File:** `{spec_path.relative_to(PROJECT_ROOT)}`\n")

    summary_path = PROJECT_ROOT / "docs/summaries" / f"{task_title}.en.md"  # Simplified
    if summary_path.exists():
        summary_meta = parse_task_metadata(summary_path)
        context_content.append("## 3. Feature Summary\n")
        context_content.append(f"- **Summary:** {summary_meta.get('summary', 'N/A')}")
        context_content.append(
            f"- **File:** `{summary_path.relative_to(PROJECT_ROOT)}`\n"
        )

    context_file_path = PROJECT_ROOT / ".temp_context.md"
    with open(context_file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(context_content))

    echo(style("✅ Context built successfully at: .temp_context.md", fg="green"))
    echo("AI agent should now read this file to begin its work.")


@context.command(name="query")
@click.argument("search_term")
def context_query(search_term: str):
    """Performs a quick search across the knowledge base."""
    click.echo(
        style(f"🔍 Searching for '{search_term}' in the knowledge base...", fg="cyan")
    )

    search_dirs = [
        PROJECT_ROOT / "docs",
        PROJECT_ROOT / "project_logs",
        PROJECT_ROOT / "src",
    ]

    results = []
    for directory in search_dirs:
        if directory.exists():
            try:
                # Use git grep for speed and respecting .gitignore
                output = run_command(
                    ["git", "grep", "-l", search_term, "--", str(directory)], quiet=True
                )
                results.extend(output.splitlines())
            except Exception:
                continue  # Ignore errors if no match is found

    if not results:
        echo(style(f"No results found for '{search_term}'.", fg="yellow"))
        return

    echo(style("\nFound potential matches in the following files:", fg="green"))
    for file_path in results[:10]:  # Limit to top 10 results
        echo(f"  - {file_path}")


if __name__ == "__main__":
    cli()
