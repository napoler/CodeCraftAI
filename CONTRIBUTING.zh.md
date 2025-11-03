# 贡献指南 (Contribution Guidelines)

> **【模板文件 - 请勿直接修改】**
>
> 本文件是 CodeCraftAI 核心模板的一部分。为了方便未来无冲突地升级模板，请**不要**直接修改本文件。
>
> 如果你需要添加项目专属的贡献指南，请在 `project_docs/` 目录下创建新文件。

欢迎你为本项目贡献！本指南旨在帮助每一位成员（无论是人类还是AI）高效协作，并共同维护项目的长期健康。

## 0. 基本原则 (Fundamental Principles)

### **元规则：一切行动，以文档为准 (The Documentation-First Principle)**

这是本项目的**最高行为准则**。

- 在执行任何操作或使用本项目提供的任何自动化工具之前，你**必须**首先查阅并遵循相关的官方文档。所有工具的权威使用规范，均定义在 **[工具集与自动化标准](./.codecraft/docs/05-tooling-and-automation-standard.md)** 中。
- 如果文档中的规范与你之前的理解有任何冲突，**永远以文档为准**。

**在开始之前，请务必先阅读我们的 [快速入门教程 (`project_docs/help/`)](./project_docs/help/)**。

## 1. 核心理念：CLI 驱动的开发

我们项目的核心是**命令行助手 (`cli.py`)**。它将我们所有复杂的 Git 工作流、项目管理和代码质量检查，都封装成了简单、统一的命令。

**所有开发者（人类与AI）都必须优先使用 `cli.py` 与项目进行交互。** 这不是一个建议，而是一项要求，因为它内置了我们所有的流程规范和安全检查。

## 2. AI 安全红线 (AI Safety Red Lines)

这是一套为 AI 开发者制定的，**必须严格遵守**的最高优先级准则。

### **红线一：禁止原生文件删除**
- **严禁** AI 直接使用任何操作系统的原生删除命令，如 `rm`, `del` 等。
- **必须**: 所有文件的删除操作，都**必须**通过我们提供的安全命令行工具执行：
  ```bash
  python .codecraft/scripts/cli.py delete <file_path>
  ```
- **理由**: 该命令内置了强制性的“风险评估”问答和可恢复的“垃圾桶”机制，是防止灾难性误删除的核心防线。

### **红线二：禁止直接修改受保护文件**
- 本项目在 `.codecraft/protected_paths.yml` 文件中定义了一份“受保护路径”清单。
- **严禁** AI 对此清单中的任何文件进行直接的修改、移动或删除。
- **必须**: 如果 AI 认为需要修改一个受保护的文件，它**必须**停止操作，并明确地向人类开发者 **`@user`** 请求审查和批准。

### **红线三：必须遵循容错与日志记录标准**
- 所有代码的编写，**必须**严格遵守项目中定义的 **[容错性与日志记录标准](./.codecraft/docs/04-error-handling-and-logging-standard.md)**。
- 在处理任何可能失败的操作（如文件IO、网络请求）时，必须使用 `try...except` 结构，并记录下有意义的错误日志。严禁静默忽略任何异常。

---

## 3. 标准开发工作流 (由 CLI 驱动)

请遵循 `project_docs/help/01-quick-start-with-cli.md` 中的端到端教程。以下是对其核心步骤的摘要：

1.  **创建任务**:
    `python .codecraft/scripts/cli.py task new <task-title>`
2.  **开始任务**:
    `python .codecraft/scripts/cli.py task start <task-title>`
    *(这会自动为你创建分支、移动任务文件并创建第一个Commit)*
3.  **编码与设计**:
    - 编写你的代码。
    - 编写或更新对应的 `specs/` 文件。
4.  **代码质量优化 (AI 开发者强制执行)**:
    在提交代码前，对你修改的每一个文件运行“代码医生”：
    `python .codecraft/scripts/cli.py ai doctor <file_path>`
    *(这会自动格式化、修复Lint错误，并对无法修复的类型错误生成修复提示)*
5.  **完成任务**:
    `python .codecraft/scripts/cli.py task complete <task-title>`
    *(这会将任务移至 `done/` 目录并创建Commit)*
6.  **创建 Pull Request**:
    - 将你的分支推送到远程仓库。
    - 创建一个 Pull Request，并在描述中链接到对应的任务和 Spec 文件。

## 4. Git 规范

虽然 `cli.py` 为你处理了大部分 Git 操作，但你仍需遵守以下规范：

### **分支命名**
CLI 会自动为你生成符合 `类型/简短描述` 格式的分支名 (例如 `feat/user-login`)。

### **提交信息 (Commit Messages)**
我们采用 **Conventional Commits** 规范 (`<类型>: <描述>`)。CLI 生成的 Commit 会自动遵循此规范。对于你自己的代码提交，也请同样遵守。

**`<类型>`** 必须是以下之一：
*   **feat**: 新功能
*   **fix**: Bug 修复
*   **docs**: 文档变更
*   **refactor**: 代码重构
*   **test**: 增加或修改测试
*   **chore**: 构建过程或辅助工具的变动 (例如，CLI生成的提交)

## 5. 本地完整构建验证

在发起 Pull Request 之前，**必须**运行本地完整构建脚本，确保所有检查通过：

```bash
bash .codecraft/scripts/build.sh
```
这个脚本是最终的质量门槛，它模拟了云端 CI 将执行的所有检查。

感谢你的贡献！
