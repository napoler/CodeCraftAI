# Standard 05: Tooling and Automation Standard

- **Status**: Adopted
- **Version**: 1.1.0
- **Date**: 2024-08-17

---

## 1. The Supreme Principle: Documentation-Driven

This document is the **sole authoritative usage guide** for all built-in tools in this project.

All developers (especially AI developers), **must** consult and follow the rules defined in this document before performing any automated operation. If a tool's actual behavior conflicts with this document, this document is considered correct, and an issue should be raised to fix the tool.

## 2. The Toolset at a Glance

### a. The Core Workflow Assistant: `cli.py`

- **File Path**: `.codecraft/scripts/cli.py`
- **Core Purpose**: This is the **only officially designated entry point** for interacting with the project workflow. It encapsulates the complexity of project management and includes built-in safety checks.
- **When to Use**: When performing any operation related to "tasks, specs, designs, safe deletion, or code optimization." Bypassing this tool to directly execute native commands like `git mv` or `rm` is **strictly forbidden**.

#### **Main Commands (`python .codecraft/scripts/cli.py ...`)**
- `task new <title>`: Creates a new task.
- `task start <title>`: Starts a task (auto-creates branch, moves file).
- `task complete <title>`: Completes a task on the current feature branch (moves file).
- `delete <path>`: Safely deletes a file (interactive Q&A + move to trash).
- `trash list|restore|empty`: Manages the trash can.
- `ai format|lint-fix|doctor <path>`: Intelligently optimizes and fixes code.
- `--help`: View all available commands and their help text.

---

### b. The Local Integrity Verifier: `build.sh`

- **File Path**: `.codecraft/scripts/build.sh`
- **Core Purpose**: To simulate the cloud CI/CD environment locally, performing a **complete, end-to-end** project health check.
- **When to Use**: **Mandatory** to run this script and ensure all checks pass **before** creating a Pull Request.

#### **Checks Performed**
1.  Dependency Health Check (`pip check`)
2.  Static Type Checking (`mypy`)
3.  Unit Testing & Coverage (`pytest --cov`)
4.  Documentation Website Build (`mkdocs build`)
5.  Python Package Build (`python -m build`)
6.  Docker Image Build (`docker build`)

Only when this script executes successfully is your code considered "ready for review."

---

### c. The Real-Time Development Guardian: `guardian.py`

- **File Path**: `.codecraft/scripts/guardian.py`
- **Core Purpose**: To provide an **instant** code quality feedback loop, standing guard for you in the background every second you are coding.
- **When to Use**: Recommended to run in a separate terminal during any long coding session.

#### **Main Features**
- **Auto-formatting**: Automatically runs `black` when you save a `.py` file.
- **Auto-fixing**: Automatically runs `ruff --fix`.
- **Continuous Testing**: Automatically runs `pytest` and `mypy` in the background.

This tool is optional but highly recommended. It dramatically improves coding efficiency and quality by catching issues early.

---
## 3. Tool Interaction Principles & Expert Tips

- **Prioritize `cli.py`**: For any functionality provided by `cli.py`, **do not** use lower-level native commands.
- **Trust `build.sh`**: The successful execution of `build.sh` is the "gold standard" for code entering the main branch.
- **Befriend `guardian.py`**: Let the guardian be your coding partner, not an enemy you face only at the end.

### **Expert Tip for AI Developers: The `doctor` Philosophy**

The `ai doctor` command is more than just a fixer; it is a diagnostic tool.

> When `doctor` reports a `mypy` type error, do not just blindly try to silence it. An excellent engineer sees a type error as a **symptom**. Ask yourself: **Why** did this type error occur? Does it reveal a deeper flaw in the data structure design or the logic flow? Use the opportunity of fixing a type error to **refactor and improve the intrinsic quality of the code**.
