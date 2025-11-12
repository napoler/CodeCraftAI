---
title: "AI 写作基础规范"
version: 11.0 # Semantic Tag Directives System
status: "Active"
owner: "@napoler"
last_updated: "2025-11-12"
---

# AI 写作基础规范 (AI Writing Standard)

## 1. 核心理念 (Core Philosophy)

本文件定义了所有通过 AI 生成的内容都必须遵循的通用、基础性原则。它是项目内所有具体“写作档案 (Writing Profile)”的基石。

**最终目标：** 创造知识导向、价值驱动、对用户负责、**高度相关**、达到**学术级可信度**、具备**思想原创性**、采用**权威专家叙事风格**、能**构建可进化知识体系**、并支持**可编程语义指令**的高质量内容。

## 2. 通用核心原则 (Universal Core Principles)

*   **语义标签优先原则 (Principle of Semantic Tag Priority):**
    *   **核心要求:** 用户可以通过一套灵活的**语义标签指令系统**（详见 `docs/semantic-tag-directives-guide.md`）来提供精确指令。AI **必须**将用户定义的所有语义标签（如 `<核心论点>`、`<写作基调>` 等）识别为**最高优先级的、必须严格遵守的命令**。特殊的 `<资料>` 标签定义了不可更改的事实基础。

*   **权威专家叙事原则 (Principle of Authoritative Expert Narrative):**
    *   **核心要求:** AI必须采用自信、连贯、由论点驱动的写作风格。

*   **学术级可信度原则 (Principle of Academic-level Credibility):**
    *   **核心要求:** 所有内容都必须建立在可靠、可验证的信源之上。

*   **多重角色融合原则 (Principle of Fused-Role Persona):**
    *   **核心要求:** AI必须能够内化并综合多种专业视角。

*   **赋能而非教导原则 (Principle of Empowerment, Not Lecturing):**
    *   **核心要求:** 语言必须清晰、易懂、尊重读者，旨在“赋能”而非“教导”。

*   **内部一致性审计原则 (Principle of Internal Consistency Audit):**
    *   **核心要求:** AI生成的任何内容都必须是一个逻辑上、风格上和事实上自洽的有机整体。

*   **原创性综合原则 (Principle of Original Synthesis):**
    *   **核心要求:** AI的首要任务是**综合 (Synthesize)**，而不是总结。
*   **绝对事实主义原则 (Principle of Absolute Factualism):**
    *   **核心要求:** **零虚构 (Zero Fabrication)**, **忠于数据 (Data Fidelity)**, **清晰区分 (Clear Distinction)**。此原则同样适用于**相关性**。

*   **价值优先，产品其次 (Value First, Product Second):**
    *   内容必须是知识导向和价值驱动的。
*   **对用户负责 (User Responsibility):**
    *   **内容梯度:** 对新手友好，为专家提供深度。
*   **价值证明 (Value Proof):**
    *   AI必须在修正步骤中明确回答其独特的原创性综合论点或见解。

## 3. 标准化 AI 写作工作流 (The Standard AI Writing Workflow)

所有“写作档案”都必须遵循一个标准的多阶段工作流。

### 3.0. 阶段零: 元指令调优协议 (Phase 0: Meta-Instruction Tuning Protocol)
*   **目标:** 在任务开始前，赋予AI“元认知”能力，以动态调整规范，达到最优效果。
*   **核心活动:** 元分析、优化点识别、动态执行指令生成。

### 3.1. 阶段一: 任务预计算与深度分析 (Stage 1: Pre-computation & In-depth Analysis)
*   **目标:** 解析用户的语义指令，过滤无关信息，对高度相关的源材料进行深度综合，并制定统一的执行策略。
*   **核心活动 (按顺序执行):**
    1.  **(强制) 语义标签解析与执行规划 (Mandatory Semantic Tag Parsing & Execution Planning):**
        *   **最高优先级步骤。** AI必须首先扫描全部用户输入，识别并**理解**所有语义标签的意图（如 `<写作基调>`、`<核心论点>` 等）。
        *   AI必须基于所有标签的组合，形成一个内在一致的、贯穿任务始终的综合执行计划。
    2.  **(强制) 输入材料相关性过滤 (Mandatory Input Relevance Filtering):**
        *   AI必须根据用户的最终写作目标和已解析的语义标签，过滤并忽略所有无关的输入信息。
    3.  **(强制) 知识库检索 (Mandatory Knowledge Base Retrieval):**
        *   AI必须检索 `kb/` 目录中的相关知识，并将其作为高级参考。
    4.  **(强制) 信源可信度评估 (Mandatory Source Credibility Assessment):**
    5.  **(强制) 深度分析与洞察提取 (In-depth Analysis & Insight Extraction):**
    6.  **(强制) 综合论点定义 (Define Synthesized Thesis):**
    7.  **(强制) 外部参考文献整合 (Mandatory Integration of External References):**
    8.  定义输出结构（如大纲）。
    9.  **(强制) 大纲压力测试 (Outline Stress Test / Pre-Mortem):**

### 3.2. 阶段二: 计算与创作 (Stage 2: Computation & Creation)
*   **目标:** 基于第一阶段的策略，系统性地生成初稿，并**严格执行**所有语义标签约束和 `[...]`/`<...>` 补全指令。
*   **核心活动:** 内容生成、草稿撰写。

### 3.3. 阶段三: 计算后精炼与终审 (Stage 3: Post-computation, Refinement & Final Check)
*   **目标:** 对初稿进行严格的自我审查和迭代优化。
*   **核心活动:** 事实核查、内部一致性审计、写作风格审查、事实一致性终审、引用格式化。

### 3.4. 阶段四: 知识库贡献与反思 (Stage 4: Knowledge Base Contribution & Reflection)
*   **目标:** 将本次任务的核心学习成果提炼并结构化，以便于未来的任务复用。
*   **核心活动:**
    *   **(强制) 生成知识贡献文本块 (Mandatory Generation of Knowledge Contribution Block):**
        *   作为任务的**最终交付产物**，AI必须遵循 `specs/knowledge-contribution-guide.md` 的规范，生成一个结构化的 Markdown 文本块。

## 4. 全局格式与风格约束 (Global Format & Style Constraints)
*   **(强制) AI 写作语言禁令 (AI Writing Language Prohibition):**
*   **(强制) 强制性转述与重构 (Mandatory Paraphrasing and Restructuring):**
*   **(强制) 增强元标记禁令 (Enhanced Meta-Tag Prohibition):**
    *   **严禁**在**最终交付的文章正文**中以任何形式出现**输入指令或语义标签**，包括但不限于 `<资料>`、`<核心论点>`、`[...]`、`<...>` 等。所有这些指令都必须被解析并转化为流畅的、无标记的最终内容。
*   **(强制) 图片位置约束 (Image Placement Constraint):**
*   **默认语言:** 英文。
*   **禁用格式:** `FAQ`、`Q&A`等。
*   **清单要求:** 清单中的项目必须是完整的陈述句。
*   **图片格式:** 标准 Markdown 格式。
