#!/usr/bin/python3.4 -tt
import sys
import os
import pathlib
import random
sys.path.append(os.getcwd()) # Ugh its so gross never do this

try:
    import crypto
except ImportError:
    print("Error! Can't find the crypto module. Make sure that you're in the right directory")
    raise

CWD = pathlib.Path.cwd()
BASE_DIR = pathlib.Path('/afs/ir/class/cs41/repos/python-assignments/assign1/')
CAESAR_TESTS = BASE_DIR / 'tests' / 'caesar-tests.txt'
VIGENERE_TESTS = BASE_DIR / 'tests' / 'vigenere-tests.txt'


def test_caesar(encrypt_fn, decrypt_fn):
    with open(str(CAESAR_TESTS), 'r') as f:
        lines = [line.upper().strip("\r\n") for line in f.readlines()]

    tests = [line.upper().split(sep='\t', maxsplit=1) for line in lines if not line.startswith('#')]
    for plain, cipher in tests:
        plain_student, cipher_student = decrypt_fn(cipher), encrypt_fn(plain)
        if cipher_student != cipher:
            print("Incorrect encryption of '{}': was '{}', should be '{}'".format(plain, cipher_student, cipher))
            break
        if plain_student != plain:
            print("Incorrect decryption of '{}': was '{}', should be '{}'".format(cipher, plain_student, plain))
            break
    else:
        print("Caesar tests complete.")


def test_vigenere(encrypt_fn, decrypt_fn):
    with open(str(VIGENERE_TESTS), 'r') as f:
        lines = [line.upper().strip("\r\n") for line in f.readlines()]

    tests = [line.upper().split(sep='\t', maxsplit=2) for line in lines if not line.startswith('#')]
    for plain, key, cipher in tests:
        plain_student, cipher_student = decrypt_fn(cipher, key), encrypt_fn(plain, key)
        if cipher_student != cipher:
            print("Incorrect encryption of '{}' with '{}': was '{}', should be '{}'".format(plain, key, cipher_student, cipher))
            break
        if plain_student != plain:
            print("Incorrect decryption of '{}' with '{}': was '{}', should be '{}'".format(cipher, key, plain_student, plain))
            break
    else:
        print("Vigenere tests complete.")


def test_merkle_hellman(private_key_gen, public_key_gen, encrypt_fn, decrypt_fn):
    lengths = [1,1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,9,9,9,10,20,50,100,200]
    print("Ascii Tests")
    for i in range(100):
        random.seed()
        private_key = private_key_gen()
        public_key = public_key_gen(private_key)
        for j in range(100):
            length = random.choice(lengths)
            plaintext = bytes(random.sample(range(32, 127), length))
            chunks = encrypt_fn(plaintext, public_key)
            decrypted = decrypt_fn(chunks, private_key)
            if plaintext != decrypted:
                print("Decrypting encrypted text failed (private_key={}, public_key = {}): Started with {}, ended with {}".format(private_key, public_key, plaintext, decrypted))
                break
    print("General binary tests")
    for i in range(100):
        random.seed()
        private_key = private_key_gen()
        public_key = public_key_gen(private_key)
        for j in range(100):
            length = random.choice(lengths)
            plaintext = bytes(random.sample(range(32, 127), length))
            chunks = encrypt_fn(plaintext, public_key)
            decrypted = decrypt_fn(chunks, private_key)
            if plaintext != decrypted:
                print("Decrypting encrypted text failed (private_key={}, public_key = {}): Started with {}, ended with {}".format(private_key, public_key, plaintext, decrypted))
                break
    print("Done!")


if __name__ == '__main__':
    print("Testing Caesar...")
    test_caesar(crypto.encrypt_caesar, crypto.decrypt_caesar)
    print("Done!")
    print("Testing Vigenere...")
    test_vigenere(crypto.encrypt_vigenere, crypto.decrypt_vigenere)
    print("Done!")
    print("Fuzz-testing Merkle-Hellman")
    print("Done!")
