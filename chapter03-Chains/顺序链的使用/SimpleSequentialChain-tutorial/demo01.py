#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project ：LangChain-tutorial 
@File    ：demo01.py
@Author  ：你的名字
@Date    ：2025/12/7 15:12
@Desc    ：
"""

import os
import sys

from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SimpleSequentialChain
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
    chainA_template = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一位精通各种领域知识的知名教授"),
            ("human", "请你尽可能详细的解释一下：{knowledge}"),
        ]
    )
    chainA_chains = LLMChain(llm=llm, prompt=chainA_template, verbose=True)
    # chainA_chains.invoke({"knowledge": "什么是LangChain？"})
    chainB_template = ChatPromptTemplate.from_messages(
        [
            ("system", "你非常善于提取文本中的重要信息，并做出简短的总结"),
            ("human", "这是针对一个提问的完整的解释说明内容：{description}"),
            ("human", "请你根据上述说明，尽可能简短的输出重要的结论，请控制在20个字以内")
        ]
    )
    chainB_chains = LLMChain(llm=llm, prompt=chainB_template, verbose=True)
    full_chain = SimpleSequentialChain(chains=[chainA_chains, chainB_chains], verbose=True)
    result = full_chain.invoke({"input": "什么是LangChain？"})
    print(result)

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
