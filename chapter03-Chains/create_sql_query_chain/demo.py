#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project ：LangChain-tutorial 
@File    ：demo.py
@Author  ：zxb
@Date    ：2025/12/7 21:25
@Desc    ：
"""

import os
import sys

from dotenv import load_dotenv
from langchain_classic.chains.sql_database.query import create_sql_query_chain
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI

# 导入通知库（提前安装 plyer）
try:
    from plyer import notification
except ImportError:
    print("未安装 plyer 库，正在自动安装...")
    os.system(f"{sys.executable} -m pip install plyer")
    from plyer import notification


def main():
    """主函数入口（你的核心代码写在这里）"""
    load_dotenv()
    llm = ChatOpenAI(model=os.getenv("LLM_MODEL"))
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
    # print("哪种数据库:", db.dialect)
    # print("获取数据表:", db.get_usable_table_names())
    # 执行查询
    # res = db.run("SELECT count(1) from tourism_data")
    # print("查询结果:",res)
    chain = create_sql_query_chain(llm=llm, db=db)
    response = chain.invoke({"question": "一共有多少个用户？", "table_names_to_use": ["user"]})
    print(f"生成的sql:", response)
    actual_result = db.run(response)
    print(f"查询结果:", actual_result)


if __name__ == "__main__":
    try:
        main()  # 执行核心代码
        # 代码执行成功，发送通知
        notification.notify(
            title="✅ 脚本执行成功",
            message=f"文件：demo.py\n项目：LangChain-tutorial\n已全部运行完成！",
            timeout=10
        )
    except Exception as e:
        # 代码执行失败，发送错误通知
        notification.notify(
            title="❌ 脚本执行失败",
            message=f"文件：demo.py\n错误原因：{str(e)[:50]}...",  # 截取前50字错误信息
            timeout=15
        )
        raise e  # 继续抛出异常，不影响调试
