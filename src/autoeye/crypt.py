import pickle
from getpass import getpass

from cryptography.fernet import Fernet
from pathlib import Path

from autoeye.credential import Credential


def gen_key(out_file: Path) -> None:
    key = Fernet.generate_key()
    out_file.write_bytes(key)


def get_credential() -> Credential:
    return Credential(username=input("Username: "), password=getpass())


def encrypt(credential: Credential, key_path: Path, out_file: Path) -> None:
    key = Fernet(key_path.read_bytes())
    pickled_credential = pickle.dumps(credential)
    encrypted_bytes = key.encrypt(pickled_credential)
    out_file.write_bytes(encrypted_bytes)
