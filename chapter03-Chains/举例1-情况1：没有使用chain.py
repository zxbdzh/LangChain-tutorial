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

prompt_value = prompt_template.invoke({"topic": "冰淇淋"})

result = chat_model.invoke(prompt_value)

out_put = parser.invoke(result)

print(out_put)
print(type(out_put))
