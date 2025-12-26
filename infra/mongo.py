import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi

_client: MongoClient | None = None

def get_client() -> MongoClient:
    global _client
    if _client is None:
        uri = os.getenv("MONGODB_URI")
        if not uri:
            raise RuntimeError("MONGODB_URI não definido (use .env ou variável de ambiente).")

        timeout = int(os.getenv("MONGODB_TIMEOUT_MS", "5000"))

        _client = MongoClient(
            uri,
            server_api=ServerApi("1"),
            serverSelectionTimeoutMS=timeout,
        )
    return _client

def get_db():
    db_name = os.getenv("MONGODB_DB", "pythonlabs")
    return get_client()[db_name]

def ping() -> bool:
    get_client().admin.command("ping")
    return True
