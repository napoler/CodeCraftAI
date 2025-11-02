# CodeCraftAI
Develop an AI-assisted programming tool that automates code generation, optimizes existing code, and provides real-time debugging suggestions, aiming to improve developers' coding efficiency while ensuring code quality and maintainability.

---

## 开发环境设置 (Development Setup)

在开始编码之前，请遵循以下步骤设置你的本地开发环境。这将确保你拥有所有必需的工具，并能遵循项目的代码质量标准。

1.  **创建并激活虚拟环境**

    我们推荐使用 Python 的 `venv` 模块来创建一个独立的开发环境。

    ```bash
    # 在项目根目录创建一个名为 .venv 的虚拟环境
    python -m venv .venv

    # 激活虚拟环境 (Linux/macOS)
    source .venv/bin/activate

    # 激活虚拟环境 (Windows)
    # .\.venv\Scripts\activate
    ```

2.  **安装项目依赖**

    本项目使用 `pyproject.toml` 来管理依赖。使用以下命令安装所有核心依赖和开发工具（如 `pytest`, `black`, `ruff`）。

    ```bash
    # 确保你的 pip 是最新版本
    pip install --upgrade pip

    # 安装项目为可编辑模式，并包含 [dev] 依赖
    pip install -e .[dev]
    ```
    *   **说明**: `-e` 选项（editable）会将项目以“可编辑”模式安装，这意味着你对代码的修改会立即生效，无需重新安装。`[dev]` 则表示同时安装我们在 `pyproject.toml` 中定义的开发依赖。

3.  **激活 Git Hooks**

    我们使用 `pre-commit` 框架在代码提交前自动运行代码格式化和检查。这可以极大地保证代码库的整洁和一致。

    ```bash
    # 在你的虚拟环境中安装 git hooks
    pre-commit install
    ```
    现在，每当你尝试 `git commit` 时，`black` 和 `ruff` 都会自动运行。如果它们对你的文件进行了修改，或者发现了错误，提交将会被中止，你需要重新暂存（`git add`）修改后的文件，然后再次提交。

至此，你的开发环境已准备就绪！

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
