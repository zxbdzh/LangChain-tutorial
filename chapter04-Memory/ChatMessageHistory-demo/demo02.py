#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project ：LangChain-tutorial 
@File    ：demo02.py
@Author  ：zxb
@Date    ：2025/12/8 09:58
@Desc    ：
"""

import os
import sys

from dotenv import load_dotenv
from langchain.memory import ChatMessageHistory
from langchain_openai import ChatOpenAI

# 导入通知库（提前安装 plyer）
try:
    from plyer import notification
except ImportError:
    print("未安装 plyer 库，正在自动安装...")
    os.system(f"{sys.executable} -m pip install plyer")
    from plyer import notification


def main():
    """主函数入口（你的核心代码写在这里）"""
    history = ChatMessageHistory()
    history.add_ai_message("我是一个无所不能的小智")
    history.add_user_message("你好，我叫小明，请介绍一下你自己")
    history.add_user_message("我是谁呢？")
    load_dotenv()
    llm = ChatOpenAI(model=os.getenv("LLM_MODEL"), verbose=True)
    ai_message = llm.invoke(history.messages)
    print(ai_message.content)
    history.add_ai_message(ai_message.content)
    history.add_user_message("再见，我是谁呢？")
    print(llm.invoke(history.messages).content)

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
