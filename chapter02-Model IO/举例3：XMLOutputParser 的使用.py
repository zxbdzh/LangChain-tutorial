import os

from dotenv import load_dotenv
from langchain_core.output_parsers import XMLOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

# 初始化语言模型
chat_model = ChatOpenAI(model=os.getenv("LLM_MODEL"))

# 测试模型的xml解析效果
actor_query="生成汤姆·汉克斯的简短电影记录，使用中文回复"

# 定义XMLOutputParser对象
parser = XMLOutputParser()

# 定义提示词模板对象
prompt_template = PromptTemplate.from_template("{query}\n{format_instructions}")

prompt_template1 = prompt_template.partial(format_instructions=parser.get_format_instructions())

response = chat_model.invoke(prompt_template1.format_prompt(query=actor_query))
print(response.content)