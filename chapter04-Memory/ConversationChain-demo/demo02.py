#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project :LangChain-tutorial 
@File    :demo02.py
@Author  :zxb
@Date    :2025/12/8 15:07
"""

import os
import sys
from typing import List, Dict, Optional

from dotenv import load_dotenv
from langchain.chains.conversation.base import ConversationChain
from langchain_openai import ChatOpenAI

# 导入通知库（提前安装 plyer）
try:
    from plyer import notification
except ImportError:
    print("未安装 plyer 库，正在自动安装...")
    os.system(f"{sys.executable} -m pip install plyer")
    from plyer import notification


def main():
    load_dotenv()
    llm = ChatOpenAI(model=os.getenv("LLM_MODEL"))

    # 初始化对话链
    conv_chain = ConversationChain(llm=llm)

    # 进行对话
    conv_chain.invoke(input="小明有1只猫")
    conv_chain.invoke(input="小刚有2只狗")
    res = conv_chain.invoke(input="小明和小刚一共有多少只宠物？")
    print(res)

if __name__ == "__main__":
    try:
        main()  # 执行核心代码
        # 代码执行成功，发送通知
        notification.notify(
            title="✅ 脚本执行成功",
            message=f"文件：demo02.py\n项目：LangChain-tutorial\n已全部运行完成！",
            timeout=10
        )
    except Exception as e:
        # 代码执行失败，发送错误通知
        notification.notify(
            title="❌ 脚本执行失败",
            message=f"文件：demo02.py\n错误原因：{str(e)[:50]}...",  # 截取前50字错误信息
            timeout=15
        )
        raise e  # 继续抛出异常，不影响调试
