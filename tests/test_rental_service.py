import json

from app.services import log_service


def test_write_log_creates_log_entry(tmp_path, monkeypatch):
    test_log_file = tmp_path / "activity_log.json"

    monkeypatch.setattr(log_service, "LOG_FILE", test_log_file)

    log_service.write_log(
        action="test_action",
        telegram_id=123456,
        details="Test log message"
    )

    with open(test_log_file, "r", encoding="utf-8") as file:
        logs = json.load(file)

    assert len(logs) == 1
    assert logs[0]["action"] == "test_action"
    assert logs[0]["telegram_id"] == 123456
    assert logs[0]["details"] == "Test log message"