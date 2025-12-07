import os

from dotenv import load_dotenv
from langchain_core.output_parsers import XMLOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

chat_model = ChatOpenAI(model=os.getenv("LLM_MODEL"))

output_parser = XMLOutputParser()
# 返回一些指令或模板，这些指令告诉系统如何解析或格式化输出数据
format_instructions = output_parser.get_format_instructions()
print(format_instructions)
# 测试模型的xml解析效果
actor_query = "生成汤姆·汉克斯的简短电影记录和信息等"
output = chat_model.invoke(f"""
{actor_query}请将影片附在<movie></movie>标签中
""")
print(type(output))
print(output.content)
