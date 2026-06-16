import tomllib
from pathlib import Path
from typing import Any


class Config:
    _config: dict[str, Any]

    def __init__(self, path: Path) -> None:
        self._config = self._load(path)

    def _load(self, path: Path) -> dict[str, dict]:
        with path.open(mode='rb') as f:
            return tomllib.load(f)

    def get(self, key: str) -> Any:
        path = self._config.get(key)

        if not path:
            raise

        return path
