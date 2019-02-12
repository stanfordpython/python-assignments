"""Mathematical utilities for CS41's Assignment 1: Cryptography."""
import math


class Error(Exception):
    """Base class for exceptions in this module."""


class BinaryConversionError(Error):
    """Custom exception for invalid binary conversions."""


class NotCoprimeError(Error):
    """Custom exception for arguments that are not coprime but need to be."""


def is_superincreasing(seq):
    """Return whether a given sequence is superincreasing.

    A sequence is superincreasing if each element is greater than the sum of
    all elements before it.

    Usage::

        is_superincreasing([1, 1, 1, 1, 1])  # => False
        is_superincreasing([1, 3, 4, 9, 15, 90])  # => False
        is_superincreasing([1, 2, 4, 8, 16])  # => True

    :param seq: The iterable to check.
    :returns: Whether this sequence is superincreasing.
    """
    total = 0  # Total so far
    for n in seq:
        if n <= total:
            return False
        total += n
    return True


def modinv(a, b):
    """Return the modular inverse of a mod b.

    The returned value s satisfies a * s == 1 (mod b).

    As a precondition, a should be less than b and a and b must be coprime.
    Errors are raised if these conditions do not hold.

    Adapted from https://en.wikibooks.org/wiki/Algorithm_Implementation/
    Mathematics/Extended_Euclidean_algorithm#Python

    :param a: Value whose modular inverse to find.
    :param b: The modulus.

    :raises: ValueError if a >= b.
    :raises: NotCoprimeError if a and b are not coprime.

    :returns: The modular inverse of a mod b.
    """
    if a >= b:
        raise ValueError("First argument to modinv must be less than the second argument.")
    if not coprime(a, b):
        raise NotCoprimeError("Mathematically impossible to find modular inverse of non-coprime values.")

    # Actually find the modular inverse.
    saved = b
    x, y, u, v = 0, 1, 1, 0
    while a:
        q, r = b // a, b % a
        m, n = x - u*q, y - v*q
        # Tuple packing and unpacking can be useful!
        b, a, x, y, u, v = a, r, u, v, m, n
    return x % saved


def coprime(a, b):
    """Return whether a and b are coprime.

    Two numbers are coprime if and only if their greater common divisor is 1.

    Usage::

        print(coprime(5, 8))  # => True (5 and 8 have no common divisors)
        print(coprime(6, 9))  # => False (6 and 9 are both divisible by 3)
    """
    return math.gcd(a, b) == 1


def byte_to_bits(byte):
    """Convert a byte to an tuple of 8 bits for use in Merkle-Hellman.

    The first element of the returned tuple is the most significant bit.

    Usage::
        byte_to_bits(65)  # => [0, 1, 0, 0, 0, 0, 0, 1]
        byte_to_bits(b'ABC'[0])  # => [0, 1, 0, 0, 0, 0, 0, 1]
        byte_to_bits('A')  # => raises TypeError

    :param byte: The byte to convert.
    :type byte: int between 0 and 255, inclusive.

    :raises: BinaryConversionError if byte is not in [0, 255].
    :returns: An 8-tuple of bits representing this byte's value.
    """
    if not 0 <= byte <= 255:
        raise BinaryConversionError(byte)

    out = []
    for i in range(8):
        out.append(byte & 1)
        byte >>= 1
    return tuple(out[::-1])


def bits_to_byte(bits):
    """Convert a tuple of 8 bits into a byte for use in Merkle-Hellman.

    The first element of the returned tuple is assumed to be the most significant bit.

    :param bits: collection of 0s and 1s representing a bit string.
    :type bits: tuple

    :raises: BinaryConversionError if the supplied tuple isn't all 0s and 1s.
    :returns: A converted byte value for this bit tuple.
    """
    if not all(bit in (0, 1) for bit in bits):
        raise BinaryConversionError("Encountered non-bits in bit tuple.")

    byte = 0
    for bit in bits:
        byte *= 2
        if bit:
            byte += 1
    return byte
