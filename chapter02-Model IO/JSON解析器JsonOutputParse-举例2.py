import os

from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()
chat_model = ChatOpenAI(model=os.getenv("LLM_MODEL"))

joke_query = "告诉我一个笑话。"

# 定义json解析器
parser = JsonOutputParser()

# 定义提示词模板
prompt = PromptTemplate(
    template="回答用户的查询.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# 使用LCEL语法组合一个简单的链
chain = prompt | chat_model | parser
# 执行链
output = chain.invoke({"query": "给我讲一个笑话"})
print(output)
