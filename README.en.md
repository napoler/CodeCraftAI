# CodeCraft AI Development Framework

Welcome to CodeCraft, a structured, documentation-driven framework for professional AI-powered software development. This project provides a complete ecosystem of tools, workflows, and safety features to ensure that AI agents can contribute to your codebase in a predictable, safe, and efficient manner.

This framework is built on the **"Documentation-First"** principle: all processes, standards, and protocols are explicitly defined in documentation, which serves as the ultimate source of truth for both human and AI developers.

## Key Features

- **Spec-Driven Workflow**: A mandatory development process that requires a detailed specification (`spec`) before any code is written.
- **CLI Automation**: A powerful Command-Line Interface (`cli.py`) that manages the entire development lifecycle, from task creation to completion.
- **AI Safety Protocols**: A multi-layered safety system, including a `.trash/` directory for safe file deletion and a manifest of protected files to prevent accidental modification of critical code.
- **Built-in Quality Assurance**: Integrated `pre-commit` hooks with `black` for formatting and `ruff` for linting, ensuring code quality from the start.
- **Internationalization**: Full bilingual support (English and Chinese) for all core documentation.

## Getting Started

To begin using this framework, please follow the detailed setup instructions.

- **[Installation Guide (`INSTALL.en.md`)](./INSTALL.en.md)**

## Protocol for AI Agents

This project is designed to be used by AI developers. A strict protocol has been defined to guide their operations. All AI agents must adhere to these instructions.

- **[AI Agent Protocol (`AIAgents.en.md`)](./AIAgents.en.md)**

## Core Concepts

- **Tasks**: Units of work, defined in `.md` files and managed in `tasks/`.
- **Specs**: Detailed technical designs created for each task, managed in `specs/`.
- **ADRs**: Architecture Decision Records for documenting significant architectural choices, managed in `adr/`.

This project structure enforces a clear separation of concerns and ensures that every change is well-documented and thoughtfully implemented.
