import pickle
import sys

from argparse import ArgumentParser, Namespace
from enum import Enum
from pathlib import Path

from autoeye.crypt import Credential, encrypt, gen_key, get_credential


class _Operation(str, Enum):
    KEYGEN = "keygen"
    ENCRYPT = "encrypt"


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
        "--out-file", "-o", default="credential.enc", required=True, type=Path
    )

    return parser.parse_args(argv)


def main(argv=sys.argv[1:]):
    args = _parse_args(argv)

    match args.operation:
        case _Operation.KEYGEN:
            gen_key(args.key_file)
            print(f"Saved secret key to {args.key_file}")
        case _Operation.ENCRYPT:
            credential = get_credential()
            encrypt(credential, args.key_file, args.out_file)
            print(f"Saved encrypted credentials to {args.out_file}")
        case _:
            print("Invalid operation", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
