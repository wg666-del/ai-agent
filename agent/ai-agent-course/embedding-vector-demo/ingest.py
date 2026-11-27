import asyncio
import uuid

from langchain_core.documents import Document

from vector_store import initialize_vector_store


async def main():
    vector_store = await initialize_vector_store()

    documents = [
        Document(
            id=str(uuid.uuid4()),
            page_content=(
                "员工申请年假需要提前三个工作日提交申请，"
                "审批通过后才能休假。"
            ),
            metadata={
                "source": "hr-policy",
                "category": "leave",
                "department": "HR",
                "tenant_id": "tenant_001",
            },
        ),
        Document(
            id=str(uuid.uuid4()),
            page_content=(
                "员工申请病假需要提交医院相关证明，"
                "并按照公司规定完成审批流程。"
            ),
            metadata={
                "source": "hr-policy",
                "category": "sick_leave",
                "department": "HR",
                "tenant_id": "tenant_001",
            },
        ),
        Document(
            id=str(uuid.uuid4()),
            page_content=(
                "企业服务器部署需要配置Docker环境，"
                "并完成应用镜像构建与容器启动。"
            ),
            metadata={
                "source": "devops-guide",
                "category": "deployment",
                "department": "IT",
                "tenant_id": "tenant_001",
            },
        ),
    ]

    # langchain-postgres v2 的 PGVectorStore：
    # add_documents 是同步方法，异步场景应使用 aadd_documents
    await vector_store.aadd_documents(documents)

    print(f"成功入库 {len(documents)} 条文档")


if __name__ == "__main__":
    asyncio.run(main())