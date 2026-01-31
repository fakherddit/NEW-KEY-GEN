#!/usr/bin/env python3
"""
NEW-KEY-GEN: A simple yet powerful key generation utility.
Generates random keys with various formats and character sets.
"""

import argparse
import secrets
import string
import sys


def generate_key(length=32, charset='alphanumeric', separator='', chunk_size=0):
    """
    Generate a random key with specified parameters.
    
    Args:
        length: Length of the key to generate
        charset: Character set to use ('alphanumeric', 'alpha', 'numeric', 'hex', 'base64')
        separator: Separator character to use between chunks
        chunk_size: Size of chunks (0 means no chunking)
    
    Returns:
        Generated key as a string
    """
    # Define character sets
    charsets = {
        'alphanumeric': string.ascii_letters + string.digits,
        'alpha': string.ascii_letters,
        'numeric': string.digits,
        'hex': '0123456789abcdef',
        'base64': string.ascii_letters + string.digits + '+/',
        'symbols': string.ascii_letters + string.digits + string.punctuation,
    }
    
    if charset not in charsets:
        raise ValueError(f"Invalid charset. Choose from: {', '.join(charsets.keys())}")
    
    chars = charsets[charset]
    
    # Generate the key
    key = ''.join(secrets.choice(chars) for _ in range(length))
    
    # Apply chunking if requested
    if chunk_size > 0 and separator:
        chunks = [key[i:i+chunk_size] for i in range(0, len(key), chunk_size)]
        key = separator.join(chunks)
    
    return key


def main():
    """Main entry point for the key generator."""
    parser = argparse.ArgumentParser(
        description='NEW-KEY-GEN: Generate random keys with various formats',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                          # Generate default 32-char alphanumeric key
  %(prog)s -l 64                    # Generate 64-character key
  %(prog)s -c hex                   # Generate hexadecimal key
  %(prog)s -l 16 -c alpha           # Generate 16-character alphabetic key
  %(prog)s -l 20 -s - -k 5          # Generate key with dashes every 5 chars
  %(prog)s -n 5                     # Generate 5 keys at once
        """
    )
    
    parser.add_argument(
        '-l', '--length',
        type=int,
        default=32,
        help='Length of the key (default: 32)'
    )
    
    parser.add_argument(
        '-c', '--charset',
        choices=['alphanumeric', 'alpha', 'numeric', 'hex', 'base64', 'symbols'],
        default='alphanumeric',
        help='Character set to use (default: alphanumeric)'
    )
    
    parser.add_argument(
        '-s', '--separator',
        type=str,
        default='',
        help='Separator character for chunking (e.g., "-" or " ")'
    )
    
    parser.add_argument(
        '-k', '--chunk-size',
        type=int,
        default=0,
        help='Size of chunks when using separator (default: 0, no chunking)'
    )
    
    parser.add_argument(
        '-n', '--count',
        type=int,
        default=1,
        help='Number of keys to generate (default: 1)'
    )
    
    args = parser.parse_args()
    
    try:
        for i in range(args.count):
            key = generate_key(
                length=args.length,
                charset=args.charset,
                separator=args.separator,
                chunk_size=args.chunk_size
            )
            print(key)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        sys.exit(130)


if __name__ == '__main__':
    main()
