# Template Upgrading Guide

This guide explains how to incorporate updates from the CodeCraftAI template into your own project.

## Strategy

The core principle is to treat the template as an upstream remote repository.

1.  **Add the template as a remote:**
    ```bash
    git remote add template https://github.com/napoler/CodeCraftAI.git
    ```

2.  **Fetch updates:**
    ```bash
    git fetch template
    ```

3.  **Merge or cherry-pick changes:**
    You can merge changes from the template's main branch. Be aware of merge conflicts, especially in configuration files.
    ```bash
    git merge template/main --allow-unrelated-histories
    ```
