# CodeCraftAI: AI驱动的开发规范与项目模板

本项目是一个功能完备、遵循行业最佳实践的项目模板，旨在帮助开发者和团队快速启动一个规范化、高质量的AI工程项目。

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

### 方式二：手动创建

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
    pip install -r requirements/dev.txt
    ```
    *   **说明**: 这将使用我们锁定的版本文件，安装所有核心依赖和开发工具（如 `pytest`, `black`, `ruff`），以确保开发环境的绝对一致性。
3.  **激活 Git Hooks**:
    ```bash
    pre-commit install
    ```
    *   **说明**: 这将确保你的代码在提交前自动通过格式化和质量检查。

---

## 3. 部署 (Deployment)

我们提供全面的部署支持，旨在实现轻松、可靠的部署流程。

*   **Docker 支持**: 本项目已完全容器化。我们强烈推荐使用 **Docker** 进行部署，以保证环境的一致性和可移植性。
*   **多环境指南**: 我们也为不使用 Docker 的用户提供了详细的虚拟环境（`venv`, `conda`）设置指南。

详细的构建、运行和维护说明，请参阅我们的 **[部署与运维指南 (`docs/DEPLOYMENT.md`)](docs/DEPLOYMENT.md)**。

---

## 4. 本模板包含的核心规范

本项目内置了一整套规范，旨在提升团队协作效率和项目质量。

*   **[贡献指南 (`CONTRIBUTING.md`)](CONTRIBUTING.md)**: 包含了详细的 **Git工作流、分支命名、提交信息规范**等团队协作标准。
*   **[规范驱动开发 (`specs/README.md`)](specs/README.md)**: 我们采用Spec-Driven Development流程，确保在编码前达成共识。所有新功能都始于一份规范文档。
*   **自动化代码质量**: 通过 `pre-commit` 集成了 `black` (格式化) 和 `ruff` (代码检查)。
*   **标准化测试**: 使用 `pytest` 作为测试框架，所有测试位于 `tests/` 目录。
*   **Pull Request模板**: 位于 `.github/PULL_REQUEST_TEMPLATE.md`，规范化代码审查流程。

欢迎开始你的高质量AI项目开发之旅！

---

## 4. 许可证 (License)

本项目采用 [MIT 许可证](LICENSE)。

这意味着你可以自由地使用、修改和分发本项目的代码。所有对本项目的贡献，也将默认遵循此许可证。
