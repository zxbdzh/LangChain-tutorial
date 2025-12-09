#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project :LangChain-tutorial 
@File    :demo02.py
@Author  :zxb
@Date    :2025/12/9 11:20
"""
import os
import sys
from typing import List, Dict, Optional

from langchain_core.tools import tool

# 导入通知库（提前安装 plyer）
try:
    from plyer import notification
except ImportError:
    print("未安装 plyer 库，正在自动安装...")
    os.system(f"{sys.executable} -m pip install plyer")
    from plyer import notification

# ------------- 关键：自动获取文件名和项目名 -------------
# 当前脚本文件名（含后缀，如 test.py）
FILE_NAME = os.path.basename(sys.argv[0])
# 当前脚本文件名（不含后缀，如 test）
FILE_NAME_NO_EXT = os.path.splitext(FILE_NAME)[0]
# 项目名（默认取脚本所在文件夹的名称，可根据需要修改）
PROJECT_NAME = os.path.basename(os.path.dirname(os.path.abspath(sys.argv[0])))
# ------------------------------------------------------

@tool(name_or_callable="add_two_number", description="two number add", return_direct=True)
def add_number(a: int, b: int) -> int:
    return a + b


def main():
    """主函数入口（你的核心代码写在这里）"""
    print(f"name={add_number.name}")
    print(f"name={add_number.args}")
    print(f"name={add_number.description}")
    print(f"name={add_number.return_direct}")

    res = add_number.invoke({"a": 10, "b": 20})
    print(res)


if __name__ == "__main__":
    try:
        main()  # 执行核心代码
        # 代码执行成功，发送通知（直接使用上面定义的变量）
        notification.notify(
            title="✅ 脚本执行成功",
            message=f"文件：{FILE_NAME}\n项目：{PROJECT_NAME}\n已全部运行完成！",
            timeout=10
        )
    except Exception as e:
        # 代码执行失败，发送错误通知
        notification.notify(
            title="❌ 脚本执行失败",
            message=f"文件：{FILE_NAME}\n错误原因：{str(e)[:50]}...",  # 截取前50字错误信息
            timeout=15
        )
        raise e  # 继续抛出异常，不影响调试