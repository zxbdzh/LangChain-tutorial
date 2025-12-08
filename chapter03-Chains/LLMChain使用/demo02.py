#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project ：LangChain-tutorial 
@File    ：demo02.py
@Author  ：zxb
@Date    ：2025/12/7 13:25
@Desc    ：
"""

import os
import sys

from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# 导入通知库（提前安装 plyer）
try:
    from plyer import notification
except ImportError:
    print("未安装 plyer 库，正在自动安装...")
    os.system(f"{sys.executable} -m pip install plyer")
    from plyer import notification


def main():
    """
    主函数入口（你的核心代码写在这里）
    举例2：verbose参数，使用使用ChatPromptTemplate
    """
    load_dotenv()

    # 1. 定义提示模板对象
    chat_template = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一位{area}领域具备丰富经验的高端技术人才"),
            ("human", "给我讲一个{adjective}笑话")
        ]
    )

    # 2. 定义模型
    llm = ChatOpenAI(model=os.getenv("LLM_MODEL"))

    # 3. 定义LLMChain
    llm_chain = LLMChain(llm=llm, prompt=chat_template, verbose=True)

    # 4. 调用LLMChain

    response = llm_chain.invoke({"area": "机器学习", "adjective": "冰淇淋"})
    print(response)

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
