#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project :LangChain-tutorial 
@File    :demo02.py
@Author  :zxb
@Date    :2025/12/8 11:14
"""

import os
import sys
from typing import List, Dict, Optional

# 导入通知库（提前安装 plyer）
try:
    from plyer import notification
except ImportError:
    print("未安装 plyer 库，正在自动安装...")
    os.system(f"{sys.executable} -m pip install plyer")
    from plyer import notification


def main():
    """主函数入口（你的核心代码写在这里）"""
    # 1. 导入相关包
    from langchain.memory import ConversationBufferMemory

    # 2. 实例化ConversationBufferMemory对象
    memory = ConversationBufferMemory(return_messages=True)

    # 3. 保存消息到内存中
    memory.save_context({"input": "hi"}, outputs={"output": "whats up"})

    # 4. 读取内存中消息（返回消息）
    print(memory.load_memory_variables({}))

    # 5. 读取内存中消息（返回原始消息列表）
    print(memory.chat_memory.messages)

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
