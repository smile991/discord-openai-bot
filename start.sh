#!/bin/sh

# 读取用户输入的 Discord 令牌和 OpenAI API 密钥
echo "Please enter your Discord token: "
read DISCORD_TOKEN
echo "Please enter your OpenAI API key: "
read OPENAI_API_KEY

# 创建discord_bot的镜像
docker build -t discord_bot .


# 运行 Docker 容器，并将读取到的变量作为环境变量传递给容器
docker run --name discord_bot -d \
    -e DISCORD_TOKEN="$DISCORD_TOKEN" \
    -e OPENAI_API_KEY="$OPENAI_API_KEY" \
    discord_bot
