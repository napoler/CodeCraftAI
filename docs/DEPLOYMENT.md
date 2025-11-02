# 部署与运维指南

本指南详细介绍了如何打包、部署、和维护本项目。

## 1. 环境要求

在部署或运行本项目前，请确保你的系统满足以下要求：

*   **核心依赖**:
    *   **Docker**: (推荐) 版本 `20.10+`。这是我们推荐的、用于保证环境一致性的核心工具。
    *   **Python**: (备选) `3.8` 或更高版本。如果你不使用 Docker，需要确保你的系统中有兼容的 Python 版本。
*   **硬件资源**:
    *   **内存 (RAM)**: 至少 2GB。
    *   **CPU**: 至少 1 核。

## 2. 部署方案

我们提供两种部署方案，请根据你的需求选择。

### 方案一：使用 Docker (推荐)

这是最简单、最可靠的部署方式，它封装了所有依赖，能确保在任何环境中都有一致的表现。

#### 构建 Docker 镜像

在项目根目录下，运行以下命令来构建镜像：
```bash
docker build -t codecraftai .
```
*   **说明**: `-t codecraftai` 为你的镜像指定了一个名称 (`codecraftai`)，你可以替换为你自己的名称。

#### 运行项目容器

*   **用于交互式开发**:
    如果你想启动一个容器并在其中进行开发或调试，`docker-compose` 是最简单的方式：
    ```bash
    docker-compose up -d
    ```
    这会启动一个在后台运行的服务。你可以通过以下命令进入容器的 shell：
    ```bash
    docker-compose exec app bash
    ```

*   **用于生产环境 (示例)**:
    ```bash
    docker run -d --name my-codecraft-app \
      -v /path/to/your/data:/app/data \
      -e MY_ENV_VAR=some_value \
      codecraftai
    ```
    *   **说明**:
        *   `-d`: 后台运行。
        *   `--name my-codecraft-app`: 为容器指定一个名称。
        *   `-v /path/to/your/data:/app/data`: (如果适用) 将你本地的数据目录挂载到容器的 `/app/data` 目录，以实现数据持久化。
        *   `-e MY_ENV_VAR=some_value`: (如果适用) 设置环境变量。

### 方案二：使用虚拟环境 (备选)

如果你无法或不想使用 Docker，可以遵循以下步骤在本地 Python 虚拟环境中运行。

1.  **创建虚拟环境**:
    *   **使用 `venv`**:
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```
    *   **使用 `conda`**:
        ```bash
        conda create -n codecraftai python=3.11
        conda activate codecraftai
        ```

2.  **安装依赖**:
    我们使用 `pip-tools` 管理锁定的依赖。
    ```bash
    pip install -r requirements/dev.txt
    ```

3.  **运行项目**:
    *根据你的项目具体情况，在这里添加运行指令*
    ```bash
    # python your_app/main.py
    ```

## 3. 打包与分发 (可选)

如果你的目标是将本项目作为一个 Python 包发布到 PyPI 或私有仓库，可以遵循以下步骤。

1.  **安装构建工具**:
    ```bash
    pip install build
    ```

2.  **执行构建**:
    在项目根目录下运行：
    ```bash
    python -m build
    ```
    这会在 `dist/` 目录下生成 `.tar.gz` (源码包) 和 `.whl` (Wheel, 二进制包)。

3.  **发布**:
    你可以使用 `twine` 等工具将 `dist/` 目录下的包上传到你选择的仓库。

## 4. 备份与恢复

*   **代码**: 所有的代码和配置都应由 Git 进行版本控制。请确保你定期将本地的提交推送到远程仓库。
*   **数据**: (如果适用) 任何由应用产生或使用的数据，如果不在版本控制中（例如，数据库文件、用户上传的内容等），都应制定定期备份策略。在使用 Docker 时，这些数据应通过挂载卷的方式存储在宿主机上，以便于备份。
*   **环境恢复**:
    *   **使用 Docker**: 恢复环境非常简单。只需在新机器上安装 Docker，然后从镜像仓库拉取（或从源码重新构建）镜像即可。
    *   **使用虚拟环境**: 在新机器上，重新执行“方案二”中的步骤即可快速重建一个完全相同的环境。

本指南旨在提供清晰的部署和维护流程。如有任何疑问，请通过创建一个 Issue 来联系我们。
