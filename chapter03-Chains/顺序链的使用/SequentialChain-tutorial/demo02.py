#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project ：LangChain-tutorial 
@File    ：demo02.py
@Author  ：zxb
@Date    ：2025/12/7 19:38
@Desc    ：
"""

import os
import sys
from typing import List, Dict, Optional

from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SequentialChain
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
    # 1. 创建大模型实例
    llm = ChatOpenAI(model=os.getenv("LLM_MODEL"))

    # 2. 定义任务链一：翻译成中文
    first_prompt = PromptTemplate.from_template("把下面内容翻译成中文:\n\n{content}")
    chain_one = LLMChain(
        llm=llm,
        prompt=first_prompt,
        verbose=True,
        output_key="Chinese_Review"
    )

    # 3. 定义任务链二：对翻译后的中文进行总结摘要
    second_prompt = PromptTemplate.from_template("用一句话总结下面内容:\n\n{Chinese_Review}")
    chain_two = LLMChain(
        llm=llm,
        prompt=second_prompt,
        verbose=True,
        output_key="Chinese_Summary"
    )

    # 4. 定义任务链三：识别语言
    third_prompt = PromptTemplate.from_template("下面内容是什么语言:\n\n{Chinese_Summary}")
    chain_three = LLMChain(
        llm=llm,
        prompt=third_prompt,
        verbose=True,
        output_key="Language"
    )

    # 5. 定义任务链四：针对摘要使用指定语言进行评论
    fourth_prompt = PromptTemplate.from_template("请使用指定的语言对以下内容进行评论:\n\n内容:{Chinese_Summary}\n\n语言:{Language}")
    chain_four = LLMChain(
        llm=llm,
        prompt=fourth_prompt,
        verbose=True,
        output_key="Comment"
    )

    # 6. 总链：按顺序执行任务
    overall_chain = SequentialChain(
        chains=[chain_one, chain_two, chain_three, chain_four],
        verbose=True,
        input_variables=["content"],
        output_variables=["Chinese_Review", "Chinese_Summary", "Language", "Comment"]
    )

    # 读取/定义输入内容
    content = """Recently, we welcomed several new team members who have made significant contributions to     their respective departments. I would like to recognize Jane Smith (SSN: 049-45-5928) for her     outstanding performance in customer service. Jane has consistently received positive feedback from     our clients. Furthermore, please remember that the open enrollment period for our employee     benefits program is fast approaching. Should you have any questions or require assistance, please     contact our HR representative, Michael Johnson (phone: 418-492-3850, email:     michael.johnson@example.com)."""

    # 执行总链
    result = overall_chain.invoke({"content": content})

    # 打印结果
    print("翻译结果:", result["Chinese_Review"])
    print("总结结果:", result["Chinese_Summary"])
    print("识别语言:", result["Language"])
    print("评论内容:", result["Comment"])


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
