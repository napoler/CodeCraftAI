# CodeCraftAI: AI驱动的开发规范与项目模板

> **【模板文件 - 请勿直接修改】**
>
> 本文件是 CodeCraftAI 核心模板的一部分。为了方便未来无冲突地升级模板，请**不要**直接修改本文件。
>
> 如果你需要添加你自己的项目介绍或文档，请在 `project_docs/` 目录下创建新的 Markdown 文件。

本项目是一个功能完备、遵循行业最佳实践的项目模板，旨在帮助开发者和团队快速启动一个规范化、高质量的AI工程项目。

> **模板的生命周期**: 本项目会持续演进。我们提供了一份详细的 **[模板更新指南](.codecraft/docs/UPGRADING.md)**，指导你如何安全地将最新的改进同步到你自己的项目中。

---

## 1. 将本项目作为模板

这是开始一个新项目的首选方式。你可以通过AI助手或手动操作，将本项目作为一个“母模板”，快速生成一个为你量身定制的新项目。

### 方式一：使用 AI 助手自动创建 (推荐)

**适用场景**: 你的AI编程助手（如Cursor、GitHub Copilot等）支持执行Git命令和文件操作。这是最高效、最不容易出错的方式。

**核心提示词**:
```
任务：使用 CodeCraftAI 项目作为模板，为我创建一个全新的、定制化的规范化项目。

请严格按照以下步骤执行：

1.  **克隆模板**: 从 `https://github.com/napoler/CodeCraftAI.git` 克隆项目到一个你选择的目录中。

2.  **收集新项目信息**: 在继续之前，请向我（用户）提问，以获取以下信息：
    *   **新项目的名称**: 例如 `MyNewDataProcessor`
    *   **新项目的简短描述**: 例如 `一个用于处理金融数据的工具。`

3.  **自动化修改**: 在克隆下来的模板中，系统地执行以下替换操作：
    *   在 `pyproject.toml` 文件中，将 `name = "CodeCraftAI"` 替换为新的项目名称。
    *   在 `README.md` 文件中，将标题 `# CodeCraftAI: ...` 及其下方的项目描述，替换为新的项目名称和描述。

4.  **清理与初始化**:
    *   删除 `.git` 目录。
    *   重新初始化一个新的 Git 仓库 (`git init`)。

5.  **完成**: 告诉我整个过程已完成，你的新项目已经准备就绪。
```

### 方式二：AI 自动集成到现有项目

**适用场景**: 你已经有一个项目，希望能安全、自动地引入本模板的全套规范和工具链。

**核心提示词**:
```
任务：将 CodeCraftAI 的开发规范和工具链，以非破坏性的方式，集成到我当前的项目中。

上下文：我有一个已经存在的 Git 项目，现在我希望引入 CodeCraftAI (`https://github.com/napoler/CodeCraftAI.git`) 的全套开发规范、工具链和文档模板，以提升项目的专业度。

请严格按照以下步骤，小心地执行操作，确保不要覆盖或删除我项目中任何现有的、与模板无关的文件：

1.  **临时克隆模板**: 在一个临时目录（例如 `/tmp/codecraftai-template`）中，克隆 `https://github.com/napoler/CodeCraftAI.git`。

2.  **复制核心组件**: 从临时克隆的模板中，将以下文件和目录复制到我当前项目的根目录下：
    *   整个 `.github/` 目录
    *   整个 `.codecraft/` 目录
    *   整个 `specs/` 目录
    *   整个 `tasks/` 目录
    *   整个 `project_docs/` 目录
    *   整个 `project_logs/` 目录
    *   `.dockerignore`
    *   `.pre-commit-config.yaml`
    *   `CONTRIBUTING.md`
    *   `Dockerfile`
    *   `docker-compose.yml`

3.  **智能合并文件**: 对于以下已存在的文件，请执行“合并”而不是“覆盖”：
    *   **`.gitignore`**: 如果我项目中已存在 `.gitignore`，请将模板中的规则**追加**到我现有文件的末尾，并确保没有重复的条目。
    *   **`pyproject.toml`**: 智能地将模板中的 `[project.optional-dependencies.dev]` 和 `requires-python` 等字段，合并到我现有的 `pyproject.toml` 文件中。
    *   **`README.md`**: 不要覆盖我的主 `README.md`。相反，请将模板 `README.md` 中关于“开发环境设置”和“核心规范”的部分，**追加**到我现有 `README.md` 的末尾。

4.  **清理**: 删除第一步创建的临时目录。

