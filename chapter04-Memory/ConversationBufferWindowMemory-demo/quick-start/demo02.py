#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project :LangChain-tutorial 
@File    :demo02.py
@Author  :zxb
@Date    :2025/12/8 15:54
"""

import os
import sys
from typing import List, Dict, Optional

from langchain_classic.memory import ConversationBufferWindowMemory

# 导入通知库（提前安装 plyer）
try:
    from plyer import notification
except ImportError:
    print("未安装 plyer 库，正在自动安装...")
    os.system(f"{sys.executable} -m pip install plyer")
    from plyer import notification


def main():
    # 实例化ConversationBufferWindowMemory对象，设定窗口阀值
    memory = ConversationBufferWindowMemory(k=2, return_messages=True)

    # 保存消息
    memory.save_context({"input": "hi"}, {"output": "whats up"})
    memory.save_context({"input": "not sure"}, {"output": "I am good"})
    memory.save_context({"input": "how are you"}, {"output": "I am good too"})

    # 读取内存中消息
    print(memory.load_memory_variables({}))

if __name__ == "__main__":
    try:
        main()  # 执行核心代码
        # 代码执行成功，发送通知
        notification.notify(
            title="✅ 脚本执行成功",
            message=f"文件：demo02.py\n项目：LangChain-tutorial\n已全部运行完成！",
            timeout=10
        )
    except Exception as e:
        # 代码执行失败，发送错误通知
        notification.notify(
            title="❌ 脚本执行失败",
            message=f"文件：demo02.py\n错误原因：{str(e)[:50]}...",  # 截取前50字错误信息
            timeout=15
        )
        raise e  # 继续抛出异常，不影响调试
