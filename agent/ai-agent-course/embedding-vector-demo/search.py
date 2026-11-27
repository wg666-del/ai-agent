import asyncio

from vector_store import initialize_vector_store


async def main():
    vector_store = await initialize_vector_store()

    query = "员工休年假需要提前多久申请？"

    results = await vector_store.asimilarity_search(
        query=query,
        k=3,
    )

    print(f"Query: {query}")

    for index, document in enumerate(results, start=1):
        print(f"\nTop {index}")
        print("Content:", document.page_content)
        print("Metadata:", document.metadata)


if __name__ == "__main__":
    asyncio.run(main())