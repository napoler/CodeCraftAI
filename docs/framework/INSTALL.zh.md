# 安装与集成指南

本指南提供为全新项目和现有项目设置本框架的说明。其核心原则是 **非入侵式**；本框架旨在增强而非破坏您现有的代码库。

## 第 1 部分：用于全新项目

这是最直接的方法。

1.  **克隆仓库：**
    将此仓库克隆到您的本地机器，以其为起点。
    ```bash
    git clone [本框架仓库的URL] 您的新项目名称
    cd 您的新项目名称
    ```
2.  **初始化您自己的 Git 历史：**
    最佳实践是移除框架的 git 历史，开始您自己的历史记录。
    ```bash
    rm -rf .git
    git init
    git add .
    git commit -m "从 CodeCraft 框架初始化项目"
    ```
3.  **运行环境设置：**
    按照标准流程设置您的 Python 环境。
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    # 在 Windows 上: venv\Scripts\activate
    pip install -r requirements.txt
    pre-commit install
    ```
    您的新项目现已准备就绪。

## 第 2 部分：用于现有项目 (非入侵式集成)

此过程被设计为完全安全和可逆的。它 **永远不会** 覆盖您现有的文件。

1.  **将框架添加为远程仓库：**
    在您现有项目的根目录中，将框架仓库添加为一个名为 `upstream-framework` 的远程仓库。
    ```bash
    git remote add upstream-framework [本框架仓库的URL]
    ```
2.  **获取框架文件：**
    将框架的文件获取到您的本地仓库中。
    ```bash
    git fetch upstream-framework
    ```
3.  **安全地注入框架文件：**
    将框架的 `main` 分支检出到一个临时分支中。这使您可以在没有复杂合并的情况下复制必要的文件。
    ```bash
    git checkout -b temp-framework-branch upstream-framework/main
    ```
4.  **运行安全的 `init` 命令：**
    本框架包含一个安全的初始化脚本。请回到您项目的主分支并运行它。
    ```bash
    git checkout main
    python .codecraft/scripts/cli.py init
    ```
    `init` 命令将会：
    -   如果核心目录（如 `.codecraft/`, `docs/`, `tasks/`）不存在，则安全地创建它们。
    -   复制模板文件。
    -   对于像 `.gitignore` 或 `pyproject.toml` 这样的关键文件，如果它们在您的项目中已存在，该命令会创建一个带 `.template` 后缀的版本（例如 `.gitignore.template`），而不是覆盖。然后它会指导您手动比较和合并内容。

5.  **清理：**
    您现在可以删除临时分支。
    ```bash
    git branch -D temp-framework-branch
    ```

## 第 3 部分：AI 代理执行协议 (安装)

**目标：** 在现有项目中安装并初始化 CodeCraft 环境。

**指令：** 你是一个软件开发 AI。请按顺序执行以下步骤。如果遇到任何错误，请立即停止并报告。在运行 `init` 命令之前，你必须请求用户确认。

```yaml
- role: "AI 软件工程师"
- task: "安全集成 CodeCraft 框架"
- steps:
    - step: 1
      command: "git remote add upstream-framework [本框架仓库的URL]"
      description: "将框架添加为远程仓库。"
    - step: 2
      command: "git fetch upstream-framework"
      description: "获取框架的文件。"
    - step: 3
      command: "ls -a"
      description: "预检。列出现有文件以识别潜在冲突。"
    - step: 4
      action: "request_user_confirmation"
      prompt: "我已列出项目文件。下一步将运行 `init` 命令，它会安全地创建新目录和文件，不会覆盖现有文件，但会为待合并文件创建 `.template` 版本。您是否批准继续？"
    - step: 5
      command: "python .codecraft/scripts/cli.py init"
      description: "运行安全的初始化脚本。"
      precondition: "用户必须已批准上一步。"
```
