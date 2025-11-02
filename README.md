# CodeCraftAI
Develop an AI-assisted programming tool that automates code generation, optimizes existing code, and provides real-time debugging suggestions, aiming to improve developers' coding efficiency while ensuring code quality and maintainability.

---

## 快速使用指南 (Quick Start)

本节将指导你如何将我们的 **规范驱动开发 (Spec-Driven Development)** 流程快速集成到你的项目中。请根据你的工具和偏好选择最适合你的方式。

### 方式一：AI 快速启动 (推荐)

**适用场景**: 你的AI编程助手支持直接从Git仓库克隆项目。这是启动一个**新项目**的最快方式。

**提示词**:
```
任务：为我启动一个新项目，并使用 CodeCraftAI 的开发规范作为模板。

请执行以下操作：
1. 从 GitHub 克隆项目 `https://github.com/napoler/CodeCraftAI.git` 到我的本地开发环境。
2. 克隆完成后，请删除 `.git` 目录，以便我初始化自己的新 Git 仓库。
3. 告诉我操作完成。
```

**提示词解析**:
*   **直接高效**: 该指令利用了AI助手的网络和文件系统能力，直接拉取一个完整的、经过验证的模板，避免了手动创建文件或逐一生成内容的繁琐过程。
*   **最佳实践**: 指令中包含了“删除`.git`目录”的步骤，这是一个关键的最佳实践，确保新项目从一个干净的版本历史开始，而不是继承模板仓库的历史。

### 方式二：手动设置

**适用场景**: 你是习惯于自己动手操作的开发者。

#### **情况 A: 用于一个全新的项目**

1.  **克隆仓库**:
    ```bash
    git clone https://github.com/napoler/CodeCraftAI.git new-project-name
    ```
2.  **进入目录并重置Git历史**:
    ```bash
    cd new-project-name
    rm -rf .git
    git init
    ```
3.  **开始你的项目**: 你现在拥有了一个包含我们规范流程的干净项目起点。

#### **情况 B: 用于一个现有的项目**

1.  **复制 `specs` 目录**: 从本仓库中，只将 `specs` 整个目录复制到你现有项目的根目录下。
2.  **开始使用**:
    *   当需要开发新功能时，请参考 `specs/README.md` 中的流程说明。
    *   复制 `specs/template.md` 来创建你的第一份规范。

### 方式三：备选 AI 设置 (手动生成)

**适用场景**: 你的AI编程助手**不支持**直接操作Git仓库或访问网络，或者你希望对生成过程有更细致的控制。

**提示词**:
```
任务：在我的项目中初始化“规范驱动开发”流程。

上下文：我希望在当前项目中引入规范驱动开发（Spec-Driven Development）的最佳实践。请为我创建所需的文件结构和模板。

请执行以下操作：
1.  在项目根目录下创建一个名为 `specs` 的文件夹。
2.  在 `specs` 文件夹内，创建一个 `README.md` 文件，用于向团队解释规范驱动的流程、目的和生命周期（草案 -> 评审 -> 批准 -> 实现 -> 完成）。
3.  同样在 `specs` 文件夹内，创建一个名为 `template.md` 的规范模板文件。这个模板需要包含以下几个核心部分，并为每个部分提供引导性的注释或问题：
    - 规范名称、状态、负责人等元数据
    - 目标 (Goals)
    - 背景 (Background)
    - 设计方案 (Proposed Solution)
    - 备选方案 (Alternatives Considered)
    - 测试计划 (Test Plan)

请确保生成的文件内容是专业、清晰且随时可用的。
```
