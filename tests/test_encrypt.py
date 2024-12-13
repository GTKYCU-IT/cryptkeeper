from pathlib import Path

from cryptkeeper.cli import gen_key
from cryptkeeper.crypt import Credential, save_credential, load_credential


def test_encrypt_decrypt(tmp_path: Path) -> None:
    cred_path = tmp_path / "credential.enc"
    key_path = tmp_path / "secret.key"

    gen_key(key_path)

    credential = Credential(username="username", password="password")
    save_credential(credential, key_path, cred_path)

    assert cred_path.exists()

    decrypted_credential = load_credential(cred_path, key_path)
    assert decrypted_credential == credential
