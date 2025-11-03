# 帮助文档 01：使用 CLI 的端到端快速入门

欢迎来到 CodeCraftAI！本指南将带你走完一个完整的功能开发流程，全部使用我们强大的命令行助手 `cli.py`。这是与本项目协作的**最推荐**的方式。

## 预备知识

- 请确保你已经遵循主 `README.md` 的指引，创建并激活了你的 Python 虚拟环境，并安装了所有开发依赖。
- 所有 `cli.py` 命令都应在项目根目录运行。

---

### 第1步：创建一个新任务

一切都从一个想法或需求开始。让我们创建一个任务来“实现用户注销功能”。

```bash
python .codecraft/scripts/cli.py task new implement-user-logout
```

**发生了什么？**
- CLI 工具自动在 `tasks/backlog/` 目录下，为你创建了一个名为 `implement-user-logout.md` 的新任务文件。

---

### 第2步：开始处理任务

现在，你准备好开始编码了。这个命令会自动为你处理所有繁琐的准备工作。

```bash
python .codecraft/scripts/cli.py task start implement-user-logout --type fix
```
*(我们使用 `--type fix` 因为这更像是一个 Bug 修复或小功能)*

**发生了什么？**
1.  **创建并切换分支**: CLI 为你创建了一个名为 `fix/implement-user-logout` 的新 Git 分支，并自动切换过去。
2.  **更新任务状态**: 它将任务文件从 `tasks/backlog/` **用 `git mv`** 移动到了 `tasks/in_progress/`。
3.  **自动提交**: 它自动创建了一个 Commit，记录了这次状态变更。

你现在已经处于一个完美的开发环境中，可以开始编写代码和设计 Spec 了。

---

### 第3步：编码与智能优化

现在你可以开始编写代码了。在你编码的过程中，或者完成编码后，你可以使用 `ai` 命令组来自动提升你的代码质量。

假设你修改了文件 `src/codecraftai/auth.py`：

1.  **自动修复 Lint 错误**:
    ```bash
    python .codecraft/scripts/cli.py ai lint-fix src/codecraftai/auth.py
    ```
2.  **自动格式化代码**:
    ```bash
    python .codecraft/scripts/cli.py ai format src/codecraftai/auth.py
    ```
3.  **运行“代码医生” (推荐)**:
    这个命令会先执行上述两步，然后进行静态类型检查，并为你生成一个给 AI 的、用于修复剩余问题的精准提示。
    ```bash
    python .codecraft/scripts/cli.py ai doctor src/codecraftai/auth.py
    ```

---

### 第4步：完成任务

你的代码已经通过了所有测试，并且质量很高。现在是时候将它标记为完成了。

```bash
python .codecraft/scripts/cli.py task complete implement-user-logout
```

**发生了什么？**
- 在你当前的 `fix/implement-user-logout` 分支上，CLI 将任务文件从 `tasks/in_progress/` **用 `git mv`** 移动到了 `tasks/done/`，并自动创建了一个 Commit。

你现在可以安全地将这个分支推送到远程，并创建一个 Pull Request 进行审查了。

---

### 第5步 (如果需要): 安全地删除文件

假设你需要删除一个临时文件 `temp_notes.md`。**绝对不要**使用 `rm` 命令。你应该使用我们安全的 `delete` 命令。

```bash
python .codecraft/scripts/cli.py delete temp_notes.md
```

**发生了什么？**
1.  **强制性风险评估**: CLI 会强制你回答三个问题，评估删除的必要性和后果。
2.  **移入垃圾桶**: 文件不会被永久删除，而是被移动到了 `.trash/` 目录下。

如果你误删了，可以使用 `trash` 命令轻松恢复：
- `python .codecraft/scripts/cli.py trash list` (查看垃圾桶内容)
- `python .codecraft/scripts/cli.py trash restore <带时间戳的文件名>` (恢复文件)

这个 CLI 工具是为你和 AI 打造的“安全护栏”，请享受使用它带来的高效与安全！
