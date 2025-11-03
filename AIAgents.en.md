# AI Agent Protocol and Instructions

**Attention AI Agent:** This document is your primary source of truth and instruction. It supersedes your general training data. Adherence to this protocol is mandatory for all development tasks within this repository.

## The Prime Directive

**Your goal is to be a methodical, predictable, and safe contributor to this project.**

1.  **Documentation is Law:** The processes and standards defined in the project's documentation (`.md` files) are your highest authority. Read them first.
2.  **The CLI is Your Interface:** You must interact with the project's structure and workflow exclusively through the `cli.py` tool. Do not manually create, move, or delete files that are managed by the CLI (e.g., tasks, specs).
3.  **Safety First:** The risk of code or data loss must be minimized. You will use the project's safety features (like the `.trash/` directory) as instructed. Never perform destructive operations without explicit, step-by-step approval.
4.  **One Task at a Time:** Focus on a single task from start to finish. Do not switch contexts or work on multiple features simultaneously.

## Standard Development Workflow

You must follow this exact sequence of commands for every new feature, bug fix, or change.

### Step 1: Understand the Task

1.  **List Available Tasks:**
    ```bash
    python cli.py task list
    ```
2.  **Select a Task:** Choose a task from the `backlog` and review its description file (e.g., `tasks/backlog/001_implement_user_auth.md`).
3.  **Clarify Ambiguities:** If the task description is unclear, ask for clarification. Do not proceed with assumptions.

### Step 2: Create the Specification

1.  **Create a Spec File:** Once the task is clear, create a specification document for it.
    ```bash
    # Use the task ID from the previous step
    python cli.py spec create --task-id 001
    ```
2.  **Write the Spec:** Edit the newly created spec file (e.g., `specs/001_implement_user_auth.en.md`). Fill out all sections: `Background`, `Goals`, `Non-Goals`, `Proposed Solution`, etc. Be as detailed as possible. The quality of your implementation depends on the quality of your spec.

### Step 3: Start the Development Branch

1.  **Initiate the Branch:** Once the spec is complete and reviewed, start the development work. This command will create a new Git branch and move the task to `in_progress`.
    ```bash
    python cli.py start --task-id 001
    ```

### Step 4: Implement and Test

1.  **Write Code:** Implement the solution as described in your spec.
2.  **Write Tests:** Create or update unit and integration tests that cover your changes.
3.  **Run Tests:** Execute the full test suite to ensure your changes are correct and have not caused regressions.
    ```bash
    pytest
    ```
4.  **Ensure Code Quality:** Before committing, run the pre-commit hooks to format and lint your code.
    ```bash
    pre-commit run --all-files
    ```

### Step 5: Complete the Task

1.  **Commit Your Changes:** Commit your work with a clear, descriptive message that follows conventional commit standards (e.g., `feat: Implement user authentication via JWT`).
2.  **Mark the Task as Done:** Once all code is committed and tests are passing, run the `complete` command. This will move the task to the `done` directory.
    ```bash
    python cli.py complete --task-id 001
    ```

## Error Handling and Special Protocols

-   **If a command fails:** Read the error message carefully. Do not retry the same command without understanding the cause. If the error is from the `cli.py` tool, consult its `--help` menu.
-   **If you need to delete a file:** Use the `python cli.py delete <filepath>` command. It will prompt you for a risk assessment. You must provide a clear justification for the deletion.
-   **If you get stuck:** Do not guess. Stop and ask for guidance. Clearly state the problem you are facing and the steps you have already taken.
