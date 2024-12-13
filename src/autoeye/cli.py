import sys

from argparse import ArgumentParser, Namespace
from enum import Enum
from pathlib import Path

from autoeye.crypt import save_credential, gen_key, create_credential
from autoeye.exceptions import InvalidKeyException


class _Operation(str, Enum):
    KEYGEN = "keygen"
    ENCRYPT = "encrypt"

    def __str__(self) -> str:
        return self.value


def _parse_args(argv) -> Namespace:
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(
        dest="operation", required=True, help="Operation"
    )

    keygen_parser = subparsers.add_parser(
        _Operation.KEYGEN, help="Generate a secret key"
    )
    keygen_parser.add_argument(
        "--key-file", "-k", default="secret.key", required=True, type=Path
    )

    encrypt_parser = subparsers.add_parser(
        _Operation.ENCRYPT, help="Encrypt a username and password"
    )
    encrypt_parser.add_argument(
        "--key-file", "-k", default="secret.key", required=True, type=Path
    )
    encrypt_parser.add_argument(
        "--cred-file", "-o", default="credential.enc", required=True, type=Path
    )

    return parser.parse_args(argv)


def _encrypt(key_file: Path, cred_file: Path) -> None:
    credential = create_credential()
    try:
        save_credential(credential, key_file, cred_file)
        print(f"Saved encrypted credentials to {cred_file}")
    except InvalidKeyException as e:
        print(f"Invalid key provided: {e.key_path}", file=sys.stderr)
        sys.exit(1)


def _generate(key_file: Path) -> None:
    gen_key(key_file)
    print(f"Saved secret key to {key_file}")


def main(argv=sys.argv[1:]):
    args = _parse_args(argv)

    match args.operation:
        case _Operation.KEYGEN:
            _generate(args.key_file)
        case _Operation.ENCRYPT:
            _encrypt(args.key_file, args.cred_file)
        case _:
            print("Invalid operation", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
