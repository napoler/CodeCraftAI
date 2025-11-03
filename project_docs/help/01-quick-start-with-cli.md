# Help Doc 01: End-to-End Quick Start with the CLI

Welcome to CodeCraftAI! This guide will walk you through a complete feature development workflow using our powerful command-line assistant, `cli.py`. This is the **highly recommended** way to collaborate on this project.

## Prerequisites

- Ensure you have followed the main `README.md` to create and activate your Python virtual environment and install all development dependencies.
- All `cli.py` commands should be run from the project root directory.

---

### Step 1: Create a New Task

Everything starts with an idea or a requirement. Let's create a task to "implement a user logout feature."

```bash
python .codecraft/scripts/cli.py task new implement-user-logout
```

**What happened?**
- The CLI tool automatically created a new task file for you, named `implement-user-logout.md`, in the `tasks/backlog/` directory.

---

### Step 2: Start Working on the Task

Now, you're ready to start coding. This command will automatically handle all the tedious setup for you.

```bash
python .codecraft/scripts/cli.py task start implement-user-logout --type fix
```
*(We use `--type fix` as this is more like a bug fix or a small feature.)*

**What happened?**
1.  **Branch Creation & Checkout**: The CLI created a new Git branch named `fix/implement-user-logout` for you and automatically checked it out.
2.  **Task Status Update**: It moved the task file from `tasks/backlog/` to `tasks/in_progress/` **using `git mv`**.
3.  **Automatic Commit**: It automatically created a commit to record this status change.

You are now in a perfect development environment to start writing code and designing your spec.

---

### Step 3: Code and Intelligently Optimize

You can now begin writing your code. During or after your coding session, you can use the `ai` command group to automatically improve your code quality.

Let's say you've modified the file `src/codecraftai/auth.py`:

1.  **Auto-fix Lint Errors**:
    ```bash
    python .codecraft/scripts/cli.py ai lint-fix src/codecraftai/auth.py
    ```
2.  **Auto-format Code**:
    ```bash
    python .codecraft/scripts/cli.py ai format src/codecraftai/auth.py
    ```
3.  **Run the "Code Doctor" (Recommended)**:
    This command first runs the two steps above, then performs a static type check, and generates a precise prompt for the AI to fix any remaining issues.
    ```bash
    python .codecraft/scripts/cli.py ai doctor src/codecraftai/auth.py
    ```

---

### Step 4: Complete the Task

Your code has passed all tests and is high quality. It's time to mark it as complete.

```bash
python .codecraft/scripts/cli.py task complete implement-user-logout
```

**What happened?**
- On your current `fix/implement-user-logout` branch, the CLI moved the task file from `tasks/in_progress/` to `tasks/done/` **using `git mv`** and created a commit.

You can now safely push this branch to the remote and create a Pull Request for review.

---

### Step 5 (If Needed): Safely Delete a File

Suppose you need to delete a temporary file, `temp_notes.md`. **Never** use the `rm` command. You must use our safe `delete` command.

```bash
python .codecraft/scripts/cli.py delete temp_notes.md
```

**What happened?**
1.  **Mandatory Risk Assessment**: The CLI forced you to answer three questions to assess the necessity and consequences of the deletion.
2.  **Moved to Trash**: The file was not permanently deleted but was moved to the `.trash/` directory.

If you made a mistake, you can easily recover the file using the `trash` command:
- `python .codecraft/scripts/cli.py trash list` (View trash contents)
- `python .codecraft/scripts/cli.py trash restore <timestamped_filename>` (Restore a file)

This CLI tool is your "safety rail," built for you and your AI. Enjoy the efficiency and security it brings!
