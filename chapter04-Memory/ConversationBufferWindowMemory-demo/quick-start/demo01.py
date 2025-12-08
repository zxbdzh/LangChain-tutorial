#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project :LangChain-tutorial 
@File    :demo01.py
@Author  :zxb
@Date    :2025/12/8 15:50
"""

import os
import sys

from langchain.memory import ConversationBufferWindowMemory

# 导入通知库（提前安装 plyer）
try:
    from plyer import notification
except ImportError:
    print("未安装 plyer 库，正在自动安装...")
    os.system(f"{sys.executable} -m pip install plyer")
    from plyer import notification


def main():
    # 实例化ConversationBufferWindowMemory对象，设定窗口阀值
    memory = ConversationBufferWindowMemory(k=2)
    # 保存消息
    memory.save_context({"input": "你好"}, {"output": "怎么了"})
    memory.save_context({"input": "我正在学习"}, {"output": "好的，我正在学习"})
    memory.save_context({"input": "你的生日是哪天？"}, {"output": "我不清楚"})

    # 读取内存中消息
    print(memory.load_memory_variables({}))

if __name__ == "__main__":
    try:
        main()  # 执行核心代码
        # 代码执行成功，发送通知
        notification.notify(
            title="✅ 脚本执行成功",
            message=f"文件：demo01.py\n项目：LangChain-tutorial\n已全部运行完成！",
            timeout=10
        )
    except Exception as e:
        # 代码执行失败，发送错误通知
        notification.notify(
            title="❌ 脚本执行失败",
            message=f"文件：demo01.py\n错误原因：{str(e)[:50]}...",  # 截取前50字错误信息
            timeout=15
        )
        raise e  # 继续抛出异常，不影响调试
