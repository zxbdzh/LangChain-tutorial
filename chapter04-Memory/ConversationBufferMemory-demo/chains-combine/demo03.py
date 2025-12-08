#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project :LangChain-tutorial 
@File    :demo03.py
@Author  :zxb
@Date    :2025/12/8 13:51
"""

import os
import sys

from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate
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
    load_dotenv()
    llm = ChatOpenAI(model=os.getenv("LLM_MODEL"))

    # 创建prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个与人类对话的机器人。"),
        ("human", "问题: {question}")
    ])

    # 创建Memory
    memory = ConversationBufferMemory(return_messages=True)

    # 创建LLMChain
    llm_chain = LLMChain(prompt=prompt, llm=llm, memory=memory)

    # 调用LLMChain
    res1 = llm_chain.invoke({"question": "中国首都在哪里？"})
    print(res1, end="\n\n")
    res2 = llm_chain.invoke({"question": "我刚刚问了什么？"})
    print(res2)


if __name__ == "__main__":
    try:
        main()  # 执行核心代码
        # 代码执行成功，发送通知
        notification.notify(
            title="✅ 脚本执行成功",
            message=f"文件：demo03.py\n项目：LangChain-tutorial\n已全部运行完成！",
            timeout=10
        )
    except Exception as e:
        # 代码执行失败，发送错误通知
        notification.notify(
            title="❌ 脚本执行失败",
            message=f"文件：demo03.py\n错误原因：{str(e)[:50]}...",  # 截取前50字错误信息
            timeout=15
        )
        raise e  # 继续抛出异常，不影响调试
