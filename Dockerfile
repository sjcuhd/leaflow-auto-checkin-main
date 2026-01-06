# 使用支持 Chromium 的 Python 基础镜像
FROM python:3.11-slim-bookworm

# 设置时区和环境变量
ENV TZ=Asia/Shanghai \
    PYTHONUNBUFFERED=1 \
    HEADLESS=true

# 安装系统依赖 (包含 Chromium 和 驱动)
RUN apt-get update && apt-get install -y --no-install-recommends \
    chromium \
    chromium-driver \
    git \
    tzdata \
    && ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . .

# 启动命令 (使用调度器)
CMD ["python", "scheduler.py"]
