#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project ：LangChain-tutorial 
@File    ：demo02.py
@Author  ：zxb
@Date    ：2025/12/7 15:47
@Desc    ：
"""

import os
import sys

from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SimpleSequentialChain
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
    # 1. 创建大模型
    llm = ChatOpenAI(model=os.getenv("LLM_MODEL"))
    # 2. 定义一个给剧名写大纲的LLMChain
    template1 = """你是个剧作家。给定剧本的标题，你的工作就是为这个标题写一个大纲。
    Title: {title}
    """
    prompt_template1 = PromptTemplate(input_variables=['title'], template=template1)
    synopsis_chain = LLMChain(llm=llm, prompt=prompt_template1)
    # 3. 定义给一个剧本大纲写一篇评论的LLMChain
    template2 = """你是《纽约时报》的剧评家。有了剧本的大纲，你的工作就是为剧本写一篇评论剧情大纲：
    {synopsis}
    """
    prompt_template2 = PromptTemplate(input_variables=['synopsis'], template=template2)
    review_chain = LLMChain(llm=llm, prompt=prompt_template2)

    # 4. 定义一个完整的链按顺序执行
    overall_chain = SimpleSequentialChain(chains=[synopsis_chain, review_chain], verbose=True)
    # 5. 调用顺序链
    review = overall_chain.invoke("日落海滩上的悲剧")
    print(review)


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
