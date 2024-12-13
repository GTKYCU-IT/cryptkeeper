from pathlib import Path


class InvalidKeyException(Exception):
    _key_path: Path

    def __init__(self, key_path: Path, *args: object) -> None:
        super().__init__(*args)

        self._key_path = key_path

    @property
    def key_path(self) -> Path:
        return self._key_path
