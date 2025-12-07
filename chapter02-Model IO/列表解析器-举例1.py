from langchain_core.output_parsers import CommaSeparatedListOutputParser

output_parser = CommaSeparatedListOutputParser()

# 返回一些指令或模板，这些指令告诉系统如何解析或格式化输出数据
format_instructions = output_parser.get_format_instructions()
print(format_instructions)

messages = "大象,猩猩,狮子"
result = output_parser.parse(messages)
print(result)
print(type(result))