#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project :LangChain-tutorial 
@File    :demo01.py
@Author  :zxb
@Date    :2025/12/8 14:58
"""

import os
import sys
from typing import List, Dict, Optional

from dotenv import load_dotenv
from langchain_classic.chains.conversation.base import ConversationChain
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
    """主函数入口（你的核心代码写在这里）"""
    load_dotenv()
    llm = ChatOpenAI(model=os.getenv("LLM_MODEL"))

    template = """以下是人类与AI之间的友好对话描述。AI表现得很健谈，并提供了大量来自上下文的具体细节。如果AI不知道问题的答案，它会真诚地表示不知道。
    
    当前对话:
    {history}
    Human: {input}
    AI:
    """
    prompt = PromptTemplate.from_template(template)

    chain = ConversationChain(llm=llm, prompt=prompt, verbose=True)
    res = chain.invoke({"input": "你好，你的名字叫小智！"})
    print(res)

if __name__ == "__main__":
    try:
        main()  # 执行核心代码
        # 代码执行成功，发送通知
        notification.notify(
            title="✅ 脚本执行成功",
            message=f"文件：demo01.py\n项目：LangChain-tutorial\n已全部运行完成！",
            timeout=10
        )
    except Exception as e:
        # 代码执行失败，发送错误通知
        notification.notify(
            title="❌ 脚本执行失败",
            message=f"文件：demo01.py\n错误原因：{str(e)[:50]}...",  # 截取前50字错误信息
            timeout=15
        )
        raise e  # 继续抛出异常，不影响调试
