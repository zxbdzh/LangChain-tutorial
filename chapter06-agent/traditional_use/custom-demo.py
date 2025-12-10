#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project :LangChain-tutorial 
@File    :custom-demo.py
@Author  :zxb
@Date    :2025/12/10 15:06
"""
import os

from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI


# 定义工具 - 计算器
def simple_calculator(expression: str)-> str:
    """
    基础数学计算工具，支持加减乘除和幂运算
    参数:
        expression: 数学表达式字符串，如"3 + 5" 或 "2**3"
    返回:
        计算结果字符串或错误信息
    """
    print(f"[计算工具调用] 正在计算：{expression}")

    print("计算完成~")
    return str(eval(expression))

# 创建工具对象
match_calculator_tool = Tool(
    name="Math_Calculator",
    func=simple_calculator,
    description="用于执行数学计算，输入必须是一个数学表达式，如'3 + 5' 或 '2**3'。不支持字母或特殊符号"
)

# 初始化大模型
load_dotenv()
llm = ChatOpenAI(
    model=os.getenv("LLM_MODEL"),
    temperature=0
)

# 初始化AgentExecutor
agent_executor = initialize_agent(
    tools=[match_calculator_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 测试
print("===测试：正常工具调用===")
res = agent_executor.invoke("计算9的平方")
print(res)