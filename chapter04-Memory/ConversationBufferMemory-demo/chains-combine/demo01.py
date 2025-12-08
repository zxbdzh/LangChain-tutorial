#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project :LangChain-tutorial 
@File    :demo01.py
@Author  :zxb
@Date    :2025/12/8 12:00
"""

import os
import sys
from typing import List, Dict, Optional

from dotenv import load_dotenv

# 导入通知库（提前安装 plyer）
try:
    from plyer import notification
except ImportError:
    print("未安装 plyer 库，正在自动安装...")
    os.system(f"{sys.executable} -m pip install plyer")
    from plyer import notification


def main():
    """主函数入口（你的核心代码写在这里）"""
    from langchain_openai import OpenAI
    from langchain.memory import ConversationBufferMemory
    from langchain.chains.llm import LLMChain
    from langchain_core.prompts import PromptTemplate

    # 初始化大模型
    load_dotenv()
    llm =  OpenAI(model=os.getenv("LLM_MODEL"), temperature=0)

    # 创建提示
    # 有两个输入键：实际输入域来自记忆类的输入 需确保PromptTemplate和ConversationBufferMemory的键匹配
    template = """你可以与人类对话
    
    当前对话: {history}
    
    人类问题: {question}
    
    回复: 
    """
    prompt = PromptTemplate.from_template(template)

    # 创建ConversationBufferMemory
    memory = ConversationBufferMemory()

    # 初始化链
    chain = LLMChain(llm=llm, prompt=prompt, memory=memory)

    # 提问
    res = chain.invoke({"question": "我的名字叫Tom"})
    print(res)
    res = chain.invoke({"question": "我的名字是什么呢？"})
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
