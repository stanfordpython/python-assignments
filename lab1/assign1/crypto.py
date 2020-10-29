"""Assignment 1: Cryptography for CS41 Winter 2020.

Name: <YOUR NAME>
SUNet: <SUNet ID>

Replace this placeholder text with a description of this module.
"""
import utils


#################
# CAESAR CIPHER #
#################

def encrypt_caesar(plaintext):
    if plaintext.upper() != plaintext:
        print("The text is not correctly formatted")
        #Ha szeretnek itt vissza is terithetnenk errort, de amikor implementaltam, akkor sajnos ugy csinaltam, hogy menjen kisbetukre is
    res = ''
    if (len(plaintext) == 0):
        return

    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    shift = 3
    
    for a in plaintext:
        loc = abc.find(a)
        if(loc == -1):
            res = res + a
            continue
        
        upr = 0
        if(a >= 'a' and a <= 'z'):
            upr = 26
       
        res = res + abc[(loc-upr + shift)%26 + upr]
    return res

def decrypt_caesar(ciphertext):
    if ciphertext.upper() != ciphertext:
        print("The text is not correctly formatted")
        #Ha szeretnek itt vissza is terithetnenk errort, de amikor implementaltam, akkor sajnos ugy csinaltam, hogy menjen kisbetukre is

    res = ''
    if (len(ciphertext) == 0):
        return

    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    shift = 3
    
    for a in ciphertext:
        loc = abc.find(a)
        if(loc == -1):
            res = res + a
            continue
        
        upr = 0
        if(a >= 'a' and a <= 'z'):
            upr = 26
       
        res = res + abc[(loc-upr - shift)%26 + upr]
    return res

###################
# VIGENERE CIPHER #
###################

def encrypt_vigenere(plaintext, keyword):
    if len(plaintext) < 1 or plaintext.upper() != plaintext or not plaintext.isalpha():
        print("The text is not correctly formatted")
        return -1
    
    if len(keyword) < 1 or keyword.upper() != keyword or not keyword.isalpha():
        print("The text is not correctly formatted")
        return -1
    """Encrypt plaintext using a Vigenere cipher with a keyword.

    Add more implementation details here.

    :param plaintext: The message to encrypt.
    :type plaintext: str
    :param keyword: The key of the Vigenere cipher.
    :type keyword: str

    :returns: The encrypted ciphertext.
    """
    keywordLength = len(keyword)

    encryptedText = ""

    j = 0
    for c in plaintext:
        if j == keywordLength:
            j = 0
        encryptedText += chr((ord(c) + ord(keyword[j]) - 130)%26 + 65)
        j = j+1
    return encryptedText


def decrypt_vigenere(ciphertext, keyword):
    if len(ciphertext) < 1 or ciphertext.upper() != ciphertext or not ciphertext.isalpha():
        print("The text is not correctly formatted")
        return -1

    if len(keyword) < 1 or keyword.upper() != keyword or not keyword.isalpha():
        print("The text is not correctly formatted")
        return -1


    """Decrypt ciphertext using a Vigenere cipher with a keyword.

    Add more implementation details here.

    :param ciphertext: The message to decrypt.
    :type ciphertext: str
    :param keyword: The key of the Vigenere cipher.
    :type keyword: str

    :returns: The decrypted plaintext.
    """
    keywordLength = len(keyword)

    decryptedText = ""

    j = 0
    for c in ciphertext:
        if j == keywordLength:
            j = 0
        decryptedText += chr((ord(c) - ord(keyword[j]) - 130)%26 + 65)
        j = j+1
    return decryptedText

###################
# SCYTALE CIPHER #
###################

def encrypt_scytale(plaintext, circumference):
    if len(plaintext) < 1 or circumference > len(plaintext):
        #Esetleg ha a circumference kisebb mint a szoveg hossza, akkor csak visszateriteni a szoveget
        print("Invalid  parameters")
        return -1
    ciphertext = ''
    length = len(plaintext)
    p = 0
    for i in range(length):
        ciphertext += plaintext[p]
        p += circumference
        if(p >= length):
            p = (i * circumference)/length + 1
    return ciphertext

def decrypt_scytale(ciphertext, circumference):
    if len(ciphertext) < 1 or circumference > len(ciphertext):
        #Esetleg ha a circumference kisebb mint a szoveg hossza, akkor csak visszateriteni a szoveget
        print("Invalid  parameters")
        return -1
    plaintext = ''
    length = len(ciphertext)
    cycle =  length/circumference
    remainder = length%circumference

    for i in range(cycle+1):
        for p in range(circumference):
            if len(plaintext) == length:
                break
            r = min(remainder, p)
            plaintext += ciphertext[p * cycle + r + i]

    return plaintext

###################
# RAIL FENCE CIPHER #
###################

import math as math

def encrypt_railfence(plaintext, num_rails):
    if len(plaintext) < 1 or num_rails > len(plaintext):
        #Esetleg ha a num_rails kisebb mint a szoveg hossza, akkor csak visszateriteni a szoveget
        print("Invalid  parameters")
        return -1
    ciphertext = ""
    length = len(plaintext)
    cycles = 2 * num_rails - 2
    characters = length / cycles

    for i in range(characters+1):
        ciphertext += plaintext[i* cycles]

    for i in range(1, num_rails-1):
        space1 = cycles - 2 * i
        space2 = cycles - 2 * (num_rails - i -1)
        for c in range(characters):
            ciphertext += plaintext[c * space1 + i + c * space2] + plaintext[c * space2 + (c+1) * space1 + i]

        if length % cycles != 0 and (characters * space1 + i + characters * space2) < length:
            ciphertext += plaintext[characters * space1 + i + characters * space2]

    for i in range(characters):
        ciphertext += plaintext[i * cycles + num_rails-1]
        
    if length % cycles != 0 and (characters * cycles + num_rails-1) < length:
        ciphertext += plaintext[characters * cycles + num_rails-1]

    return ciphertext


