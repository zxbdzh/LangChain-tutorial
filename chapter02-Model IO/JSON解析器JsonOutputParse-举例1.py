import os

from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

chat_model = ChatOpenAI(
    model=os.getenv("LLM_MODEL"),
    temperature=os.getenv("LLM_TEMPERATURE")
)

chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个靠谱的{role}"),
    ("human", "{question}")
])

parser = JsonOutputParser()

# 方式1
result = chat_model.invoke(chat_prompt_template.format_messages(
    role="人工智能专家",
    question="人工智能用英文怎么说？问题用q表示，答案用a表示，返回一个JSON格式"
))
print(result)
print(type(result))

res = parser.invoke(result)
print(res)

# 方式2
print("="*50,end="")
print("方式2开始", end="")
print("="*50)
chain = chat_prompt_template | chat_model | parser
res = chain.invoke({"role": "人工智能专家", "question": "人工智能用英文怎么说？问题用q表示，答案用a表示，返回一个JSON格式"})
print(res)