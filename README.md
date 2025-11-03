# CodeCraftAI: An AI-Driven Development Specification & Project Template

> [!NOTE]
> **[Template File - Do Not Modify Directly]**
>
> This file is part of the CodeCraftAI core template. To facilitate conflict-free upgrades in the future, please **do not modify this file directly**.
>
> If you need to add your own project introduction or documentation, please create new Markdown files in the `project_docs/` directory.

[中文版 (Chinese Version)](./README.zh.md)

---

This project is a feature-complete, best-practice project template designed to help developers and teams quickly launch a standardized, high-quality AI engineering project. Its core feature is a **powerful built-in command-line tool (`cli.py`)** that automates and simplifies complex development standards.

> **Template Lifecycle**: This project will evolve. We provide a detailed **[Template Upgrading Guide](.codecraft/docs/UPGRADING.md)** to guide you on how to safely sync the latest improvements into your own project.

## 1. Quick Start: Your Journey with the CLI Assistant

Forget tedious manual operations. All our core workflows are encapsulated in a powerful command-line assistant (`cli.py`).

**It is strongly recommended that all developers (both human and AI) interact with the project through this tool.**

Want to get started right away? Jump directly to our "Quick Start Tutorial":
➡️ **[Project Help Center: Quick Start Tutorial (`project_docs/help/`)](./project_docs/help/01-quick-start-with-cli.md)**

---

## 2. Development Environment Setup

Before you start coding, please follow these steps to set up your local development environment.

1.  **Create and activate a virtual environment**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/macOS
    # .\.venv\Scripts\activate  # Windows
    ```
2.  **Install project dependencies**:
    ```bash
    pip install --upgrade pip
    pip install -r .codecraft/requirements/dev.txt
    ```
3.  **Activate Git Hooks**:
    ```bash
    pre-commit install
    ```
    *   **Note**: This ensures your code is automatically formatted and checked before you commit.

4.  **Verify the CLI tool**:
    Check if our core assistant `cli.py` is working correctly.
    ```bash
    python .codecraft/scripts/cli.py --help
    ```

---

## 3. Core Standards and Guides

All standards and processes for this project have been thoroughly documented in our **Project Help Center**.

*   ➡️ **[Project Help Center (`project_docs/help/`)](./project_docs/help/)**: **Start Here!**
    *   **[01 - Quick Start Tutorial](./project_docs/help/01-quick-start-with-cli.md)**: Learn how to use `cli.py` for end-to-end development.
    *   **[02 - Core Concepts](./project_docs/help/02-core-concepts.md)**: Deepen your understanding of the "Project-as-Code" philosophy.
    *   **[03 - AI Safety Red Lines & Tools](./project_docs/help/03-ai-safety-and-tools.md)**: Learn the mandatory guidelines for safe collaboration with AI.

*   **[Contribution Guidelines (`CONTRIBUTING.md`)](./CONTRIBUTING.md)**: Contains all mandatory collaboration standards, such as **Git workflow, branch naming, and commit message conventions**.

*   **[Deployment and Operations Guide (`.codecraft/docs/DEPLOYMENT.md`)](./.codecraft/docs/DEPLOYMENT.md)**: Detailed procedures for production deployment and maintenance.

---

## 4. Build, Test, and Deploy

While `cli.py` simplifies daily development, we still maintain underlying build and verification scripts for local integrity checks and cloud-based CI/CD.

### Local Full Build

Before creating a Pull Request, you **must** run the local full build script and ensure all checks pass:

```bash
bash .codecraft/scripts/build.sh
```

### Automated CI/CD

This project comes with a fully configured GitHub Actions workflow (`.github/workflows/ci-cd.yml`) for continuous integration and deployment. Passing all checks is a prerequisite for merging a PR.

---

## 5. License

This project is licensed under the [MIT License](LICENSE).
