# Contributing Guide

Thank you for your interest in contributing to this project! This document outlines the development process, coding standards, and best practices to ensure our codebase remains clean, consistent, and maintainable.

## Python Style Guide: PEP 8

All Python code in this project must strictly adhere to the [PEP 8 style guide](https://www.python.org/dev/peps/pep-0008/).

Adherence is not optional and is automatically enforced by `black` and `ruff` via pre-commit hooks.

## The Core Philosophy: Documentation-Driven Development

This project is governed by a simple rule: **if it's not in a document, it doesn't exist.** Every change must be preceded by a `spec` or `ADR` that has been reviewed and approved.

Please follow the workflow detailed in `AIAgents.md`, which uses the `cli.py` tool to manage the development lifecycle.

## Code Style and Quality

We enforce a strict set of code style and quality standards to maintain consistency.

- **Formatting:** All Python code is automatically formatted with `black`.
- **Linting:** We use `ruff` to catch common errors and style issues.
- **Type Hinting:** All new code must be fully type-hinted and pass `mypy` checks.

These checks are automatically run by the `pre-commit` hooks, which are mandatory for all contributors.

## Code-level Documentation Standards

Clear and comprehensive documentation within the code is as important as the code itself.

### 1. Docstrings

-   All public modules, classes, functions, and methods must have a docstring.
-   We follow the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#3.8-comments-and-docstrings) for docstring formatting.
-   A docstring should clearly explain what the component does, its arguments (`Args:`), and what it returns (`Returns:`).

**Example:**
```python
def my_function(param1: int, param2: str) -> bool:
    """This is a brief description of the function.

    This section provides more detail about the function's behavior,
    edge cases, and implementation notes.

    Args:
        param1: The first parameter, representing [description].
        param2: The second parameter, representing [description].

    Returns:
        True if the operation was successful, False otherwise.
    """
    # ... function body ...
```

### 2. Inline Comments

-   Use inline comments to explain **why**, not **what**. The code should be self-evident about what it's doing. Comments should clarify complex logic, business rules, or the reasoning behind a particular implementation choice.

**Good Comment (explains 'why'):**
```python
# We use a tolerance of 1e-9 to avoid floating point precision issues.
if abs(a - b) < 1e-9:
    ...
```
**Bad Comment (explains 'what'):**
```python
# Check if a is close to b.
if abs(a - b) < 1e-9:
    ...
```

### 3. Citations and References

-   If your implementation is based on or adapted from an external source (e.g., a research paper, a blog post, a Stack Overflow answer, or another open-source project), you **must** provide a citation in the comments.
-   This gives credit, provides context for future developers, and helps in understanding the origin of the solution.

**Example:**
```python
def highly_optimized_algorithm():
    # This implementation is adapted from the algorithm described in the
    # following article: https://example.com/some-clever-algorithm
    # It has been modified to handle our specific data structures.
    ...
```

By adhering to these standards, we ensure that our project is not only functional but also understandable and easy for others to contribute to.

## File Header Standard

All new Python (`.py`) files must begin with the following header block. This ensures that every file is traceable and its purpose is understood at a glance.

```python
# -*- coding: utf-8 -*-
"""
@File    :   [File Name]
@Time    :   [YYYY-MM-DD HH:MM:SS]
@Author  :   [Author Name or AI Agent ID]
@Version :   1.0
@Desc    :   [A brief description of the file's purpose]
"""
```

- **@Author:** Use your Git user name or `AI Agent` if you are an AI.
- **Automation:** We are actively exploring a pre-commit hook to automate the insertion and timestamp update of this header.
