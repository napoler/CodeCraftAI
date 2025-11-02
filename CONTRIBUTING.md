# 贡献指南 (Contribution Guidelines)

欢迎你为 CodeCraftAI 项目贡献代码或文档！为了确保项目的高效协作和代码库的长期健康，我们制定了以下规范。请在开始工作前仔细阅读。

## 1. 沟通语言

为了方便当前团队的沟通，我们约定所有公开的交流和文档编写均使用 **中文**。这包括：
*   Git 提交信息 (Commit Messages)
*   Pull Request (PR) 的描述
*   代码中的注释
*   `specs/` 目录下的规范文档

*注：随着项目的发展和国际化，未来可能会转为使用英语。*

## 2. Git 工作流规范

我们遵循一个结构化的 Git 工作流，以保持版本历史的清晰和可追溯性。

### 分支命名

所有分支都应从 `main` 分支创建，并遵循以下命名约定：

*   **`feat/<description>`**: 用于开发新功能。
    *   示例: `feat/real-time-debugging`
*   **`fix/<description>`**: 用于修复 Bug。
    *   示例: `fix/incorrect-code-suggestion`
*   **`docs/<description>`**: 用于添加或修改文档。
    *   示例: `docs/update-contributing-guide`
*   **`style/<description>`**: 用于代码风格相关的修改（如格式化）。
    *   示例: `style/apply-black-formatter`
*   **`refactor/<description>`**: 用于既非新功能也非 Bug 修复的代码重构。
    *   示例: `refactor/simplify-context-engine`
*   **`test/<description>`**: 用于添加或修改测试。
    *   示例: `test/add-unit-tests-for-parser`
*   **`chore/<description>`**: 用于构建过程、工具链等与项目代码无关的修改。
    *   示例: `chore/update-pre-commit-hooks`

### 提交信息 (Commit Messages)

我们采用 **Conventional Commits** 规范来编写提交信息。这使得提交历史极具可读性，并为自动化生成更新日志（Changelog）打下基础。

**格式**:
```
<类型>[可选的作用域]: <描述>

[可选的正文]

[可选的页脚]
```

**`<类型>`** 必须是以下之一：
*   **feat**: 新功能
*   **fix**: Bug 修复
*   **docs**: 文档变更
*   **style**: 代码风格（不影响代码含义的更改，如格式化）
*   **refactor**: 代码重构
*   **test**: 增加或修改测试
*   **chore**: 构建过程或辅助工具的变动

**示例**:
```
feat(api): add endpoint for user profiles

为用户系统增加了获取个人信息的 API 端点。
正文部分可以详细描述本次提交。

Fixes #123
```
```
docs: 完善贡献指南中的分支命名规则
```

## 3. 开发流程

1.  **领取任务**: 在开始工作前，请确保有一个对应的规范文档（Spec）或议题（Issue）。
2.  **创建分支**: 从最新的 `main` 分支，根据上述“分支命名”规范创建一个新的分支。
3.  **编码与测试**:
    *   进行代码开发。
    *   为你的代码编写必要的测试。
    *   确保所有测试都能通过 (`pytest`)。
    *   确保你的代码通过了 `pre-commit` 的所有检查。
4.  **提交代码**: 遵循“提交信息”规范，提交你的代码。
5.  **发起 Pull Request**:
    *   将你的分支推送到远程仓库。
    *   发起一个指向 `main` 分支的 Pull Request。
    *   使用我们提供的 [Pull Request 模板](.github/PULL_REQUEST_TEMPLATE.md) 填写所有必要信息，特别是关联的规范文档。
6.  **代码审查**: 至少需要一位其他团队成员的批准（Approve），你的 PR 才能被合并。
7.  **合并**: PR 被批准后，项目维护者会将其合并到 `main` 分支。

## 4. 代码注释

好的代码应该是不言自明的，但注释在必要时也至关重要。请遵循以下原则：

*   **解释“为什么”，而不是“做什么”**。
    *   **Bad**: `// 循环遍历用户列表` (代码本身已经很清楚了)
    *   **Good**: `// 为了优化性能，这里采用了惰性加载策略，只有在用户滚动时才加载下一页数据。`
*   **为复杂的业务逻辑、算法或正则表达式添加注释**。
*   **对于临时的解决方案或已知的技术债，使用 `TODO` 或 `FIXME`**。
    *   `# TODO: 未来需要替换为更高效的缓存方案`

感谢你的贡献！
