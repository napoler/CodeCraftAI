# Spec: [Title of Feature or Change]

- **Status**: Draft
- **Date**: YYYY-MM-DD
- **Owner**: @username
- **Related Task**: `tasks/`: [Link to the relevant task file]

---

## 1. Background

*   **Problem**: What is the problem we are trying to solve? What is the current situation?
*   **Motivation**: Why does this problem need to be solved now? What business value or technical improvement will it bring?

## 2. Goals

*   Clearly list the **specific**, **measurable** goals that this change aims to achieve.
*   Example:
    *   The average response time for the user login API should be less than 200ms.
    *   Implement a password reset feature that allows users to recover their password via email.

## 3. Non-Goals

*   Explicitly list what this change **will not** include to prevent scope creep.
*   Example:
    *   This change will not implement third-party login (e.g., Google, GitHub).
    *   This change will not include a UI for the admin backend.

## 4. Proposed Solution

*   Provide a detailed description of your technical solution.
*   This may include:
    *   **Architecture Changes**: Will new services or components be introduced?
    *   **API Design**: New or modified API endpoints, request/response formats.
    *   **Database Changes**: New table structures, field modifications, etc.
    *   **Core Logic**: Key algorithms or business logic flows.
    *   **File Changes**: Which key files do you plan to create, modify, or delete.

## 5. Alternative Solutions

*   Briefly describe other solutions you considered and why you did not choose them.

## 6. Risks and Unknowns

*   List potential risks, dependencies, or unresolved questions related to this solution.
*   Example:
    *   The delivery rate of the third-party SMS service in overseas regions is unknown.
    *   Is there a performance bottleneck in the new database query method under high concurrency?

## 7. Review Comments

*   This section is for recording important comments and decisions made by the team during the review of this spec.
