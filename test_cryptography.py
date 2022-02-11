from importlib.util import decode_source
from cryptography import encrypt, decrypt, crack
import pytest

def test_encrypt_with_lower_case_letters():
    assert encrypt("", 100) == ""
    assert encrypt("abc", 1) == "bcd"
    assert encrypt("abc", 10) == "klm"
    assert encrypt("abc", 27) == "bcd"
    assert encrypt("abc", 26) == "abc"
    assert encrypt("zzz", 1) == "aaa"
    assert encrypt("xyz", 29) == "abc"
    assert encrypt("x y z1", 29) == "a b c1"

def test_encrypt_with_upper_case_letter():
    assert encrypt("", 10) == ""
    assert encrypt("ABC", 1) == "BCD"
    assert encrypt("ABC", 10) == "KLM"
    assert encrypt("ABC", 27) == "BCD"
    assert encrypt("ABC", 26) == "ABC"
    assert encrypt("ZZZ", 1) == "AAA"
    assert encrypt("XYZ", 29) == "ABC"
    assert encrypt("X Y Z1", 29) == "A B C1"

def test_encrypt_with_mixed_case_letters():
    assert encrypt("", 50) == ""
    assert encrypt("AaBbCc", 1) == "BbCcDd"
    assert encrypt("AaBbCc", 10) == "KkLlMm"
    assert encrypt("AaBbCc", 27) == "BbCcDd"
    assert encrypt("AaBbCc", 26) == "AaBbCc"
    assert encrypt("ZzZzZz", 1) == "AaAaAa"
    assert encrypt("XxYyZz", 29) == "AaBbCc"
    assert encrypt("Xx Yy Zz11", 29) == "Aa Bb Cc11"

def test_decrypt_with_lower_case_letters():
    assert decrypt("", 100) == ""
    assert decrypt("bcd", 1) == "abc"
    assert decrypt("klm", 10) == "abc"
    assert decrypt("bcd", 27) == "abc"
    assert decrypt("abc", 26) == "abc"
    assert decrypt("aaa", 1) == "zzz"
    assert decrypt("abc", 29) == "xyz"
    assert decrypt("a b c1", 29) == "x y z1"

def test_decrypt_with_upper_case_letter():
    assert decrypt("", 10) == ""
    assert decrypt("BCD", 1) == "ABC"
    assert decrypt("KLM", 10) == "ABC"
    assert decrypt("BCD", 27) == "ABC"
    assert decrypt("ABC", 26) == "ABC"
    assert decrypt("AAA", 1) == "ZZZ"
    assert decrypt("ABC", 29) == "XYZ"
    assert decrypt("A B C1", 29) == "X Y Z1"

def test_decrypt_with_mixed_case_letters():
    assert decrypt("", 50) == ""
    assert decrypt("BbCcDd", 1) == "AaBbCc"
    assert decrypt("KkLlMm", 10) == "AaBbCc"
    assert decrypt("BbCcDd", 27) == "AaBbCc"
    assert decrypt("AaBbCc", 26) == "AaBbCc"
    assert decrypt("AaAaAa", 1) == "ZzZzZz"
    assert decrypt("AaBbCc", 29) == "XxYyZz"
    assert decrypt("Aa Bb Cc11", 29) == "Xx Yy Zz11"