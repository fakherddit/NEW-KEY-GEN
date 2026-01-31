# NEW-KEY-GEN

A simple yet powerful key generation utility for creating random keys with various formats and character sets.

## Features

- Multiple character sets: alphanumeric, alphabetic, numeric, hexadecimal, base64, and symbols
- Customizable key length
- Optional chunking with separators (e.g., `XXXXX-XXXXX-XXXXX`)
- Generate multiple keys at once
- Cryptographically secure random generation using Python's `secrets` module

## Installation

No installation required! Just clone the repository and run the script:

```bash
git clone https://github.com/fakherddit/NEW-KEY-GEN.git
cd NEW-KEY-GEN
```

## Usage

### Basic Examples

Generate a default 32-character alphanumeric key:
```bash
python3 keygen.py
```

Generate a 64-character key:
```bash
python3 keygen.py -l 64
```

Generate a hexadecimal key:
```bash
python3 keygen.py -c hex
```

Generate a key with dashes every 5 characters:
```bash
python3 keygen.py -l 20 -s - -k 5
```

Generate 5 keys at once:
```bash
python3 keygen.py -n 5
```

### Command-Line Options

```
-l, --length LENGTH       Length of the key (default: 32)
-c, --charset CHARSET     Character set to use (default: alphanumeric)
                          Options: alphanumeric, alpha, numeric, hex, base64, symbols
-s, --separator SEP       Separator character for chunking (e.g., "-" or " ")
-k, --chunk-size SIZE     Size of chunks when using separator (default: 0, no chunking)
-n, --count COUNT         Number of keys to generate (default: 1)
```

## Testing

Run the test suite:
```bash
python3 test_keygen.py
```

Or with verbose output:
```bash
python3 test_keygen.py -v
```

## Examples

### API Keys
```bash
python3 keygen.py -l 40 -c alphanumeric
```

### License Keys
```bash
python3 keygen.py -l 25 -s - -k 5
```

### Hex Tokens
```bash
python3 keygen.py -l 32 -c hex
```

### Passwords
```bash
python3 keygen.py -l 20 -c symbols
```

## Security

This tool uses Python's `secrets` module, which is designed for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.

## License

This project is open source and available for use.