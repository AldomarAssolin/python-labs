from datetime import datetime, timezone
from infra.mongo import get_db

def write_healthcheck(app_name: str = "python-labs") -> str:
    db = get_db()
    col = db["healthcheck"]
    res = col.insert_one({
        "app": app_name,
        "status": "ok",
        "ts": datetime.now(timezone.utc),
    })
    return str(res.inserted_id)

def list_healthchecks(limit: int = 10):
    db = get_db()
    col = db["healthcheck"]
    cursor = col.find({}, {"app": 1, "status": 1, "ts": 1}).sort("_id", -1).limit(limit)
    return list(cursor)
