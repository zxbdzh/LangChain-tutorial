import os

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

chat_model = ChatOpenAI(model=os.getenv("LLM_MODEL"))

messages = [
    SystemMessage(content="将一下内容从英文翻译成中文"),
    HumanMessage(content="I love programming.")
]

result = chat_model.invoke(messages)
print(type(result))
print(result)

parser = StrOutputParser()
# 使用parser处理model返回的结果
response = parser.invoke(result)
print(type(response))
print(response)