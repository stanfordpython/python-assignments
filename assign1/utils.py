"""Mathematical utilities for CS41's Assignment 1: Cryptography."""
import fractions


class Error(Exception):
    """Base class for exceptions in this module."""


class BinaryConversionError(Error):
    """Custom exception for invalid binary conversions."""


def is_superincreasing(seq):
    """Return whether a given sequence is superincreasing.

    Usage::

        is_superincreasing([1, 1, 1, 1, 1])  # => False
        is_superincreasing([1, 2, 4, 8, 16])  # => True

    :param seq: The iterable to check.
    """
    ct = 0  # Total so far
    for n in seq:
        if n <= ct:
            return False
        ct += n
    return True


def modinv(a, b):
    """Return the modular inverse of a mod b.

    Pre: a < b and gcd(a, b) = 1

    Adapted from https://en.wikibooks.org/wiki/Algorithm_Implementation/
    Mathematics/Extended_Euclidean_algorithm#Python
    """
    saved = b
    x, y, u, v = 0, 1, 1, 0
    while a:
        q, r = b // a, b % a
        m, n = x - u*q, y - v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    return x % saved


def coprime(a, b):
    """Returns True iff `gcd(a, b) == 1`, i.e. iff `a` and `b` are coprime"""
    return fractions.gcd(a, b) == 1


def byte_to_bits(byte):
    if not 0 <= byte <= 255:
        raise BinaryConversionError(byte)

    out = []
    for i in range(8):
        out.append(byte & 1)
        byte >>= 1
    return out[::-1]


def bits_to_byte(bits):
    if not all(bit in (0, 1) for bit in bits):
        raise BinaryConversionError("Invalid bitstring passed")

    byte = 0
    for bit in bits:
        byte *= 2
        if bit:
            byte += 1
    return byte
