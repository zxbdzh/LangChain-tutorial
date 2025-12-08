import os

from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

# 1. 创建大模型实例
chat_model = ChatOpenAI(model=os.getenv("LLM_MODEL"))

# 2. 原始字符串模板
template = "桌上有{number}个苹果，四个桃子和三本书，一共有几个水果？"
prompt = PromptTemplate.from_template(template)

# 3. 创建LLMChain
llm_chain = LLMChain(
    llm=chat_model,
    prompt=prompt
)

# 4. 调用LLMChain，返回结果
print(llm_chain.invoke({"number": 5}))
