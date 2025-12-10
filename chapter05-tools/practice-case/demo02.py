#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project :LangChain-tutorial 
@File    :demo01.py
@Author  :zxb
@Date    :2025/12/9 17:06
"""
import json
import os

from dotenv import load_dotenv
from langchain_community.tools import MoveFileTool
from langchain_core.messages import HumanMessage
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_openai import ChatOpenAI

load_dotenv()

# 定义LLM
chat_model = ChatOpenAI(model=os.getenv("LLM_MODEL"), temperature=0)

# 定义工具
tools = [MoveFileTool()]

# 4.需要将工具转换为openai函数，后续再将函数传入模型调用
functions = [convert_to_openai_function(t) for t in tools]

# 5.提供大模型调用的消息列表
messages = [HumanMessage(content="将本目录下的a.txt移动到F盘")]

# 6.调用大模型
response = chat_model.invoke(
    input=messages,
    functions=functions
)

# print(response)

if "function_call" in response.additional_kwargs:
    tool_name = response.additional_kwargs["function_call"]["name"]
    tool_args = json.loads(response.additional_kwargs["function_call"]["arguments"])
    print(f"调用工具: {tool_name}, 参数: {tool_args}")
    if "move_file" in response.additional_kwargs["function_call"]["name"]:
        tool = MoveFileTool()
        result = tool.run(tool_args) # 执行工具
        print("工具执行结果:", result)
else:
    print("模型回复:", response.content)
