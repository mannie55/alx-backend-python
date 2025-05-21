import asyncio
import aiosqlite

DB_NAME = 'my_database.db'

async def async_fetch_users():
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT * FROM users")
        results = await cursor.fetchall()
        return results
        await cursor.close()


async def async_fetch_older_users():
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > 40")
        results = await cursor.fetchall()
        return results
        await cursor.close()


async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

asyncio.run(fetch_concurrently())