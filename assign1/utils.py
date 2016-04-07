#!/usr/bin/env python3 -tt
import random

class BinaryConversionException(Exception):
    """Custom exception for invalid binary conversions"""
    pass

def is_superincreasing(seq):
    """Returns True iff `seq` is a superincreasing sequence"""
    ct = 0  # Total so far
    for n in seq:
        if n <= ct:
            return False
        ct += n
    return True


def modinv(a, b):
    """Returns the modular inverse of a mod b.

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
    while b:
        a, b = b, a % b
    return a == 1


def byte_to_bits(byte):
    if not 0 <= byte <= 255:
        raise BinaryConversionException()

    out = []
    for i in range(8):
        out.append(byte & 1)
        byte >>= 1
    return out[::-1]


def bits_to_byte(bits):
    if not all(bit == 0 or bit == 1 for bit in bits):
        raise BinaryConversionException("Invalid bitstring passed")

    byte = 0
    for bit in bits:
        byte *= 2
        if bit:
            byte += 1
    return byte

#####################
# CONSOLE UTILITIES #
#####################


def get_tool():
    print("* Tool *")
    return _get_selection("(C)aesar, (V)igenere or (M)erkle-Hellman? ", "CVM")


def get_action():
    """Return true iff encrypt"""
    print("* Action *")
    return _get_selection("(E)ncrypt or (D)ecrypt? ", "ED")


def get_filename():
    filename = input("Filename? ")
    while not filename:
        filename = input("Filename? ")
    return filename


def get_input(binary=False):
    print("* Input *")
    choice = _get_selection("(F)ile or (S)tring? ", "FS")
    if choice == 'S':
        text = input("Enter a string: ").strip().upper()
        while not text:
            text = input("Enter a string: ").strip().upper()
        if binary:
            return bytes(text, encoding='utf8')
        return text
    else:
        filename = get_filename()
        flags = 'r'
        if binary:
            flags += 'b'
        with open(filename, flags) as infile:
            return infile.read()


def set_output(output, binary=False):
    print("* Output *")
    choice = _get_selection("(F)ile or (S)tring? ", "FS")
    if choice == 'S':
        print(output)
    else:
        filename = get_filename()
        flags = 'w'
        if binary:
            flags += 'b'
        with open(filename, flags) as outfile:
            print("Writing data to {}...".format(filename))
            outfile.write(output)


def _get_selection(prompt, options):

    choice = input(prompt).upper()
    while not choice or choice[0] not in options:
        choice = input("Please enter one of {}. {}".format('/'.join(options), prompt)).upper()
    return choice[0]


def get_yes_or_no(prompt, reprompt=None):
    """
    Asks the user whether they would like to continue.
    Responses that begin with a `Y` return True. (case-insensitively)
    Responses that begin with a `N` return False. (case-insensitively)
    All other responses (including '') cause a reprompt.
    """
    if not reprompt:
        reprompt = prompt

    choice = input("{} (Y/N) ".format(prompt)).upper()
    while not choice or choice[0] not in ['Y', 'N']:
        choice = input("Please enter either 'Y' or 'N'. {} (Y/N)? ".format(reprompt)).upper()
    return choice[0] == 'Y'
