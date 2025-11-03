# Help Doc 02: Core Concepts & Directory Structure

The core design philosophy of this project is **"Project-as-Code, Code-as-Documentation."** We consolidate all aspects of project management, design, and communication—traditionally scattered across different tools—into the Git repository, managing them as code and Markdown files.

The benefits are clear: a **Single Source of Truth**, **complete transparency**, **version traceability**, and extreme friendliness to automation and AI.

Here are the five core user directories you need to know:

---

### 1. `tasks/` - Your Task Board

This directory is your "To-Do" list or Kanban board. We update task status by moving files.

- **`backlog/`**: The starting point for all new tasks.
- **`todo/`**: Tasks the team has planned and is ready to start.
- **`in_progress/`**: Tasks that you or an AI are currently working on.
- **`done/`**: Tasks that have been developed and merged into the main branch.

**Workflow**: `backlog` -> `todo` -> `in_progress` -> `done`
**Core Tool**: `python .codecraft/scripts/cli.py task`

---

### 2. `specs/` - Your Design Blueprints

This is the heart of "Spec-Driven Development." Before writing any significant code, you should create a spec file here.

- **`template.en.md`**: The template for creating new specs.
- **`[your-feature-name].md`**: The design document for a specific feature.

**Workflow**:
1.  Create a new spec by copying from `template.en.md`.
2.  Detail the design proposal.
3.  Have it reviewed by the team or an AI.
4.  Begin coding only after the spec is approved.

---

### 3. `project_docs/` - Your Project Knowledge Base

This directory belongs entirely to you and your project. All project-related documentation that is **not a spec or a task** should go here. Future template updates will never touch this directory.

- **`help/`**: This help center.
- **`[your-mind-map].md`**: Mind maps you design for features.
- **`[your-architecture-diagram].png`**: Architecture diagrams you create.

---

### 4. `project_logs/` - Your Project Memory

This directory is the project's "memory crystal," used to record crucial but ephemeral communication and decision-making processes.

- **`ai_interactions.md`**: Log key conversations, instructions, and corrections with your AI.
- **`team_discussions.md`**: Record key conclusions from team meetings.
- **`issue_investigations/`**: Store in-depth analysis reports for complex bugs.

---

### 5. `.trash/` - Your Safety Net

This is a version-control-ignored "trash can." All files deleted via `cli.py delete` are safely moved here, providing you with a layer of protection against accidental deletion.

**Core Tools**:
- `python .codecraft/scripts/cli.py delete`
- `python .codecraft/scripts/cli.py trash`

Understanding and using these directories will allow you to experience the full power of this workflow.
