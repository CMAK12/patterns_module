from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = "postgresql+asyncpg://postgres:123@localhost:5432/bookdb"
