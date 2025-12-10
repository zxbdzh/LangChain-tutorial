#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project :LangChain-tutorial 
@File    :demo01.py
@Author  :zxb
@Date    :2025/12/10 09:44
"""
import os

from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_community.tools import TavilySearchResults
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI

# 设置api秘钥
load_dotenv()

# 初始化搜索工具
search = TavilySearchResults(max_results=3)

# 创建Tool实例
search_tool = Tool(
    name="Search",
    func=search.run,
    description="搜索工具，输入搜索内容，返回搜索结果"
)

# 初始化LLM
llm = ChatOpenAI(
    model=os.getenv("LLM_MODEL"),
    temperature=0
)

# 创建AgentExecutor
agent_executor = initialize_agent(
    llm=llm,
    tools=[search_tool],
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

# 测试查询
query = "今天厦门的天气怎么样？"
result = agent_executor.invoke(query)
print(f"查询结果: {result}")