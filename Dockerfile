# 使用官方 Python 基础映像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 将依赖项列表复制到工作目录
COPY requirements.txt .

# 安装依赖项
RUN pip install --no-cache-dir -r requirements.txt

# 将项目代码复制到工作目录
COPY . .

# 运行 Discord 机器人脚本
CMD ["python", "discord_bot.py"]
