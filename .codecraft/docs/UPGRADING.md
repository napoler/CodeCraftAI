# 从模板更新项目指南

本指南旨在帮助已经使用了 CodeCraftAI 作为模板的开发者，安全、高效地将模板的最新改进同步到自己的项目中。

## 核心原则：安全第一

> ⚠️ **警告：** 这是一个**手动审查、有选择性地应用**的过程。**绝对不要**直接将模板的 `main` 分支合并到你的项目中，因为这极有可能导致冲突，或覆盖你自己的代码。我们的目标是借鉴模板的改进，而不是替换你的工作。

## 更新流程

我们推荐使用一种基于 `git remote` 和 `diff` 的安全更新策略。

### 步骤 1: 将模板仓库添加为 `template` 远程源

在你的项目仓库根目录下，运行以下命令。这个操作你只需要做一次。

```bash
git remote add template https://github.com/napoler/CodeCraftAI.git
```
这将把 CodeCraftAI 的官方仓库添加为一个名为 `template` 的远程源，方便你拉取最新的更新。

### 步骤 2: 拉取模板的最新变更

每当你希望同步更新时，请先运行以下命令，拉取模板的最新代码：

```bash
git fetch template
```
这会将模板仓库的所有分支和标签信息下载到你的本地，但不会修改你自己的任何代码。

### 步骤 3: 比较并应用变更

这是最关键的一步。你需要决定如何将模板的更新应用到你的项目中。

#### a) 应用一个全新的文件

如果模板新增了一个你的项目中没有的文件（例如，未来我们增加了 `.github/SECURITY.md`），你可以直接从模板的 `main` 分支 `checkout` 这个文件到你的当前分支。

```bash
# 示例：从模板的 main 分支，只拉取 SECURITY.md 这个文件
git checkout template/main -- .github/SECURITY.md
```

#### b) 更新一个已有的、你未修改过的文件

如果模板更新了一个配置文件，而你自从项目创建以来从未修改过它（例如，`.pre-commit-config.yaml` 或 `Dockerfile`），通常可以直接用模板的版本替换你的版本。

```bash
# 示例：用模板的 .pre-commit-config.yaml 覆盖你本地的版本
git checkout template/main -- .pre-commit-config.yaml
```
> **安全提示**: 在执行覆盖操作前，最好还是先用 `diff` 命令检查一下变更内容，以防万一。
> ```bash
> git diff template/main -- .pre-commit-config.yaml
> ```

#### c) 更新一个你已经修改过的文件 (最需要小心的场景)

对于那些你已经根据自己的项目需求修改过的文件（例如 `pyproject.toml`, `README.md`, `.gitignore`），**绝对不能直接覆盖**。

你应该使用 `diff` 命令来查看模板的变更，然后手动将你认为有价值的部分，逐一应用到你自己的文件中。

```bash
# 示例：查看模板的 pyproject.toml 文件与你当前版本有何不同
git diff template/main -- pyproject.toml
```
然后，你可以手动编辑你自己的 `pyproject.toml`，将模板中新增的开发依赖或配置项添加进去。

### 步骤 4: 提交你的更新

在你完成了所有变更的应用之后，像往常一样提交你的代码。

```bash
git add .
git commit -m "chore: Sync updates from CodeCraftAI template"
```

### (可选) 步骤 5: 清理

如果你不希望在你的远程源列表中保留 `template`，可以在更新完成后将其移除。
```bash
git remote remove template
```
下次需要更新时，再重新执行步骤 1 即可。

---

通过遵循这个手动、审查驱动的流程，你可以确保在吸收模板演进带来的好处的同时，最大程度地保护你自己项目的安全和完整性。
