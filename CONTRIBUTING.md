# Contribution Guidelines

> [!NOTE]
> **[Template File - Do Not Modify Directly]**
>
> This file is part of the CodeCraftAI core template. To facilitate conflict-free upgrades, please **do not modify this file directly**.
>
> If you need to add project-specific contribution guidelines, create a new file in the `project_docs/` directory.

[中文版 (Chinese Version)](./CONTRIBUTING.zh.md)

---

Welcome! This guide is designed to help every member—whether human or AI—collaborate efficiently and maintain the long-term health of the project.

## 0. Fundamental Principles

### **The Meta-Rule: Documentation-First**

This is the **highest behavioral guideline** for this project.

- Before performing any action or using any automated tool provided by this project, you **must** first consult and follow the relevant official documentation. The authoritative usage standards for all tools are defined in the **[Tooling and Automation Standard](./.codecraft/docs/05-tooling-and-automation-standard.md)**.
- If there is any conflict between the documentation and your prior understanding, **the documentation is always correct**.

**Before you begin, please read our [Quick Start Tutorial (`project_docs/help/`)](./project_docs/help/)**.

## 1. Core Philosophy: CLI-Driven Development

The core of this project is the **command-line assistant (`cli.py`)**. It encapsulates all our complex Git workflows, project management, and code quality checks into simple, unified commands.

**All developers (human and AI) must prioritize using `cli.py` to interact with the project.** This is a requirement, not a suggestion, as it has all our process rules and safety checks built-in.

## 2. AI Safety Red Lines

This is a set of **mandatory, highest-priority guidelines** for AI developers.

### **Red Line 1: Prohibition of Native File Deletion**
- AI is **strictly forbidden** from using any native OS delete commands, such as `rm`, `del`, etc.
- **Mandatory**: All file deletion operations **must** be performed through our provided safe command-line tool:
  ```bash
  python .codecraft/scripts/cli.py delete <file_path>
  ```
- **Reason**: This command has a built-in, mandatory risk-assessment questionnaire and a recoverable "trash can" mechanism, serving as the primary defense against catastrophic accidental deletions.

### **Red Line 2: Prohibition of Direct Modification of Protected Files**
- This project defines a list of "protected paths" in the `.codecraft/protected_paths.yml` file.
- AI is **strictly forbidden** from directly modifying, moving, or deleting any file on this list.
- **Mandatory**: If an AI determines that a protected file needs to be modified, it **must** halt its operation and explicitly request review and approval from a human developer by mentioning **`@user`**.

### **Red Line 3: Adherence to Error Handling & Logging Standard**
- All code **must** strictly adhere to the project's defined **[Error Handling and Logging Standard](./.codecraft/docs/04-error-handling-and-logging-standard.md)**.
- When handling any potentially fallible operation (e.g., file I/O, network requests), you must use a `try...except` structure and log meaningful errors. Silently ignoring exceptions is strictly forbidden.

---

## 3. Standard Development Workflow (CLI-Driven)

Please follow the end-to-end tutorial in `project_docs/help/01-quick-start-with-cli.md`. A summary of the core steps is below:

1.  **Create a Task**:
    `python .codecraft/scripts/cli.py task new <task-title>`
2.  **Start a Task**:
    `python .codecraft/scripts/cli.py task start <task-title>`
    *(This automatically creates a branch, moves the task file, and makes the first commit.)*
3.  **Code and Design**:
    - Write your code.
    - Write or update the corresponding `specs/` file.
4.  **Code Quality Optimization (Mandatory for AI)**:
    Before committing, run the "code doctor" on every file you've modified:
    `python .codecraft/scripts/cli.py ai doctor <file_path>`
    *(This auto-formats, fixes lint errors, and generates a precise prompt for any remaining type errors.)*
5.  **Complete the Task**:
    `python .codecraft/scripts/cli.py task complete <task-title>`
    *(This moves the task to the `done/` directory and creates a commit.)*
6.  **Create a Pull Request**:
    - Push your branch to the remote repository.
    - Create a Pull Request and link to the relevant task and spec files in the description.

## 4. Git Conventions

While `cli.py` handles most Git operations, you still need to adhere to the following:

### **Branch Naming**
The CLI automatically generates branch names that follow the `type/short-description` format (e.g., `feat/user-login`).

### **Commit Messages**
We adhere to the **Conventional Commits** specification (`<type>: <description>`). CLI-generated commits automatically follow this. Please do the same for your own code commits.

**`<type>`** must be one of the following:
*   **feat**: A new feature
*   **fix**: A bug fix
*   **docs**: Documentation changes
*   **refactor**: A code change that neither fixes a bug nor adds a feature
*   **test**: Adding missing tests or correcting existing tests
*   **chore**: Changes to the build process or auxiliary tools

## 5. Local Full Build Verification

Before creating a Pull Request, you **must** run the local full build script and ensure all checks pass:

```bash
bash .codecraft/scripts/build.sh
```
This script is the final quality gate and simulates all checks that will be run by the CI pipeline.

Thank you for your contribution!
