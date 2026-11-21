import json
from pathlib import Path

from domain.service_request import ServiceRequest
from domain.exceptions import PersistenceError


class FileRepository:
    """Reads and writes service requests in the required JSON file."""

    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.file_path.exists():
            self.file_path.write_text("[]", encoding="utf-8")

    def load_all(self):
        try:
            raw_data = self.file_path.read_text(encoding="utf-8").strip()
            if not raw_data:
                return []
            records = json.loads(raw_data)
            if not isinstance(records, list):
                raise PersistenceError("The JSON root must contain a list of requests.")
            return [ServiceRequest.from_dict(record) for record in records]
        except json.JSONDecodeError as exc:
            raise PersistenceError(
                f"Could not read {self.file_path}: invalid JSON."
            ) from exc
        except (KeyError, TypeError, ValueError) as exc:
            raise PersistenceError(
                f"Stored request data is incomplete or invalid: {exc}"
            ) from exc

    def save_all(self, requests):
        try:
            data = [request.to_dict() for request in requests]
            self.file_path.write_text(
                json.dumps(data, indent=4), encoding="utf-8"
            )
        except OSError as exc:
            raise PersistenceError(
                f"Could not save requests to {self.file_path}: {exc}"
            ) from exc