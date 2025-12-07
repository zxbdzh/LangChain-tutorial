import os

from dotenv import load_dotenv
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

chat_model = ChatOpenAI(model=os.getenv("LLM_MODEL"))

# 创建解析器
output_parser = CommaSeparatedListOutputParser()

# 创建LangChain提示模板
chat_prompt = PromptTemplate.from_template(
    "生成5个关于{text}的列表.\n\n{format_instructions}",
    partial_variables={"format_instructions": output_parser.get_format_instructions()
    }
)

# 将提示和模型合并 调用
chain = chat_prompt | chat_model | output_parser
res = chain.invoke({"text": "电影"})
print(res)
print(type(res))