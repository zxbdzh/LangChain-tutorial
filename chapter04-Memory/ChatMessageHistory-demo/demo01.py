#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project ：LangChain-tutorial 
@File    ：demo01.py
@Author  ：zxb
@Date    ：2025/12/8 09:11
@Desc    ：
"""

import os
import sys
from langchain.memory import ChatMessageHistory

# 导入通知库（提前安装 plyer）
try:
    from plyer import notification
except ImportError:
    print("未安装 plyer 库，正在自动安装...")
    os.system(f"{sys.executable} -m pip install plyer")
    from plyer import notification


def main():
    """主函数入口（你的核心代码写在这里）"""
    # 实例化ChatMessageHistory
    history = ChatMessageHistory()
    # 添加UserMessage
    history.add_user_message("hi!")
    # 添加AIMessage
    history.add_ai_message("what's up?")
    # 输出存储的消息
    print(history.messages)

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
