#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project ：LangChain-tutorial 
@File    ：demo01.py
@Author  ：zxb
@Date    ：2025/12/7 16:48
@Desc    ：
"""

import os
import sys

from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SequentialChain
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

    schainA_template = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一位精通各领域知识的知名教授"),
            ("human", "请你先尽可能详细的解释一下：{knowledge}，并且{action}")
        ]
    )
    schainA_chains = LLMChain(llm=llm,
                              verbose=True,
                              output_key="schainA_chains_key",
                              prompt=schainA_template)

    schainB_template = ChatPromptTemplate.from_messages(
        [
            ("system", "你非常善于提取文本中的重要信息，并做出简短的总结"),
            ("human", "这是针对一个提问完整的解释说明内容：{schainA_chains_key}"),
            ("human", "请你根据上述说明，尽可能简短的输出重要的结论，请控制在100个字以内")
        ]
    )
    schainB_chains = LLMChain(llm=llm, prompt=schainB_template, verbose=True, output_key="schainB_chains_key")

    Seq_chain = SequentialChain(
        chains=[schainA_chains, schainB_chains],
        verbose=True,
        input_variables=["knowledge", "action"],
        output_variables=["schainA_chains_key", "schainB_chains_key"]
    )
    response = Seq_chain.invoke({
        "knowledge": "如何使用LangChain进行对话",
        "action": "请尽可能详细地解释，并给出一个完整的例子"
    })
    print(response)


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
