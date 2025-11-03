# 安装与升级指南

本文档提供基于 CodeCraft 模板设置和维护项目的说明。

## 1. 初始项目设置

请按照以下步骤首次运行您的项目。

### 先决条件

- Git
- Python 3.8+
- `pip` 和 `venv` (通常随 Python 一同安装)

### 安装步骤

1.  **克隆仓库:**
    首先，将项目模板克隆到您的本地计算机。

    ```bash
    git clone [您的新仓库URL]
    cd [您的仓库名称]
    ```

2.  **创建虚拟环境:**
    强烈建议使用虚拟环境来管理项目依赖。

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    # 在 Windows 上，请使用: venv\Scripts\activate
    ```

3.  **安装依赖:**
    本项目使用 `pip-tools` 管理依赖。`requirements.txt` 文件包含了应用程序所需的固定版本的依赖。

    ```bash
    pip install -r requirements.txt
    ```

4.  **初始化 Pre-commit 钩子:**
    仓库包含了用于确保代码质量的 pre-commit 钩子。通过运行以下命令来安装它们：
    ```bash
    pre-commit install
    ```

5.  **验证安装:**
    检查 CLI 工具是否正常工作。

    ```bash
    python cli.py --help
    ```

    您应该能看到命令行界面的帮助菜单。至此，您的项目已成功设置！

## 2. 框架升级

本项目模板会不断演进。当新的功能、错误修复和最佳实践被添加到原始 CodeCraft 模板时，您可能希望将它们整合到您的项目中。

推荐的方法是将原始模板仓库添加为一个名为 `upstream` 的远程仓库。

### 升级步骤

1.  **将模板添加为 `upstream` 远程仓库:**
    此操作只需执行一次。

    ```bash
    # 请将 URL 替换为原始 CodeCraft 模板仓库的 URL
    git remote add upstream https://github.com/original/codecraft-template.git
    ```

2.  **从 `upstream` 获取更新:**
    定期从模板仓库获取最新的变更。

    ```bash
    git fetch upstream
    ```

3.  **将更新合并到您的项目中:**
    将 `upstream/main` 分支的变更合并到您项目的 `main` 分支。

    ```bash
    # 确保您在自己的 main 分支上，并已提交所有本地变更
    git checkout main
    git merge upstream/main --allow-unrelated-histories
    ```

    - 第一次合并时可能需要 `--allow-unrelated-histories` 标志。
    - Git 会尝试自动合并变更。如果存在冲突（例如，您修改了模板也更新了的同一个文件），您需要手动解决它们。

4.  **审查与测试:**
    成功合并后，请彻底测试您的应用程序，确保更新没有引入任何破坏性变更。如果 `requirements.txt` 文件有变动，请更新您的依赖。

    ```bash
    pip install -r requirements.txt
    ```

## 3. 问题排查

- **`command not found: pre-commit`**: 这意味着 pre-commit 包未正确安装。请确保您的虚拟环境已激活，并运行 `pip install pre-commit`。
- **升级过程中的合并冲突**: 如果您自定义了核心模板文件，这是正常现象。请在您的代码编辑器中仔细审查冲突，选择正确的版本（您的、模板的或两者的结合），然后提交解决后的文件。
