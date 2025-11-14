# SpecKit-Flow 工作流规约

本规约详细定义了在 `CodeCraftAI` 项目中，一个 **SpecKit 规约** 从概念到完成所必须遵循的端到端流程。所有参与者（包括 AI 代理和人类开发者）都必须严格遵守此工作流。

## SpecKit 规约的生命周期

一个标准的 SpecKit 规约生命周期包括五个核心阶段，该流程由 OpenSpec 提供支持：

1.  **Phase 1: 提案 (Proposal)** - 初始化 SpecKit 规约
2.  **Phase 2: 审查与完善 (Review & Refine)** - 达成规约共识
3.  **Phase 3: 实施 (Implementation)** - 将规约转化为代码
4.  **Phase 4: 验证 (Verification)** - 确保代码质量与规约一致
5.  **Phase 5: 归档 (Archive)** - 将规约沉淀为知识

---

### Phase 1: 提案 (Proposal)

**目标：** 基于高级指令，由 AI 代理完成一份详尽的、SpecKit 风格的规约草案。

**流程：**

1.  **创建变更流程：**
    - 在 `openspec/changes/` 目录下创建一个新的子目录，例如 `feat/user-authentication`。这代表一个由 OpenSpec 管理的流程实例。

2.  **初始化 SpecKit 规约：**
    - 在新目录下，复制 `openspec/template.md` 并重命名为 `spec.md`。这标志着一份新的 **SpecKit 规约** 的诞生。

3.  **AI 撰写规约草案：**
    - AI 代理 (Jules) 的核心责任是：将高级指令转化为一份深度结构化的 `spec.md` 草案，填满其所有部分。
    - 此时，规约的 `状态` 应为 `草稿`。

---

### Phase 2: 审查与完善 (Review & Refine)

**目标：** 人类与 AI 对 SpecKit 规约的内容达成完全共识。

**流程：**

1.  **迭代审查：**
    - 人类开发者审查 `spec.md` 草案，确保其深度和准确性。
    - AI 代理根据反馈更新规约，直至达成共识。**这是 SpecKit 的核心价值所在，在规约批准前，绝不编写任何代码。**

2.  **规约批准：**
    - 人类开发者将规约的 `状态` 修改为 `已批准`。

3.  **生成任务列表 (`tasks.md`)：**
    - 规约一经批准，AI 代理便基于 `spec.md` 中的“实施计划”生成 `tasks.md`，将深度设计转化为可执行的步骤。

---

### Phase 3: 实施 (Implementation)

**目标：** AI 代理严格按照 SpecKit 规约和 `tasks.md` 完成高质量的编码。

**流程：**

1.  **规约驱动开发：**
    - AI 代理必须严格按照 `tasks.md` 的顺序执行，该任务列表是 `spec.md` 的直接产物。
    - 流程强制遵循 **测试驱动开发 (TDD)**。

2.  **标记任务进度：**
    - AI 代理在 `tasks.md` 中实时更新任务完成状态。

---

### Phase 4: 验证 (Verification)

**目标：** 确保最终实现与 SpecKit 规约完全一致。

**流程：**

1.  **自动化检查：**
    - AI 代理运行所有测试和质量检查工具。

2.  **规约符合性验证：**
    - AI 代理必须回顾 `spec.md` 的“完成的定义”部分，逐项确认最终产出物与规约要求完全相符。

---

### Phase 5: 归档 (Archive)

**目标：** 将已完成的 SpecKit 规约沉淀为项目的永久知识资产。

**流程：**

1.  **执行归档：**
    - 整个变更目录从 `openspec/changes/` 移动到 `openspec/archive/`。
    - **知识沉淀：** 如果规约引入了对系统核心设计的变更，其内容摘要必须被更新到 `openspec/specs/` 目录下的“真理之源”中。

2.  **完成：**
    - SpecKit 规约的生命周期结束。

## 异步 AI 工作流特别说明

对于长耗时任务，AI 代理 **Jules** 将采用非阻塞模式工作，确保 SpecKit-Flow 的流程始终保持敏捷。
