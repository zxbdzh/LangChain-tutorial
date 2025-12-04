import asyncio
import os
import time

import dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

dotenv.load_dotenv()

# 初始化大模型
chat_model = ChatOpenAI(model=os.getenv('LLM_MODEL'))


# 同步调用
def sync_test():
    messages1 = [
        SystemMessage(content="你是一位乐于助人的智能小助手"),
        HumanMessage(content="请帮我介绍一下什么是机器学习")
    ]
    start_time = time.time()
    response = chat_model.invoke(messages1)
    duration = time.time() - start_time
    print(f"同步调用耗时：{duration:.2f}秒")
    return response, duration


# 异步调用
async def async_test():
    messages1 = [
        SystemMessage(content="你是一位乐于助人的智能小助手"),
        HumanMessage(content="请帮我介绍一下什么是机器学习")
    ]
    start_time = time.time()
    response = await chat_model.ainvoke(messages1)
    duration = time.time() - start_time
    print(f"异步调用耗时：{duration:.2f}秒")
    return response, duration


if __name__ == "__main__":
    sync_response, sync_duration = sync_test()
    print(f"同步响应内容: {sync_response.content[:100]}...\n")

    async_response, async_duration = asyncio.run(async_test())
    print(f"异步响应内容: {async_response.content[:100]}...\n")

    # 并发测试
    print("\n===并发测试 ===")
    start_time = time.time()


    async def run_concurrent_tests():
        # 创建3个异步任务
        tasks = [async_test() for _ in range(3)]
        # 并发执行所有任务
        return await asyncio.gather(*tasks)


    # 执行并发测试
    results = asyncio.run(run_concurrent_tests())

    total_time = time.time() - start_time
    print(f"\n3个并发异步调用总耗时：{total_time:2f}秒")
    print(f"平均每个调用耗时：{total_time / 3:2f}秒")
