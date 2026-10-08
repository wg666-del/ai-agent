# AI Agent 全栈开发实战

Python + FastAPI + LLM + LangChain + LangGraph + DeepAgents

## 当前阶段

第二章：Python AI 开发环境搭建

## 技术栈

- Python 3.12
- FastAPI
- Uvicorn
- uv

## 运行项目

```bash
uv sync
uv run uvicorn app.main:app --reload

## 项目结构

```text
app/
├── api/              FastAPI 接口层
├── core/             核心配置、常量、日志、异常
├── schemas/          Pydantic 请求与响应模型
├── services/         业务逻辑层
├── repositories/     数据访问层
├── models/           数据库 ORM 模型
└── dependencies/     FastAPI 依赖注入