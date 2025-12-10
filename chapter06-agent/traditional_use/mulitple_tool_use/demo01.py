#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project :LangChain-tutorial 
@File    :demo01.py
@Author  :zxb
@Date    :2025/12/10 13:03
"""
import os

from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_community.tools import TavilySearchResults
from langchain_core.tools import Tool
from langchain_experimental.utilities.python import PythonREPL
from langchain_openai import ChatOpenAI

load_dotenv()

# 定义搜索工具
search = TavilySearchResults(max_results=3)

search_tool = Tool(
    name="Search",
    func=search.run,
    description="用于搜索互联网上的信息，特别是股票价格和新闻"
)

# 定义计算工具
python_repl = PythonREPL()

calc_tool = Tool(
    name="Calculator",
    func=python_repl.run,
    description="用于执行数学计算，例如百分比变化"
)

# 定义llm
llm = ChatOpenAI(
    model=os.getenv("LLM_MODEL"),
    temperature=0
)

# 创建AgentExecutor
agent_executor = initialize_agent(
    tools=[search_tool, calc_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

query = "特斯拉今天的股票价格如何？比上周的变化是多少？"
result = agent_executor.invoke(query)
print(f"查询结果: {result}")