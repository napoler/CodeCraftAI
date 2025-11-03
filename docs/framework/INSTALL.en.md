# Installation & Integration Guide

This guide provides instructions for setting up this framework for both new and existing projects. The core principle is **non-invasion**; this framework should enhance, not disrupt, your existing codebase.

## Part 1: For Brand New Projects

This is the most straightforward approach.

1.  **Clone the Repository:**
    Clone this repository to your local machine to use it as a starting point.
    ```bash
    git clone [URL_OF_THIS_FRAMEWORK_REPOSITORY] your-new-project-name
    cd your-new-project-name
    ```
2.  **Initialize Your Own Git History:**
    It's best practice to remove the framework's git history and start your own.
    ```bash
    rm -rf .git
    git init
    git add .
    git commit -m "Initial project setup from CodeCraft framework"
    ```
3.  **Run the Environment Setup:**
    Follow the standard procedure to set up your Python environment.
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    pre-commit install
    ```
    Your new project is now ready.

## Part 2: For Existing Projects (Non-Invasive Integration)

This process is designed to be completely safe and reversible. It will **never** overwrite your existing files.

1.  **Add the Framework as a Remote:**
    In your existing project's root directory, add the framework repository as a remote named `upstream-framework`.
    ```bash
    git remote add upstream-framework [URL_OF_THIS_FRAMEWORK_REPOSITORY]
    ```
2.  **Fetch the Framework Files:**
    Fetch the framework's files into your local repository.
    ```bash
    git fetch upstream-framework
    ```
3.  **Safely Inject Framework Files:**
    Check out the framework's `main` branch into a temporary branch. This allows you to copy the necessary files without complex merges.
    ```bash
    git checkout -b temp-framework-branch upstream-framework/main
    ```
4.  **Run the Safe `init` Command:**
    The framework includes a safe initialization script. Return to your project's main branch and run it.
    ```bash
    git checkout main
    python .codecraft/scripts/cli.py init
    ```
    The `init` command will:
    - Safely create core directories like `.codecraft/`, `docs/`, and `tasks/` if they don't exist.
    - Copy template files.
    - For critical files like `.gitignore` or `pyproject.toml`, if they already exist in your project, it will create a `.template` version (e.g., `.gitignore.template`) instead of overwriting. It will then instruct you to manually compare and merge the contents.

5.  **Clean Up:**
    You can now delete the temporary branch.
    ```bash
    git branch -D temp-framework-branch
    ```

## Part 3: AI Agent Execution Protocol (Installation)

**Objective:** Install and initialize the CodeCraft environment in an existing project.

**Instructions:** You are a software development AI. Execute the following steps sequentially. Halt and report any errors. You must ask for user confirmation before running the `init` command.

```yaml
- role: "AI Software Engineer"
- task: "Safe Integration of CodeCraft Framework"
- steps:
    - step: 1
      command: "git remote add upstream-framework [URL_OF_THIS_FRAMEWORK_REPOSITORY]"
      description: "Add the framework as a remote repository."
    - step: 2
      command: "git fetch upstream-framework"
      description: "Fetch the framework's files."
    - step: 3
      command: "ls -a"
      description: "Pre-check. List existing files to identify potential conflicts."
    - step: 4
      action: "request_user_confirmation"
      prompt: "I have listed the project files. The next step will run the `init` command, which will create new directories and files safely. It will not overwrite existing files but will create `.template` versions for manual merging. Do you approve to proceed?"
    - step: 5
      command: "python .codecraft/scripts/cli.py init"
      description: "Run the safe initialization script."
      precondition: "User must have approved the previous step."
```
