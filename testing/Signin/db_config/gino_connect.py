from gino import Gino

db = Gino()
async def sess_db():
    await db.set_bind("postgresql+asyncpg://postgres:1303@localhost:5432/user",
                      min_size=5,
                      max_size=10,
                      echo=True)