5.  **完成**: 告诉我集成已完成，并提醒我需要手动检查合并后的文件，然后运行 `pip install -r .codecraft/requirements/dev.txt` 和 `pre-commit install` 来完成设置。
```

### 方式三：手动创建

**适用场景**: 你希望完全手动控制项目的创建过程。

1.  **克隆仓库**:
    ```bash
    git clone https://github.com/napoler/CodeCraftAI.git <你的新项目目录>
    ```
2.  **进入目录并修改信息**:
    ```bash
    cd <你的新项目目录>
    ```
    *   手动修改 `pyproject.toml` 文件中的 `name` 字段。
    *   手动修改 `README.md` 的标题和描述。
3.  **重置Git历史**:
    ```bash
    rm -rf .git
    git init
    git add .
    git commit -m "Initial commit"
    ```
4.  **开始你的项目**: 你现在拥有了一个干净、规范化的项目起点。

### 常见问题 (FAQ)

**Q: 我必须使用你们推荐的所有工具和流程吗？**
A: 我们强烈推荐你保持这套集成的工具链。`pre-commit`, `black`, `ruff`, 和 `pytest` 共同构成了一个强大的质量保障体系。Spec-Driven的流程则能极大地减少沟通成本和返工。如果你选择移除或替换某些部分，请确保你的团队有替代方案来保证同样水平的质量和协作效率。

**Q: 如果这个模板更新了，我如何将这些更新同步到我的项目中？**
A: 我们提供了一份详细的 **[模板更新指南](.codecraft/docs/UPGRADING.md)**，它将指导你如何安全、高效地将模板的最新改进同步到你的项目中。

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
    *   **说明**: 这将使用我们锁定的版本文件，安装所有核心依赖和开发工具（如 `pytest`, `black`, `ruff`），以确保开发环境的绝对一致性。
3.  **激活 Git Hooks**:
    ```bash
    pre-commit install
    ```
    *   **说明**: 这将确保你的代码在提交前自动通过格式化和质量检查。
4.  **启动实时开发模式 (推荐)**:
    ```bash
    python .codecraft/scripts/guardian.py
    ```
    *   **说明**: 这将启动一个后台“守护”进程，实时监控你的文件变更，并自动运行代码检查、测试和文档构建。这是最高效的开发方式，详情请参阅 **[贡献指南](CONTRIBUTING.md)**。

---

## 3. 构建、测试与部署

我们建立了一套从本地开发到云端自动化的完整流程，以确保代码质量和部署效率。

### 本地构建与测试

在提交代码前，请务必在本地验证所有更改。

1.  **运行测试**:
    ```bash
    pytest
    ```
2.  **执行完整构建**:
    ```bash
    bash .codecraft/scripts/build.sh
    ```
    此脚本是本地的“真理之源”，它模拟了CI服务器将执行的绝大多数检查，包括：
    *   依赖关系检查
    *   代码质量扫描
    *   单元测试
    *   文档站点生成
    *   项目打包

    **只有当此脚本成功执行后，你的代码才被认为是“准备好”提交的。**

### 自动化CI/CD

本项目已配置好一套完整的GitHub Actions工作流 (`.github/workflows/ci-cd.yml`)，实现了持续集成和持续部署。

*   **持续集成 (CI)**: 当你创建一个Pull Request时，CI流程会自动触发。它将运行所有的测试和构建步骤，以确保你的更改不会破坏主分支。**所有检查通过是合并PR的必要条件。**
*   **持续部署 (CD)**: 当一个版本标签 (例如 `v1.0.0`) 被推送到 `main` 分支时，CD流程会自动触发。它将构建所有产物（Python包、文档压缩包），并自动创建一个GitHub Release，将这些产物附加为可下载的附件。

关于版本发布和标签的详细规范，请参阅 **[贡献指南 (`CONTRIBUTING.md`)](CONTRIBUTING.md)**。

### 手动部署

对于生产环境的部署，我们强烈推荐使用容器化方案。

*   **Docker 支持**: 本项目已完全容器化。
*   **部署指南**: 详细的构建、运行和维护说明，请参阅我们的 **[部署与运维指南 (`.codecraft/docs/DEPLOYMENT.md`)](.codecraft/docs/DEPLOYMENT.md)**。

---

## 4. 核心规范与指南

为了帮助你快速上手，我们已经将所有核心工作流都文档化了。

### a. 新手入门

*   **[项目帮助中心 (`project_docs/help/`)](./project_docs/help/)**: **从这里开始！** 这里有我们为你准备的一系列快速上手指南，涵盖了从管理任务到提交代码的所有核心流程。
*   **[贡献指南 (`CONTRIBUTING.md`)](./CONTRIBUTING.md)**: 包含了所有必须遵守的协作标准，例如 **Git工作流、分支命名、提交信息规范**等。

### b. 核心工作流文档

*   **[规范驱动开发 (`specs/`)](./specs/)**: 了解我们“先设计，后编码”的核心理念。
*   **[项目管理即代码 (`tasks/`)](./tasks/)**: 学习如何使用目录和文件来跟踪你的项目进度。
*   **[设计与脑图 (`project_docs/`)](./project_docs/)**: 学习如何使用脑图模板来规划你的功能。
*   **[沟通与决策日志 (`project_logs/`)](./project_logs/)**: 了解如何记录与AI和团队的讨论，以沉淀项目知识。

### c. 技术与模板文档

*   **[部署与运维指南 (`.codecraft/docs/DEPLOYMENT.md`)](./.codecraft/docs/DEPLOYMENT.md)**: 详细的生产环境部署和维护流程。
*   **[模板更新指南 (`.codecraft/docs/UPGRADING.md`)](./.codecraft/docs/UPGRADING.md)**: 如何安全地将本模板的更新同步到你的项目中。
*   **架构决策记录 (ADR)**: 所有重要的架构决策都记录在 ` .codecraft/adr/` 目录中。
*   **自动化代码质量**: 通过 `pre-commit` 集成了 `black` (格式化) 和 `ruff` (代码检查)。
*   **GitHub协作模板**: 位于 `.github/` 目录，包含了Issue和Pull Request的模板。

欢迎开始你的高质量AI项目开发之旅！

---

## 5. 许可证 (License)

本项目采用 [MIT 许可证](LICENSE)。

这意味着你可以自由地使用、修改和分发本项目的代码。所有对本项目的贡献，也将默认遵循此许可证。
