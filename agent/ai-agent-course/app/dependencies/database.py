from collections.abc import AsyncGenerator

class MockBDSession:
    async def execute(self, sql: str) -> str:
        return f"执行 SQL：{sql}"

    async def close(self):
        print("关闭 MockDBSession")


async def get_db_session() -> AsyncGenerator[MockBDSession, None]:
    db = MockBDSession()

    try:
        yield db
    finally:
        await db.close()