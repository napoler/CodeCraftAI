# Help Doc 03: AI Safety Red Lines & Smart Tools

Collaborating with AI significantly boosts development efficiency, but it also introduces new challenges. To ensure project safety and stability, we have established a set of **"Safety Red Lines"** that AI developers must strictly follow, and we provide a powerful suite of smart tools to assist AI in working safely and efficiently.

---

## 1. AI Safety Red Lines

This is a set of **mandatory** behavioral guidelines. Any violation of these rules should be immediately stopped and corrected.

### **Red Line 1: Prohibition of Native File Deletion**
- AI is **strictly forbidden** from directly using any native OS delete commands, such as `rm`, `del`, `erase`, etc.
- **Mandatory**: All file deletion operations **must** be performed through our provided safe command-line tool:
  ```bash
  python .codecraft/scripts/cli.py delete <file_path>
  ```
- **Reason**: This command has a built-in "think three times" risk assessment questionnaire and a recoverable "trash can" mechanism, serving as the first line of defense against catastrophic accidental deletions.

### **Red Line 2: Prohibition of Direct Modification of Protected Files**
- This project defines a "protected paths" list in the `.codecraft/protected_paths.yml` file, which includes all core project configuration files, workflow scripts, and templates.
- AI is **strictly forbidden** from directly modifying, moving, or deleting any file on this list.
- **Mandatory**: If an AI determines that a protected file needs to be modified, it **must** halt its operation, log its intent in `project_logs/ai_interactions.md`, and explicitly request review and approval from a human developer by mentioning **`@user`**.

### **Red Line 3: Prioritization of the CLI Tool**
- **Strongly Recommended**: AI should prioritize using `cli.py` for all workflow-related operations (like starting and completing tasks) instead of manually running `git mv` or other commands.
- **Reason**: The CLI tool has built-in validation against the `workflow.yml` rules, ensuring all operations conform to the predefined project process and reducing the likelihood of errors.

---

## 2. The AI Smart Toolkit (`ai` command)

We provide AI with a powerful suite of "code quality" tools, encapsulated in the `cli.py ai` command group. AI developers should routinely use these tools to optimize the code they generate before submitting it for review.

### `ai format <file_path>`
- **Function**: Uses `black` to perform lossless, deterministic code formatting on the specified Python file.
- **When to use**: During or after coding to unify code style.

### `ai lint-fix <file_path>`
- **Function**: Uses the power of `ruff` to automatically fix all safely fixable linting errors (like unused imports, incorrect variable names, etc.).
- **When to use**: After code formatting to fix common code defects.

### `ai doctor <file_path>` (Most Recommended)
- **Function**: This is the most powerful "one-stop" code diagnostic tool. It will:
    1.  Automatically run `format` and `lint-fix`.
    2.  Run `mypy` for static type checking.
    3.  If it finds type errors that cannot be auto-fixed, it will automatically generate a structured **prompt** with full context, precisely instructing the AI on what needs to be fixed.
- **When to use**: As the final step before committing code, serving as a final quality check and self-correction mechanism.
