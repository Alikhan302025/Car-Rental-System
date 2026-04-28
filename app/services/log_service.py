import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("data/activity_log.json")


def write_log(action: str, telegram_id: int, details: str):
    try:
        if not LOG_FILE.exists():
            LOG_FILE.write_text("[]", encoding="utf-8")

        with open(LOG_FILE, "r", encoding="utf-8") as file:
            logs = json.load(file)

        logs.append({
            "time": datetime.now().isoformat(timespec="seconds"),
            "action": action,
            "telegram_id": telegram_id,
            "details": details
        })

        with open(LOG_FILE, "w", encoding="utf-8") as file:
            json.dump(logs, file, indent=4, ensure_ascii=False)

    except Exception as e:
        print("Log error:", e)