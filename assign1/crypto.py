#!/usr/bin/env python3 -tt
"""
File: crypto.py
---------------
Assignment 1: Cryptography
Course: CS 41
Name: <YOUR NAME>
SUNet: <SUNet ID>

Replace this with a description of the program.
"""
import random

import utils
"""
Caesar Cipher
"""

def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.
    Add more implementation details here.
    """
    pass  # Your implementation here


def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.
    Add more implementation details here.
    """
    pass  # Your implementation here


"""
Vigenere Cipher
"""

def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher with a keyword.
    Add more implementation details here.
    """
    pass  # Your implementation here


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts ciphertext using a Vigenere cipher with a keyword.
    Add more implementation details here.
    """
    pass  # Your implementation here


"""
Merkle-Hellman Knapsack Cryptosystem
"""

def generate_private_key(n=8):
    """Generate a private key for use in the Merkle-Hellman Knapsack Cryptosystem

    Following the instructions in the handout, construct the private key components
    of the MH Cryptosystem. This consistutes 3 tasks:

    1. Build a superincreasing sequence `w` of length n
        (Note: you can check if a sequence is superincreasing with `utils.is_superincreasing(seq)`)
    2. Choose some integer `q` greater than the sum of all elements in `w`
    3. Discover an integer `r` between 2 and q that is coprime to `q` (you can use utils.coprime)

    You'll need to use the random module for this function, which has been imported already

    Somehow, you'll have to return all of these values out of this function! Can we do that in Python?!

    @param n bitsize of message to send (default 8)
    @type n int

    @return 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.
    """
    pass

def create_public_key(private_key):
    """Creates a public key corresponding to the given private key.

    To accomplish this, you only need to build and return `beta` as described in the handout.

        beta = (b_1, b_2, ..., b_n) where b_i = r × w_i mod q

    Hint: this can be written in one line using a list comprehension

    @param private_key The private key
    @type private_key 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.

    @return n-tuple public key
    """
    pass


def encrypt_mh(message, public_key):
    """Encrypt an outgoing message using a public key.

    1. Separate the message into chunks the size of the public key (in our case, fixed at 8)
    2. For each byte, determine the 8 bits (the `a_i`s) using `utils.byte_to_bits`
    3. Encrypt the 8 message bits by computing
         c = sum of a_i * b_i for i = 1 to n
    4. Return a list of the encrypted ciphertexts for each chunk in the message

    Hint: think about using `zip` at some point

    @param message The message to be encrypted
    @type message bytes
    @param public_key The public key of the desired recipient
    @type public_key n-tuple of ints

    @return list of ints representing encrypted bytes
    """
    return message

def decrypt_mh(message, private_key):
    """Decrypt an incoming message using a private key

    1. Extract w, q, and r from the private key
    2. Compute s, the modular inverse of r mod q, using the
        Extended Euclidean algorithm (implemented at `utils.modinv(r, q)`)
    3. For each byte-sized chunk, compute
         c' = cs (mod q)
    4. Solve the superincreasing subset sum using c' and w to recover the original byte
    5. Reconsitite the encrypted bytes to get the original message back

    @param message Encrypted message chunks
    @type message list of ints
    @param private_key The private key of the recipient
    @type private_key 3-tuple of w, q, and r

    @return bytearray or str of decrypted characters
    """
    return message


#########################################################
#            IMPLEMENTATION OF CONSOLE MENU             #
# You shouldn't need to change anything below this box. #
#########################################################

def clean_caesar(text):
    """Convert text to a form compatible with the preconditions imposed by Caesar cipher"""
    return text.upper()

def clean_vigenere(text):
    return ''.join(ch for ch in text.upper() if ch.isupper())

def run_caesar():
    action = utils.get_action()
    encrypting = action == 'E'
    data = clean_caesar(utils.get_input(binary=False))

    print("* Transform *")
    print("{}crypting {} using Caesar cipher...".format('En' if encrypting else 'De', data))

    output = (encrypt_caesar if encrypting else decrypt_caesar)(data)

    utils.set_output(output)


def run_vigenere():
    action = utils.get_action()
    encrypting = action == 'E'
    data = clean_vigenere(utils.get_input(binary=False))

    print("* Transform *")
    keyword = clean_vigenere(input("Keyword? "))

    print("{}crypting {} using Vigenere cipher and keyword {}...".format('En' if encrypting else 'De', data, keyword))

    output = (encrypt_vigenere if encrypting else decrypt_vigenere)(data, keyword)

    utils.set_output(output)


def run_merkle_hellman():
    action = utils.get_action()

    print("* Seed *")
    seed = input("Set Seed [enter for random]: ")
    import random
    random.seed(seed)
    print("* Building private key...")

    private_key = generate_private_key()
    public_key = create_public_key(private_key)

    if action == 'E':  # Encrypt
        data = utils.get_input(binary=True)
        print("* Transform *")
        chunks = encrypt_mh(data, public_key)
        output = ' '.join(map(str, chunks))
    else:  # Decrypt
        data = utils.get_input(binary=False)
        chunks = [int(line.strip()) for line in data.split() if line.strip()]
        print("* Transform *")
        output = decrypt_mh(chunks, private_key)

    utils.set_output(output)


def run_suite():
    """
    Runs a single iteration of the cryptography suite.

    Asks the user for input text from a string or file, whether to encrypt
    or decrypt, what tool to use, and where to show the output.
    """
    print('-' * 34)
    tool = utils.get_tool()
    # This isn't the cleanest way to implement functional control flow,
    # but I thought it was too cool to not sneak in here!
    commands = {
        'C': run_caesar,         # Caesar Cipher
        'V': run_vigenere,       # Vigenere Cipher
        'M': run_merkle_hellman  # Merkle-Hellman Knapsack Cryptosystem
    }
    commands[tool]()


def main():
    """Harness for CS41 Assignment 1"""
    print("Welcome to the Cryptography Suite!")
    run_suite()
    while utils.get_yes_or_no("Again?"):
        run_suite()
    print("Goodbye!")


if __name__ == '__main__':
    main()