def decrypt_railfence(ciphertext, num_rails):
    if len(ciphertext) < 1 or num_rails > len(ciphertext):
        #Esetleg ha a num_rails kisebb mint a szoveg hossza, akkor csak visszateriteni a szoveget
        print("Invalid  parameters")
        return -1
    length = len(ciphertext)
    plaintext = list(['.' for i  in range(length-1)])
    cycles = 2 * num_rails - 2
    characters = length / cycles

    plaintext += ciphertext[0]

    curr = 0

    for i in range(characters+1):
        plaintext[i* cycles] = ciphertext[curr]
        curr = curr + 1

    for i in range(1, num_rails-1):
        space1 = cycles - 2 * i
        space2 = cycles - 2 * (num_rails - i -1)
        for c in range(characters):
            plaintext[c * space1 + i + (c) * space2] = ciphertext[curr]
            curr = curr + 1
            plaintext[(c) * space2 + (c+1) * space1 + i] =  ciphertext[curr]
            curr = curr + 1
        if length % cycles != 0 and (characters * space1 + i + characters * space2) < length:
            plaintext[characters * space1 + i + characters * space2] = ciphertext[curr]
            curr = curr + 1

    for i in range(characters):
        plaintext[i * cycles + num_rails-1] = ciphertext[curr]
        curr = curr + 1

    if length % cycles != 0 and (characters * cycles + num_rails-1) < length:
        plaintext[characters * cycles + num_rails-1] = ciphertext[curr]
        curr = curr + 1 
    
    return "".join(plaintext)

########################################
# MERKLE-HELLMAN KNAPSACK CRYPTOSYSTEM #
########################################

def generate_private_key(n=8):
    """Generate a private key to use with the Merkle-Hellman Knapsack Cryptosystem.

    Following the instructions in the handout, construct the private key
    components of the MH Cryptosystem. This consists of 3 tasks:

    1. Build a superincreasing sequence `w` of length n
        Note: You can double-check that a sequence is superincreasing by using:
            `utils.is_superincreasing(seq)`
    2. Choose some integer `q` greater than the sum of all elements in `w`
    3. Discover an integer `r` between 2 and q that is coprime to `q`
        Note: You can use `utils.coprime(r, q)` for this.

    You'll also need to use the random module's `randint` function, which you
    will have to import.

    Somehow, you'll have to return all three of these values from this function!
    Can we do that in Python?!

    :param n: Bitsize of message to send (defaults to 8)
    :type n: int

    :returns: 3-tuple private key `(w, q, r)`, with `w` a n-tuple, and q and r ints.
    """
    # Your implementation here.
    raise NotImplementedError('generate_private_key is not yet implemented!')

def create_public_key(private_key):
    """Create a public key corresponding to the given private key.

    To accomplish this, you only need to build and return `beta` as described in
    the handout.

        beta = (b_1, b_2, ..., b_n) where b_i = r × w_i mod q

    Hint: this can be written in one or two lines using list comprehensions.

    :param private_key: The private key created by generate_private_key.
    :type private_key: 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.

    :returns: n-tuple public key
    """
    # Your implementation here.
    raise NotImplementedError('create_public_key is not yet implemented!')


def encrypt_mh(message, public_key):
    """Encrypt an outgoing message using a public key.

    Following the outline of the handout, you will need to:
    1. Separate the message into chunks based on the size of the public key.
        In our case, that's the fixed value n = 8, corresponding to a single
        byte. In principle, we should work for any value of n, but we'll
        assert that it's fine to operate byte-by-byte.
    2. For each byte, determine its 8 bits (the `a_i`s). You can use
        `utils.byte_to_bits(byte)`.
    3. Encrypt the 8 message bits by computing
         c = sum of a_i * b_i for i = 1 to n
    4. Return a list of the encrypted ciphertexts for each chunk of the message.

    Hint: Think about using `zip` and other tools we've discussed in class.

    :param message: The message to be encrypted.
    :type message: bytes
    :param public_key: The public key of the message's recipient.
    :type public_key: n-tuple of ints

    :returns: Encrypted message bytes represented as a list of ints.
    """
    # Your implementation here.
    raise NotImplementedError('encrypt_mh is not yet implemented!')


def decrypt_mh(message, private_key):
    """Decrypt an incoming message using a private key.

    Following the outline of the handout, you will need to:
    1. Extract w, q, and r from the private key.
    2. Compute s, the modular inverse of r mod q, using the Extended Euclidean
        algorithm (implemented for you at `utils.modinv(r, q)`)
    3. For each byte-sized chunk, compute
         c' = cs (mod q)
    4. Solve the superincreasing subset sum problem using c' and w to recover
        the original plaintext byte.
    5. Reconstitute the decrypted bytes to form the original message.

    :param message: Encrypted message chunks.
    :type message: list of ints
    :param private_key: The private key of the recipient (you).
    :type private_key: 3-tuple of w, q, and r

    :returns: bytearray or str of decrypted characters
    """
    # Your implementation here.
    raise NotImplementedError('decrypt_mh is not yet implemented!')

