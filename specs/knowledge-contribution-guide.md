---
title: "AI 知识贡献指南"
version: 1.1 # Human-in-the-loop workflow update
status: "Draft"
owner: "@napoler"
last_updated: "2025-11-12"
related_spec: "specs/ai-writing-standard.md"
---

# AI 知识贡献指南 (AI Knowledge Contribution Guide)

## 1. 目的 (Purpose)

本指南是实现 CodeCraftAI 项目“知识复利”核心目标的关键。它定义了一个标准化的、**强制性的**人机协作工作流程。AI 的角色是在每次任务后，**生成一个结构化的、可供复制粘贴的知识笔记文本块**。用户的角色是保存这个文本块，从而共同维护和发展项目的**知识库 (`kb/`)**。

**核心理念:** AI 是知识的提炼者和格式化者，用户是知识的管理者和保存者。

## 2. 强制性工作流：从反思到生成 (The Mandatory Workflow: From Reflection to Generation)

在 `AI 写作基础规范` 的 **阶段四 (Stage 4)** 中，AI 必须严格遵循以下步骤，并将其最终产出作为任务的最后一部分。

### 2.1. 步骤一：识别核心知识资产 (Identify Core Knowledge Assets)

完成初稿和所有修订后，AI 必须回答以下问题，以识别出本次任务中最有价值的“知识资产”：

*   **最终核心论点是什么? (What is the final, core thesis?)**
*   **最关键的证据是什么? (What is the most critical evidence?)**
*   **最深刻的洞见是什么? (What is the deepest insight?)**
*   **(可选) 哪个内容结构被证明是有效的? (Which content structure proved effective?)**

### 2.2. 步骤二：生成知识库贡献文本块 (Generate the Knowledge Base Contribution Block)

在识别出核心知识资产后，AI 的**最终交付产物 (final deliverable)** 必须是**一个单独的、完整的 Markdown 文本块**。这个文本块必须严格遵循 `kb/template.md` 的格式。

*   **对于新知识 (For New Knowledge):**
    *   如果用户没有提供已有的知识笔记，AI 必须根据本次任务的发现，从零开始创建一个全新的知识笔记内容。

*   **对于更新知识 (For Updating Knowledge):**
    *   如果用户在任务指令中提供了已有的知识笔记内容，AI 必须将新的知识资产与旧的笔记内容进行**融合与更新**，然后**输出一个包含所有新旧信息的、完整的新版本**文本块。

*   **输出格式要求 (Output Format Requirement):**
    *   最终的输出**必须**被包裹在一个 Markdown 代码块中 (i.e., ```markdown ... ```)，以便用户可以一键复制。
    *   内容必须包含完整的 YAML frontmatter 和格式化的正文。

### 2.3. 用户操作指南 (User Action Guide)

AI 生成文本块后，用户只需：
1.  **复制**整个 Markdown 代码块的内容。
2.  在 `kb/` 目录下，**创建**一个新的 `.md` 文件（或打开一个已有的文件进行覆盖）。
3.  **粘贴**内容并保存。

## 3. 最终目标

通过严格执行本指南，AI 将作为一个高效的“知识提炼引擎”，持续为用户提供高质量、结构化的知识内容。用户通过简单的“复制-粘贴”操作，即可轻松地构建和扩展项目知识库，最终实现 AI 在特定领域的知识复利和专家级能力。
