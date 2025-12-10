#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project :LangChain-tutorial 
@File    :demo01.py
@Author  :zxb
@Date    :2025/12/10 09:10
"""
import os

from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from langchain_community.tools import FileSearchTool

load_dotenv()

llm = ChatOpenAI(model=os.getenv("LLM_MODEL"))

# 创建AgentExecutor
agent_executor = initialize_agent(
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    tools=[FileSearchTool()],
    verbose=True
)

# 执行
res = agent_executor.run("当前目录下是否有a.txt")
print(res)