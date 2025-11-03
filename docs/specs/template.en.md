# Specification: [Feature or Change Title]

- **Summary**: "[A one-sentence summary of the proposed solution]"
- **Status**: Draft
- **Author**: @username | AI Agent
- **Associated Task**: `tasks/...`
- **Related Logs**: `[Link to relevant discussion logs]`

---

## Part 1: Prompt Analysis (Deconstruct & Diagnose)

> *AI Agent: This section is your mandatory thinking process. Answer these questions before writing any code.*

### 1. Core Request Deconstruction
- **What is the fundamental goal of this task?**
  - *[Analyze the user's request and state the core objective in one sentence.]*
- **Who are the users or systems involved?**
  - *[List the key actors.]*
- **What are the explicit requirements and constraints?**
  - *[List all stated deliverables, technical constraints, performance requirements, etc.]*

### 2. Diagnosis of Ambiguities
- **What information is missing or unclear?**
  - *[Identify gaps in the request. e.g., "The error handling behavior for invalid input is not specified."]*
- **What assumptions am I making?**
  - *[List any assumptions you are making to proceed. These must be validated if significant.]*
- **Clarifying Questions (if any):**
  - *[If ambiguities cannot be resolved with safe assumptions, list the questions you need answered before development.]*

---

## Part 2: Implementation Plan (Develop)

> *AI Agent: This is your optimized prompt for yourself. Detail your plan of action.*

### 1. Role Assignment
- **My Role:** I will act as a `[e.g., Senior Python Developer, API Design Specialist]` to ensure best practices in `[e.g., code structure, API design]`.

### 2. Proposed Solution
- **High-Level Strategy:**
  - *[Describe your overall approach. e.g., "Create a new service class to handle business logic, add a new endpoint in the controller, and define a new DTO for the request body."]*
- **File Changes:**
  - **Create:**
    - `[List new files to be created]`
  - **Modify:**
    - `[List existing files to be modified]`
  - **Delete:**
    - `[List files to be deleted, with justification]`
- **Key Logic / Algorithm:**
  - *[Describe any complex logic, data transformations, or algorithms in pseudocode or a step-by-step list.]*
- **API Design (if applicable):**
  - **Endpoint:** `[e.g., POST /api/users]`
  - **Request Body:** `[JSON structure]`
  - **Success Response (200 OK):** `[JSON structure]`
  - **Error Responses:** `[e.g., 400 Bad Request, 404 Not Found]`

### 3. Testing Strategy
- **Unit Tests:**
  - *[Describe the unit tests needed. e.g., "Test the `calculate_discount` method with valid, invalid, and edge-case inputs."]*
- **Integration Tests:**
  - *[Describe any integration tests. e.g., "Test the full API endpoint from request to database interaction."]*

### 4. Code-level Documentation & Citations
- **Docstrings:**
  - *[Outline the plan for documenting new classes and methods. e.g., "All public methods in the `UserService` will have full docstrings explaining their purpose, parameters, and return values."]*
- **Citations:**
  - *[If using code or ideas from external sources, list them here. e.g., "The token generation logic is based on the algorithm described in [link to article]."]*

### 5. Documentation Impact Analysis
- **Documents to Create:**
  - `[List any new user guides, tutorials, or project-level READMEs that need to be created. e.g., "docs/project/guides/new-api-usage.md"]`
- **Documents to Update:**
  - `[List existing documents that will need to be updated. e.g., "README.md", "docs/framework/INSTALL.md"]`

---

## Part 3: Output Specification (Deliver)

> *AI Agent: This defines the final, expected state.*

- **Definition of Done:**
  - [ ] All code implemented as per the plan.
  - [ ] All new and existing tests pass.
  - [ ] Code quality checks (linting, formatting) pass.
  - [ ] The associated task is moved to the `done` state.
- **Risks and Unknowns:**
  - *[List any potential risks or dependencies, e.g., "This change depends on an external API that has a low rate limit."]*
