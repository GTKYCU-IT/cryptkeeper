# CryptKeeper CLI Tool 🔒

CryptKeeper is a command-line tool for managing encrypted credentials using secure key-based encryption. 🔑

## Features 🔧

- **Key Generation:** Create a secure key for encryption and decryption.
- **Credential Encryption:** Encrypt username and password credentials using the generated key.

## Installation 📦

1. Clone the repository:

   ```bash
   git clone https://github.com/GTKYCU-IT/cryptkeeper
   cd cryptkeeper
   ```

2. Install the package using pip:

   ```bash
   pip install .
   ```

## Usage 🔐

### Generate a Secret Key 🗝️

```bash
cryptkeeper keygen --key-file secret.key
```

This command creates a file named `secret.key` containing a secure encryption key.

### Encrypt Credentials 🔒

```bash
cryptkeeper encrypt --key-file secret.key --cred-file credential.enc
```

Follow the prompts to enter your username and password. The credentials will be encrypted and saved to `credential.enc`.

## Command Line Arguments ⚙️

### `keygen` (Generate Key)

- `--key-file`, `-k` (required): Path to save the generated key file. Default: `secret.key`

### `encrypt` (Encrypt Credentials)

- `--key-file`, `-k` (required): Path to the encryption key file.
- `--cred-file`, `-o` (required): Path to save the encrypted credential file.

## Security Recommendations 🔐

To secure your secret key, consider the following best practices:

- **File Permissions:** Restrict access to the secret key file by adjusting file permissions:

  ```bash
  chmod 600 secret.key
  ```

  This command ensures only the file owner can read and write the key.

- **Secure Storage:** Use encrypted storage services or a hardware security module (HSM).

- **Environment Variables:** Store key paths in environment variables instead of hardcoding them.

- **Backups:** Keep a secure backup of the key in a separate, secure location.

- **Access Monitoring:** Monitor access logs to detect unauthorized access attempts.

## Example Workflow 🔄

1. Generate a secret key:

   ```bash
   cryptkeeper keygen --key-file my_secret.key
   ```

2. Encrypt credentials:

   ```bash
   cryptkeeper encrypt --key-file my_secret.key --cred-file my_credentials.enc
   ```

3. Store these files securely.

## Development Setup 🛠️

1. Install development dependencies:

   ```bash
   pip install .[dev]
   ```

2. Run tests:

   ```bash
   pytest
   ```

### Integrating into Your Code 📦

To use CryptKeeper's functionality in your code, you can load and decrypt an existing credential file:

```python
from pathlib import Path
from cryptkeeper.crypt import load_credential

# Specify paths to the encrypted credential file and secret key
cred_file = Path("my_credentials.enc")
key_file = Path("my_secret.key")

# Load and decrypt credentials
try:
    credential = load_credential(cred_file, key_file)
    print(f"Decrypted Username: {credential.username}")
    print(f"Decrypted Password: {credential.password}")
except Exception as e:
    print(f"Failed to decrypt credentials: {e}")
```

### Adding CryptKeeper as a Dependency in `pyproject.toml` 📂

To use CryptKeeper in another project, add it as a dependency in your `pyproject.toml` file:

```toml
[project]
name = "your_project"
version = "0.1.0"
description = "Your project description"
requires-python = ">=3.8"

[project.dependencies]
cryptkeeper = { git = "https://github.com/GTKYCU-IT/cryptkeeper" }
```

Replace the repository URL with the actual URL of your CryptKeeper project.

## Contributing 🤝

Contributions are welcome! Please submit pull requests or file issues for any bugs or feature requests.

## License 📜

This project is licensed under the MIT License.

---

Let me know if you'd like additional sections or further customization!
