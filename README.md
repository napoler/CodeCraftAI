# CodeCraftAI: AI驱动的开发规范与项目模板

> **【模板文件 - 请勿直接修改】**
>
> 本文件是 CodeCraftAI 核心模板的一部分。为了方便未来无冲突地升级模板，请**不要**直接修改本文件。
>
> 如果你需要添加你自己的项目介绍或文档，请在 `project_docs/` 目录下创建新的 Markdown 文件。

本项目是一个功能完备、遵循行业最佳实践的项目模板，旨在帮助开发者和团队快速启动一个规范化、高质量的AI工程项目。其核心特性是**内置了一套强大的命令行工具 (`cli.py`)**，将复杂的开发规范自动化、简单化。

> **模板的生命周期**: 本项目会持续演进。我们提供了一份详细的 **[模板更新指南](.codecraft/docs/UPGRADING.md)**，指导你如何安全地将最新的改进同步到你自己的项目中。

---

## 1. 快速上手：与 CLI 助手同行

忘掉繁琐的手动操作，我们所有的核心工作流都被封装在一个强大的命令行助手 (`cli.py`) 中。

**强烈建议所有开发者（无论是人类还是AI）都通过这个工具与项目进行交互。**

想立刻开始？请直接跳转到我们的“快速入门教程”：
➡️ **[项目帮助中心：快速入门教程 (`project_docs/help/`)](./project_docs/help/01-quick-start-with-cli.md)**

---

## 2. 开发环境设置

在开始编码之前，请遵循以下步骤设置你的本地开发环境。

1.  **创建并激活虚拟环境**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/macOS
    # .\.venv\Scripts\activate  # Windows
    ```
2.  **安装项目依赖**:
    ```bash
    pip install --upgrade pip
    pip install -r .codecraft/requirements/dev.txt
    ```
3.  **激活 Git Hooks**:
    ```bash
    pre-commit install
    ```
    *   **说明**: 这将确保你的代码在提交前自动通过格式化和质量检查。

4.  **验证CLI工具**:
    检查我们的核心助手 `cli.py` 是否工作正常。
    ```bash
    python .codecraft/scripts/cli.py --help
    ```

---

## 3. 核心规范与指南

本项目的所有规范和流程，都已在我们的**项目帮助中心**中进行了详细的文档化。

*   ➡️ **[项目帮助中心 (`project_docs/help/`)](./project_docs/help/)**: **从这里开始！**
    *   **[01-快速入门教程](./project_docs/help/01-quick-start-with-cli.md)**: 端到端地学习如何使用 `cli.py` 进行开发。
    *   **[02-核心理念](./project_docs/help/02-core-concepts.md)**: 深入理解“项目即代码”的设计哲学。
    *   **[03-AI安全红线与工具](./project_docs/help/03-ai-safety-and-tools.md)**: 学习与AI安全协作的强制性准则。

*   **[贡献指南 (`CONTRIBUTING.md`)](./CONTRIBUTING.md)**: 包含了所有必须遵守的协作标准，例如 **Git工作流、分支命名、提交信息规范**等。

*   **[部署与运维指南 (`.codecraft/docs/DEPLOYMENT.md`)](./.codecraft/docs/DEPLOYMENT.md)**: 详细的生产环境部署和维护流程。

---

## 4. 构建、测试与部署

虽然 `cli.py` 简化了日常开发，但我们依然保留了底层的构建和验证脚本，用于本地的完整性检查和云端的 CI/CD。

### 本地完整构建

在发起 Pull Request 之前，**必须**运行本地完整构建脚本，确保所有检查通过：

```bash
bash .codecraft/scripts/build.sh
```

### 自动化CI/CD

本项目已配置好一套完整的GitHub Actions工作流 (`.github/workflows/ci-cd.yml`)，实现了持续集成和持续部署。所有检查通过是合并PR的必要条件。

---

## 5. 许可证 (License)

本项目采用 [MIT 许可证](LICENSE)。
