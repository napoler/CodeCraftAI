# Task: [Enter a concise title for the task here]

- **Summary**: "[A one-sentence summary of the task's goal]"
- **Status**: Backlog
- **Type**: Feature | Bug | Chore
- **Priority**: Medium | High | Critical
- **Author**: @username
- **Date**: YYYY-MM-DD
- **Dependencies**: `[e.g., #001, #002]`

---

### 1. Goal (What is the desired outcome?)

*Please provide a clear and concise description of what needs to be accomplished. What does success look like?*

> **Example:** "Implement a password reset feature that allows users to reset their password via a secure email link."

### 2. Context (Why is this task necessary?)

*Provide any relevant background information. Why is this change needed now? What problem does it solve?*

> **Example:** "Currently, users who forget their password have to contact support manually, which is inefficient. This feature will improve user experience and reduce support load."

### 3. Requirements & Constraints (What are the specific rules?)

*List any specific requirements, business rules, or technical constraints.*

- **Must-haves:**
  - *e.g., The reset link must expire in 1 hour.*
  - *e.g., The new password must meet the project's security policy.*
- **Nice-to-haves:**
  - *e.g., Send a confirmation email after the password has been successfully changed.*
- **Constraints:**
  - *e.g., Must use the existing SendGrid email service.*
  - *e.g., The solution should not require any database schema changes.*

### 4. Acceptance Criteria (How do we know it's done?)

*Provide a checklist of observable outcomes that will prove the task is complete.*

- [ ] User can request a password reset from the login page.
- [ ] User receives an email with a unique, single-use reset link.
- [ ] Clicking the link takes the user to a page to enter a new password.
- [ ] The user can successfully log in with the new password.
- [ ] The old reset link is invalidated after use.

### 5. Related Logs (Links to discussion summaries)

*Link to any relevant discussion summaries in `project_logs/` that provide context for this task.*

- `[e.g., ../project_logs/2023-11-03_discussion_on_password_reset.md]`
