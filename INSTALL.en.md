# Installation and Upgrade Guide

This document provides instructions for setting up and maintaining your project based on the CodeCraft template.

## 1. Initial Project Setup

Follow these steps to get your project running for the first time.

### Prerequisites

- Git
- Python 3.8+
- `pip` and `venv` (usually included with Python)

### Step-by-Step Installation

1.  **Clone the Repository:**
    Start by cloning the project template to your local machine.

    ```bash
    git clone [URL_OF_YOUR_NEW_REPOSITORY]
    cd [YOUR_REPOSITORY_NAME]
    ```

2.  **Create a Virtual Environment:**
    It is highly recommended to use a virtual environment to manage project dependencies.

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    # On Windows, use: venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    This project uses `pip-tools` to manage dependencies. The `requirements.txt` file contains the pinned dependencies for the application.

    ```bash
    pip install -r requirements.txt
    ```

4.  **Initialize Pre-commit Hooks:**
    The repository includes pre-commit hooks to ensure code quality. Install them by running:
    ```bash
    pre-commit install
    ```

5.  **Verify the Installation:**
    Check if the CLI tool is working correctly.

    ```bash
    python cli.py --help
    ```

    You should see the help menu for the command-line interface. Your project is now set up!

## 2. Upgrading the Framework

This project template is designed to evolve. As new features, bug fixes, and best practices are added to the original CodeCraft template, you may want to incorporate them into your project.

The recommended way to do this is by adding the original template repository as a remote named `upstream`.

### Step-by-Step Upgrade Process

1.  **Add the Template as an `upstream` Remote:**
    This only needs to be done once.

    ```bash
    # Replace the URL with the original CodeCraft template repository URL
    git remote add upstream https://github.com/original/codecraft-template.git
    ```

2.  **Fetch Updates from `upstream`:**
    Periodically, fetch the latest changes from the template repository.

    ```bash
    git fetch upstream
    ```

3.  **Merge Updates into Your Project:**
    Merge the changes from the `upstream/main` branch into your project's `main` branch.

    ```bash
    # Ensure you are on your main branch and have committed all your changes
    git checkout main
    git merge upstream/main --allow-unrelated-histories
    ```

    - The `--allow-unrelated-histories` flag may be needed the first time you merge.
    - Git will attempt to merge the changes automatically. If there are conflicts (e.g., you've modified a file that the template also updated), you will need to resolve them manually.

4.  **Review and Test:**
    After a successful merge, thoroughly test your application to ensure that the updates have not introduced any breaking changes. Update your dependencies if the `requirements.txt` file has changed.

    ```bash
    pip install -r requirements.txt
    ```

## 3. Troubleshooting

- **`command not found: pre-commit`**: This means the pre-commit package is not installed correctly. Ensure your virtual environment is active and run `pip install pre-commit`.
- **Merge Conflicts during Upgrade**: This is normal if you have customized the core template files. Carefully review the conflicts in your code editor, choose the correct version (yours, the template's, or a combination), and then commit the resolved files.
