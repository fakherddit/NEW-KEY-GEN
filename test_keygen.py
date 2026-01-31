#!/usr/bin/env python3
"""
Tests for the NEW-KEY-GEN key generator.
"""

import unittest
import string
from keygen import generate_key


class TestKeyGen(unittest.TestCase):
    """Test cases for key generation functionality."""
    
    def test_default_length(self):
        """Test that default key length is 32 characters."""
        key = generate_key()
        self.assertEqual(len(key), 32)
    
    def test_custom_length(self):
        """Test generating keys with custom lengths."""
        for length in [8, 16, 32, 64, 128]:
            key = generate_key(length=length)
            self.assertEqual(len(key), length)
    
    def test_alphanumeric_charset(self):
        """Test that alphanumeric keys only contain valid characters."""
        key = generate_key(length=100, charset='alphanumeric')
        valid_chars = set(string.ascii_letters + string.digits)
        self.assertTrue(all(c in valid_chars for c in key))
    
    def test_alpha_charset(self):
        """Test that alphabetic keys only contain letters."""
        key = generate_key(length=100, charset='alpha')
        valid_chars = set(string.ascii_letters)
        self.assertTrue(all(c in valid_chars for c in key))
    
    def test_numeric_charset(self):
        """Test that numeric keys only contain digits."""
        key = generate_key(length=100, charset='numeric')
        valid_chars = set(string.digits)
        self.assertTrue(all(c in valid_chars for c in key))
    
    def test_hex_charset(self):
        """Test that hex keys only contain hexadecimal characters."""
        key = generate_key(length=100, charset='hex')
        valid_chars = set(string.hexdigits.lower()[:16])
        self.assertTrue(all(c in valid_chars for c in key))
    
    def test_chunking_with_separator(self):
        """Test key chunking with separator."""
        key = generate_key(length=20, separator='-', chunk_size=5)
        # Should have 4 chunks separated by 3 dashes
        self.assertEqual(key.count('-'), 3)
        chunks = key.split('-')
        self.assertEqual(len(chunks), 4)
        for chunk in chunks:
            self.assertEqual(len(chunk), 5)
    
    def test_no_separator_without_chunk_size(self):
        """Test that separator is not applied without chunk size."""
        key = generate_key(length=20, separator='-', chunk_size=0)
        self.assertNotIn('-', key)
        self.assertEqual(len(key), 20)
    
    def test_invalid_charset(self):
        """Test that invalid charset raises ValueError."""
        with self.assertRaises(ValueError):
            generate_key(charset='invalid')
    
    def test_randomness(self):
        """Test that generated keys are different (randomness check)."""
        keys = [generate_key() for _ in range(10)]
        # All keys should be unique
        self.assertEqual(len(keys), len(set(keys)))


if __name__ == '__main__':
    unittest.main()
