import os
from dotenv import load_dotenv

load_dotenv()

from infra.mongo import get_db, ping  # noqa

try:
    if ping():
        print("✅ Conectou no MongoDB Atlas")

    db = get_db()
    col = db["healthcheck"]
    res = col.insert_one({"app": "python-labs", "status": "ok"})
    print("✅ Insert OK:", res.inserted_id)
except:
    print("Erro ao conectar")
