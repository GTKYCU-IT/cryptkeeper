import pickle

from cryptography.fernet import Fernet
from getpass import getpass
from pathlib import Path

from autoeye.credential import Credential
from autoeye.exceptions import InvalidKeyException


def gen_key(out_file: Path) -> None:
    key = Fernet.generate_key()
    out_file.write_bytes(key)


def create_credential() -> Credential:
    return Credential(username=input("Username: "), password=getpass())


def save_credential(credential: Credential, key_path: Path, cred_path: Path) -> None:
    try:
        key = Fernet(key_path.read_bytes())
    except ValueError:
        raise InvalidKeyException(key_path)

    pickled_credential = pickle.dumps(credential)
    encrypted_bytes = key.encrypt(pickled_credential)
    cred_path.write_bytes(encrypted_bytes)


def load_credential(cred_path: Path, key_path: Path) -> Credential:
    key = Fernet(key_path.read_bytes())
    decrypted_bytes = key.decrypt(cred_path.read_bytes())
    return pickle.loads(decrypted_bytes)
