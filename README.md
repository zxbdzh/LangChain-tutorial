# LangChain 教程项目

这是一个系统性的 LangChain 教程项目，旨在帮助开发者快速掌握 LangChain 框架的使用方法。

## 项目介绍

本项目包含了 LangChain 框架的各种核心概念和使用方法，通过实际代码示例帮助学习者理解并应用 LangChain 构建 AI 应用。

## 目录结构

```
├── chapter01-summary/          # 第一章：项目概述
│   └── HelloWorld.ipynb        # Hello World 示例
├── chapter02-Model IO/         # 第二章：模型输入输出
│   ├── 1.模型的调用.ipynb      # 模型调用示例
│   ├── Model IO之Prompt Template.ipynb  # Prompt Template 使用
│   ├── async_demo.py           # 异步调用示例
│   └── JSON解析器JsonOutputParse-举例1.py  # JSON 输出解析示例
└── requirements.txt            # 项目依赖
```

## 环境要求

- Python 3.8+
- 相关依赖包 (详见 requirements.txt)

## 安装步骤

1. 克隆项目到本地：
   ```bash
   git clone <repository-url>
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

3. 配置环境变量：
   在项目根目录创建 `.env` 文件，并添加必要的环境变量：
   ```env
   OPENAI_API_KEY=your_openai_api_key
   LLM_MODEL=glm-4.6
   ```

## 使用说明

每个章节都包含独立的示例代码，可以直接运行查看效果。建议按照章节顺序逐步学习。

## 学习资源

- [LangChain官方文档](https://docs.langchain.com/)
- [LangChain GitHub仓库](https://github.com/langchain-ai/langchain)

## 注意事项

- 请确保正确配置API密钥
- 部分功能可能产生API调用费用
- 建议在虚拟环境中运行项目

## 许可证

MIT License