# 使用官方 Python 基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 将依赖文件复制到工作目录
COPY requirements/dev.txt .

# 安装依赖
RUN pip install --no-cache-dir -r dev.txt

# 将项目代码复制到工作目录
COPY . .

# （可选）暴露端口，如果你的应用是一个服务
# EXPOSE 8000

# （可选）运行应用的命令
# CMD ["python", "your_app/main.py"]
