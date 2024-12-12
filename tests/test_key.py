from pathlib import Path
from autoeye.crypt import gen_key


def test_generate_key(tmp_path: Path):
    key_path = tmp_path / "secret.key"
    assert not key_path.exists()

    gen_key(key_path)
    assert key_path.exists()
