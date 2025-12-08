#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project :LangChain-tutorial 
@File    :demo.py
@Author  :zxb
@Date    :2025/12/8 18:33
"""

import os
import sys
from typing import List, Dict, Optional

from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain.memory import ConversationBufferWindowMemory
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# 导入通知库（提前安装 plyer）
try:
    from plyer import notification
except ImportError:
    print("未安装 plyer 库，正在自动安装...")
    os.system(f"{sys.executable} -m pip install plyer")
    from plyer import notification


def main():
    # 定义模板
    template = """以下是人类与AI之间的友好对话描述，AI表现得很健谈，并提供了大量来自其上下文的具体细节。如果AI不知道问题的答案，它会表示不知道。
    
    当前对话:
    {history}
    Human: {question}
    AI:"""
    # 定义提示词模板
    prompt_template = PromptTemplate.from_template(template)

    # 创建大模型
    load_dotenv()
    llm = ChatOpenAI(model=os.getenv("LLM_MODEL"))

    # 实例化ConversationBufferWindowMemory对象，设定窗口阈值
    memory = ConversationBufferWindowMemory(k=1)

    # 定义LLMChain
    conversation_with_summary = LLMChain(
        llm=llm,
        prompt=prompt_template,
        memory=memory,
        verbose=True
    )

    # 执行链
    conversation_with_summary.invoke({"question": "你好, 我叫孙小空"})
    conversation_with_summary.invoke({"question": "我还有两个徒弟, 一个是猪小戒, 一个是沙小僧"})
    conversation_with_summary.invoke({"question": "我今年高考，居然考上了1本"})
    res = conversation_with_summary.invoke({"question": "我叫什么？"})
    print(res)

if __name__ == "__main__":
    try:
        main()  # 执行核心代码
        # 代码执行成功，发送通知
        notification.notify(
            title="✅ 脚本执行成功",
            message=f"文件：demo.py\n项目：LangChain-tutorial\n已全部运行完成！",
            timeout=10
        )
    except Exception as e:
        # 代码执行失败，发送错误通知
        notification.notify(
            title="❌ 脚本执行失败",
            message=f"文件：demo.py\n错误原因：{str(e)[:50]}...",  # 截取前50字错误信息
            timeout=15
        )
        raise e  # 继续抛出异常，不影响调试
