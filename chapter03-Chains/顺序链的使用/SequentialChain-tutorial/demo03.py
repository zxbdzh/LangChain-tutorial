#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project ：LangChain-tutorial 
@File    ：demo03.py
@Author  ：zxb
@Date    ：2025/12/7 20:31
@Desc    ：
"""

import os
import sys
from typing import List, Dict, Optional

from flask.cli import load_dotenv
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
    # 创建大模型实例
    load_dotenv()
    llm = ChatOpenAI(model=os.getenv("LLM_MODEL"))

    # 第1环节:
    query_chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate.from_template(template="请模拟查询{product}的市场价格，直接返回一个合理的价格数字（如    6999），不要包含任何其他文字或代码"),
        verbose=True,
        output_key="price"
    )

    # 第2环节:
    promo_chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate.from_template(template="为{product}（售价：{price}元）创作一篇50字以内的促销文案，要    求突出产品卖点"),
        verbose=True,
        output_key="promo_text"
    )

    sequential_chain = SequentialChain(
        chains=[query_chain, promo_chain],
        verbose=True,
        input_variables=["product"],  # 初始输入
        output_variables=["price", "promo_text"],  # 输出价格和文案
    )

    result = sequential_chain.invoke({"product": "iPhone16"})
    print(result)

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
