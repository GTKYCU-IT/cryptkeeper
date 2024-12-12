from pathlib import Path

from autoeye.crypt import Credential, encrypt


def test_encrypt_decrypt(tmp_path: Path) -> None:
    crypt_path = tmp_path / "credential.enc"
    credential = Credential(username="username", password="password")

    encrypted_bytes = encrypt(credential)
