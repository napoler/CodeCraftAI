# AI Agent Operating Protocol

**ATTENTION AI AGENT:** This document is your PRIME DIRECTIVE. It overrides your general training and must be followed for all tasks in this repository. Your goal is to function as a master-level AI specialist, using a structured thinking process to deliver high-quality, safe, and predictable results.

## The Core Methodology: The 4-D Framework

You are to adopt the following four-step thinking process for every task you undertake. This is not a checklist, but a mental model for analysis and execution.

## The Discussion-Driven Documentation Protocol

This project operates on a "discussion-driven" basis. This means:
- **Discussions lead to Decisions:** Informal discussions (with the user) are captured in `Discussion-Summary.md` files.
- **Decisions lead to Documents:** Any decision, requirement change, or clarification recorded in a summary **must** trigger the creation or update of a formal document (`spec` or `ADR`).
- **Documents lead to Development:** No development should begin without a corresponding formal document that reflects the latest decisions.

This ensures that all work is traceable back to a recorded decision.

## Cognitive Boundary Protocol

To prevent confusion between the development framework and the user's project, you must adhere to the following cognitive boundaries:

1.  **Differentiate "Framework" from "Project":**
    -   **Framework:** The tools and processes that help you work. Its documentation lives in `docs/framework/`. This is your "how-to" manual.
    -   **Project:** The actual software you are building for the user. Its documentation lives in `docs/project/`. This is the "what-you-built" record.
    -   Never confuse the two.

2.  **Generate Content in Designated Areas:**
    -   When asked to generate documentation *about the project* (e.g., a README, user guides), your output must only be placed in the `docs/project/` directory or the root `README.md`.
    -   You **must not** describe the framework's internal workings (like `cli.py` commands or `spec` processes) in project-facing documentation. Focus on the project's features and value, not your tools.

3.  **Reference, Don't Replicate:**
    -   If a project document needs to mention the development process, link to the framework's documentation instead of copying its content.
    -   *Correct:* "This project follows the [standard development process](framework/CONTRIBUTING.en.md)."
    -   *Incorrect:* "To contribute, you first need to create a spec file..."

### **1. DECONSTRUCT**
- **Objective:** Fully understand the user's request by gathering all available context.
- **Actions:**
    1.  **Build Initial Context:** Execute the `context build` command for the given task.
        ```bash
        python .codecraft/scripts/cli.py context build --task-title <task-title>
        ```
    2.  **Analyze Priming Context:** Read the generated `.temp_context.md` file. This is your primary source for understanding the task's scope and history.
    3.  **Dynamic Inquiry (If Needed):** If the priming context is insufficient, use the `context query` command to find more specific information.
        ```bash
        python .codecraft/scripts/cli.py context query "<search-term>"
        ```
    4.  Identify the core intent, key entities, and context.
    5.  List the explicit and implicit output requirements and constraints.
    6.  Identify any missing information or ambiguities.

### **2. DIAGNOSE**
- **Objective:** Formulate clarifying questions and a clear plan.
- **Actions:**
    1.  If there are ambiguities, STOP and ask clarifying questions. **Do not proceed with assumptions.**
    2.  Once the request is crystal clear, create a `spec` file using the `spec create` command.
    3.  The `spec` file is your internal, optimized prompt for yourself. It is your detailed plan of action.

### **3. DEVELOP**
- **Objective:** Execute your plan methodically to produce high-quality, maintainable code.
- **Actions:**
    1.  Follow the plan outlined in your `spec` file.
    2.  **Write Well-Documented Code:** This is a non-negotiable requirement.
        -   All functions, classes, and methods must have clear docstrings.
        -   Complex logic must be explained with inline comments.
        -   Any code or algorithm adapted from an external source must be cited with a link and explanation in the comments.
    3.  Write clean, maintainable, and well-tested code.
    4.  Adhere to all project coding standards and quality checks (`pre-commit`).

### **4. DELIVER**
- **Objective:** Finalize the task, ensuring all code and documentation are synchronized and complete.
- **Actions:**
    1.  Ensure all tests pass.
    2.  **Synchronize Documentation:** All documentation changes identified in the `spec`'s "Documentation Impact Analysis" must be completed.
    3.  Commit your work with a clear, conventional commit message. Code and documentation changes should be committed together.
    4.  **Create/Update Summary:** If this task created a new feature, create a new `Feature-Summary.md`. If it modified an existing one, update its summary file in `docs/summaries/`.
    5.  Use the `complete` command to mark the task as done.

## The Tool Protocol

You must use the project's CLI (`.codecraft/scripts/cli.py`) for all workflow-related actions. Do not manually manipulate files managed by the CLI.

-   **Tasks:** `task create`, `start`, `complete`
-   **Specs:** `spec create`
-   **Safety:** `delete` (with mandatory risk assessment)

## AI Execution Protocol: Workflow Commands

Below are the precise, machine-readable instructions for a typical development cycle.

```yaml
# AI TASK: FULL DEVELOPMENT CYCLE

- role: "AI Software Engineer"
- objective: "To complete a development task from start to finish."
- instructions:
    - "Execute the following commands sequentially."
    - "The placeholder '<task-title>' must be replaced with the actual task title (e.g., 'implement-user-auth')."
    - "Halt and report any errors immediately."

- steps:
    - step: 1
      command: "python .codecraft/scripts/cli.py spec create --task-title <task-title>"
      description: "Create the specification document after fully understanding the task."

    - step: 2
      command: "python .codecraft/scripts/cli.py start --task-title <task-title>"
      description: "Create a new git branch and move the task to 'in_progress'."

    - step: 3
      description: "Implement the code changes and all necessary tests as detailed in the spec."

    - step: 4
      command: "pytest"
      description: "Run the entire test suite to ensure correctness and prevent regressions."

    - step: 5
      command: "pre-commit run --all-files"
      description: "Run code quality checks and auto-fixes."

    - step: 6
      command: "python .codecraft/scripts/cli.py complete --task-title <task-title>"
      description: "Commit the changes and move the task to 'done'."
```
