import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

chat_model = ChatOpenAI(model=os.getenv("LLM_MODEL"))

prompt_template = PromptTemplate.from_template(
    template="给我讲一个关于{topic}话题的简短笑话"
)

parser = StrOutputParser()

# 链式调用
chain = prompt_template | chat_model | parser
out_put = chain.invoke({"topic": "冰淇淋"})
print(out_put)
print(type(out_put))
