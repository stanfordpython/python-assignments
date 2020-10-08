# Assignment 1: Cryptography
**Due: Midnight, Tuesday of Week 5 (Febuary 4, 2020)**

## Overview
In this assignment, you will build a cryptography suite that implements two or three different cryptosystems - Caesar cipher, Vigenere cipher, and (optionally) the Merkle-Hellman Knapsack Cryptosystem. This handout will walk you through the details of building this text-based cryptography tool. We want to instill good Pythonic practices from the beginning - so we encourage you to think critically about writing clean Python code.

* *Expected Time: 3 hours, 6 hours with Merkle-Hellman*
* *Max Time: 6 hours; higher if you complete an extension*

Note: It's always a good idea to get started early, in case you run into unexpected difficulties down the line. Merkle-Hellman is a hard cipher to implement.

## Review

Get a quick refresher by flipping through our slides from the first few weeks on [the course website](https://stanfordpython.com).

## Starter Files

We've provided starter files available on the website as a skeleton for this assignment. Here's an overview of what's in it:

1. `crypto.py` is the primary file you will modify. It will implement all the functions to decrypt/encrypt strings.
2. `utils.py` provides some helper functions for the Merkle-Hellman cryptosystem.
3. `crypto-console.py` runs an interactive console that lets you test your cryptography functions.
4. `design.txt` is where you'll record some design decisions you're making.
5. `tests/` folder contains test input and output
6. `res/` folder of sample text files to play around with file I/O. For Merkle-Hellman, we used the random seed 41 to generate these values.

The files in the `res/` folder come in pairs and correspond to plaintext and ciphertext pairs.

```
res/caesar-plain.txt   and res/caesar-cipher.txt
res/vigenere-plain.txt and res/vigenere-cipher.txt
res/mh-plain.txt       and res/mh-cipher.txt
```

# Cryptography Suite
## General Tips

You'll be modifying a lot of strings in this assignment. The `string` module exports some useful values:

```
>>> import string
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
```

## Building the Ciphers
In this section, you will build cipher functions to encrypt and decrypt messages. We'll give a brief overview of each cipher and give some pointers on how it fits it into the starter files.

### Caesar Cipher

A Caesar cipher involves shifting each character in a plaintext by **three** letters forward (note that the shift can be anything between zero and 25, but we're just going to implement the three-shift cipher):

```
A -> D, B -> E, C -> F, etc... 
```

At the end of the alphabet, the cipher mapping wraps around the end, so:

```
..., X -> A, Y -> B, Z -> C.
```

For example, encrypting `'PYTHON'` using a Caesar cipher gives

```
PYTHON
||||||
SBWKRQ
```

In this part, implement the functions:

```Python
encrypt_caesar(plaintext)
decrypt_caesar(ciphertext)
```

Each of these functions takes one argument, a string representing a message to be encrypted or decrypted, and returns a string representing the encrypted or decrypted message.

Notes:

- Non-alphabetic characters should not be modified by encryption or decryption.
- You may assume that all alphabetic characters will be in uppercase.
- Do not assume that the arguments to this function always have at least one character.

That is, `encrypt_caesar("")` should return `""` (the empty string) and `encrypt_caesar("F1RST P0ST")` should return `"I1UVW S0VW"` (where the letters have been encrypted by the numbers, and the space, have been left unchanged).

There are two ways to test your ciphers.

Your primary method of debugging should be using the interactive interpreter:

```
(cs41-env) $ ipython -i crypto.py
In [1]: encrypt_caesar("PYTHON")
"SBWKRQ"
In [2]:decrypt_caesar("SBWKRQ")
"PYTHON"
```

A non-exhaustive list of test cases, represented by a tab-delimited (plaintext, ciphertext) pair are given in the text file `tests/caesar-tests.txt`. You can use this file to sanity check your implementation.

**Questions to Ponder:**

- What sort of data structure can be used to represent an association of input characters to (encrypted) output characters? 
- How can we make one of these data structures efficiently? 
- How can we use it to transform an input message?

For this part of the assignment, try not to use the `ord` and `chr` functions.

### Vigenere Cipher

A Vigenere cipher is similar in nature to a Caesar cipher. However, in a Vigenere cipher, every character in the plaintext can be shifted by a variable amount. The amount to shift any letter in the plaintext is determined by a keyword, where 'A' corresponds to shift of 0 (no shift), 'B' corresponds to a shift of 1, ..., and 'Z' corresponds to a shift of 25, wrapping around if necessary (as with the Caesar cipher).

The keyword is repeated or truncated as necessary to fit the length of the plaintext. As an example, encrypting `"ATTACKATDAWN"` with the key `"LEMON"` gives:

```
Plaintext:		ATTACKATDAWN
Key:			LEMONLEMONLE
Ciphertext:	 	LXFOPVEFRNHR
```

Looking more closely, each letter in the ciphertext is the sum of the letters in the plaintext and the key. Thus, the first character of ciphertext is `"L"` because of the following calculations:

```
A + L = 0 + 11 = 11 -> L
```

The second character of the ciphertext is `"X"` because shifting `"T"` by 4 (associated to shifting by `"E"`) gives:

```
T + E = 19 + 4 = 23 -> X
```

Note that, since we're considering A to encode 0, our indices are one off of a letter's ordinal position in the alphabet. That is, even though E is the 5th letter of the alphabet, it encodes a shift of 4.

The third character of the ciphertext is `"F"` because:

```
T + M = 19 + 12 = 31 -> 5 -> F
```

We have wrapped around the alphabet from +31 to +5, resulting in an output ciphertext character of `"F"`.

Implement the functions:

```Python
encrypt_vigenere(plaintext, keyword)
decrypt_vigenere(ciphertext, keyword)
```

These functions take two arguments, a message to encrypt (or decrypt) and a keyword to use for encryption or decryption. Both functions should return the encrypted (or decrypted) message.

Notes:

- You can assume that all characters in the plaintext, ciphertext, and keyword will be alphabetic (i.e no spaces, numbers, or punctuation).	
- You can assume that all of the characters will be provided in uppercase.
- You can assume that keyword will have at least one letter in it.

After you've implemented these functions, you can test them using the interactive interpreter.

```
(cs41-env)$ ipython -i crypto.py
In [1]: encrypt_vigenere("ATTACKATDAWN", "LEMON")
"LXFOPVEFRNHR"
In [2]: decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
"ATTACKATDAWN"
```
Another list of non-exhaustive tests are available at `tests/vigenere-tests.txt`.

**Questions to Ponder:**

- How can you cycle through the letters of the keyword? Consider looking at functions exported by the `itertools` module.
- What concepts from class can we employ to make this code more elegant?

You can use the functions `ord` and `chr` which convert strings of length one to and from their ASCII numerical equivalents. For example, `ord('A') == 65`, `ord('B') == 66`, ..., `ord('Z') == 90`, and `chr(65) == 'A'`, `chr(66) == 'B'`, ..., `chr(90) == 'Z'`. For an extra challenge, try to implement these functions purely functionally.

Intrigued? Take a look in `not_a_secret_message.txt`. One possible extension is to try to decrypt this message (or any encrypted message!) despite not knowing what the key is. For this encryption, ignore non-alphabetic characters entirely. In particular, non-alphabetic characters do not use up any of the characters from the key. For example:

```
  ATTACK AT DAWN!
+ LEMONL EM ONLE
-----------------
  LXFOPV EF RNHR!
```


## Console Menu

To help you test your implementation, we've provided a console menu to interact with the cryptography functions you're building. This shouldn't replace your normal debugging process - rather, view it as an augmentation of the tools you have that you can use to track down any elusive bugs.

In general, this console doesn't do very much error handling (since it's just intended as a debugging tool), so it may crash gracelessly when given bad input. You're welcome to modify or change the console menu as you see fit. We'll only be grading the functions in the `crypto` module, so make sure that you don't change the interface if you modify the console code.

After implementing some of the functions, a sample run of the console might look like:

```
(cs41-env) $ python3 crypto-console.py
Welcome to the Cryptography Suite!
----------------------------------
* Cryptosystem *
(C)aesar, (V)igenere or (M)erkle-Hellman? c
* Action *
(E)ncrypt or (D)ecrypt? e
* Input *
(F)ile or (S)tring? s
Enter a string: hello!
* Transform *
Encrypting HELLO! using Caesar cipher...
* Output *
(F)ile or (S)tring? s
"KHOOR"
Again? (Y/N) y
----------------------------------
* Cryptosystem *
(C)aesar, (V)igenere or (M)erkle-Hellman? v
* Action *
(E)ncrypt or (D)ecrypt? d
* Input *
(F)ile or (S)tring? f
Filename? res/vigenere-cipher.txt
* Transform *
Keyword? LEMON
Decrypting LXFOPVEFRNHR using Vigenere cipher and keyword LEMON...
* Output *
(F)ile or (S)tring? s
"ATTACKATDAWN"
Again? (Y/N) n
Goodbye!
(cs41-env) $ 
```

## Design

Please submit a short design document (`design.txt`) describing your approach to each of the parts of the assignment. "Short" means just a few sentences (1-3) per part discussing the rationale behind your decision to implement this program in the way you did. Consider answering the following questions:

1. What data structures did you use to handle transformation of data?
2. What Pythonic ideas or strategies did you incorporate in your approach, if any?

Again, by "short" we really mean that you shouldn't take more than, say, fifteen minutes filling out this document.

## Grading

Your grade will be assessed on both functionality and style.

Functionality will be determined entirely by your program's correctness on a suite of unit tests (some of which are provided with the starter code).

Stylistically, you will be evaluated on your general program design (a la 106 series: decomposition, logic, naming, spacing) as well as your Python-specific style. In particular, we will be looking for "Pythonic" approaches to solving problems, as opposed to "non-Pythonic" solutions, that emphasize the Zen of Python. We will also be looking at your Python syntax and mechanics.

**We encourage you to format your code in accordance with [Python style guidelines](https://www.python.org/dev/peps/pep-0008/).**

You can find a tool to help format your code [online](http://pep8online.com/). If you have any questions, please don't hesitate to let us know. Think about the [Zen of Python](https://www.python.org/dev/peps/pep-0020/) when making design decisions. 

## Submitting

Submit the following files:

1. Your modified `crypto.py`
2. The `design.txt` file documenting your design decisions

See the [submission instructions](https://github.com/stanfordpython/python-handouts/blob/master/submitting-assignments.md) on the course website.

## Merkle-Hellman Knapsack Cryptosystem (optional)

Public-key cryptography is essential to modern society. You may have heard of RSA - one of the most popular public-key cryptosystems. Less well known, however, is the Merkle-Hellman Knapsack Cryptosystem, one of the earliest public-key cryptosystems (invented in 1978!), which relies on the NP-complete subset sum problem. Although it has been since been broken, it illustrates several important concepts in public-key cryptography and gives you lots of practice with the Pythonic constructs we've discussed in this class.

Building the Merkle-Hellman Cryptosystem involves three parts:

1. Key Generation
2. Encryption
3. Decryption

At a high-level, in the Merkle-Hellman Knapsack Cryptosystem, all participants go through key generation once to construct both a public key and a private key, linked together in some mathematical way. Public keys are made publicly available, whereas private keys are kept under lock and key (no pun intended). Usually, encryption functions are derived from the public keys, and decryption functions are derived from the private keys, so in some sense they act as inverses.

For Person A to send a message `m` to Person B, Person A encrypts message `m` using Person B's public-key-derived encryption function. Person A can then send the encrypted message to Person B over an insecure channel. Person B then decrypts the encrypted message using Person B's private-key-derived decryption function, which only Person B knows. Often, long messages are send in shorted chunks, with each chunk respectively encrypted before it is sent to the recipient.

Make sure you understand the general idea behind public-key cryptosystems before moving forward. You don't need to know all of the details, but you should be able to explain why Person A doesn't encrypt an outgoing message with her own public key.

First, we'll discuss the mathematics behind Merkle-Hellman Knapsack Cryptosystem, and then we'll dive into what functions you have to write for this assignment.


#### Key Generation
In the key generation step, we will construct a private key and a public key.

Choose a fixed integer `n` for the chunk size (in bits) of messages to send. For this assignment, we'll use `n = 8` bits, so we can encrypt and decrypt messages one byte at a time.

First, we must build a superincreasing sequence of `n` nonzero natural numbers:

```
w = (w_1, w_2, ..., w_n)
```

A superincreasing sequence is one in which every element is greater than the sum of all previous elements. For example, `(1, 3, 6, 13, 27, 52)` is a superincreasing sequence, but `(1, 3, 4, 9, 15, 25)` is not, because `1 + 3 + 4 + 9 = 16 > 15`. One way to construct a superincreasing sequence is to start with some small number - say, a random number between 2 and 10. You can generate the next number by selecting randomly from a range something like `[total + 1, 2 * total]`, where `total` is the sum of all of the elements so far. In this way, we can iteratively build up as large a superincreasing sequence as we need - in this case, until we have `n = 8` elements.

Next, we pick a random integer `q`, such that `q` is greater than the sum of the the elements in `w`. To leverage code we've already written, let's choose `q` between `[total + 1, 2 * total]`, where `total` is the sum over all elements of `w`. 

Then, we choose a random integer `r` such that `gcd(r, q) = 1` (i.e. r and q are coprime). To accomplish this, it's sufficient to just generate random numbers in the range `[2, q-1]` until you find some `r` such that `r` and `q` are coprime. (Hint: the `utils` module exports a convenient `coprime` function. Use it!)

Finally, we calculate the tuple

```
beta = (b_1, b_2, ..., b_n)
```

where

```
b_i = r × w_i mod q
```

The public key is `beta`, while the private key is `(w, q, r)`.

Both `w` and `beta` should be represented as tuples, since they are fixed-size and immutable.

*Implementation Note:*

To find random integers, you can use the `randint(a, b)` function (returns a random integer in the range [a, b], including both end points) from the `random` module. For example,

```
import random
x = random.randint(1, 6)  # Returns either 1, 2, 3, 4, 5, 6 with uniform probability.
```

#### Encryption

We will encrypt a message one character (byte) at a time.

To encrypt a character, first convert it into an equivalent array of bits. For example, the character `'A'` has an ASCII value of 65, which can be written in binary as `01000001`. We will represent this as the 8-element array `[0, 1, 0, 0, 0, 0, 0, 1]`. If there are leading zeros in the binary representation, we need to make sure that we generate an 8-element array as shown above, with leading zeros as necessary.

Encrypting this character is now equivalent to encrypting an 8-bit message. Define

```
alpha = (a_1, a_2, ..., a_n)
```

where `a_i` is the `i`-th bit of the message and `a_i` is either 0 or 1. In our example able, `a_1 == 0` and `a_8 == 1`. Next, we calculate:

```
c = sum of a_i × b_i for i = 1 to n
```

We then output `c` as the encryption of our character. Note that `c` is an integer, possibly much larger than 255.

The encryption of a long message is an array of these `c`s.

*Implementation Note:*

Whenever you're encrypting or decrypting data using Merkle-Hellman, you'll want to deal with bits. Fortunately, the `utils` module exports a `bits_to_byte(bits)` and `byte_to_bits(byte)` functions which respectively convert a tuple of length 8 containing 1s and 0s to an integer between 0-255 (conceptually, a byte).

#### Decryption

In order to decrypt a ciphertext `c` and recover a single character, a receiver would have to determine the message bits `a_i` such that they satisfy

```
c = sum of a_i × b_i for i = 1 to n
```

This is generally a hard problem, if the `b_i` are random values, because the receiver would have to solve an instance of the subset sum problem, which is known to be NP-hard (i.e. very hard). However, we constructed `beta` in a very special way, such that if we *also* know the private key `(w, q, r)`, then we can decrypt the message more easily using mathematical magic.

The key to decryption will be a special integer `s` that has some nice properties - namely, that `s` is the modular inverse of `r` modulo `q`. That means `s` satisfies the equation `r × s mod q = 1`, and since `r` was chosen such that `gcd(r, q) = 1`, it will always be possible to find such an `s` using something called the Extended Euclidean algorithm, which we've implemented for you (in `utils.modinv(r, q)`). It's a really cool algorithm! If you're interested, Wikipedia has a [nice summary](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm).

Once `s` is determined, the receiver of the ciphertext computes

```
c' = cs mod(q)
```

for each ciphertext piece `c`. Because we know `r × s mod q = 1` and `b_i = r × w_i (mod q)`, it's also true that

```
b_i s =  w_i × r × s = w_i (mod q).
```

Therefore,

```
c' = c × s = sum of a_i × b_i × s for each i = a_i × w_i (mod q).
```

Wow! We've converted our problem of solving a subset sum problem over the `b_i`s, which might be a very nasty sequence, to an equivalent problem over the `w_i`s, which form a very nice sequence. In particular, recall that the `w_i`s form a superincreasing sequence!

Therefore, the receiver has to solve the subset sum problem:

```
c' = sum of a_i × w_i for i = 1 to n
```

This problem is computationally easy because `w` was chosen to be a superincreasing sequence! Take the largest element in `w`, say `w_k`. If `w_k > c'` , then `a_k = 0`, and if `w_k  <= c'`, then `a_k = 1`. Then, subtract `w_k × a_k` from `c'` , and repeat these steps, iterating backwards, until you have recovered all of `alpha`.

Still confused? This stuff can get complicated. Wikipedia provides [a great example](https://en.wikipedia.org/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem#Example) to work through if you prefer concrete numbers over abstract symbols.

#### Implementation

What do you actually have to implement? We've taken care of a lot of the math behind-the-scenes (if you want to check out how, look into `utils.py`), so your job focuses more on the data structures and Pythonic constructs. In particular, you need to write the following four functions.

```Python
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
```

The astute reader might notice that the input parameter to encrypt_mh is actually a message of type `bytes`, which is a standard type we haven't seen before. The [standard library](https://docs.python.org/3/library/stdtypes.html#bytes) provides the best documentation for `bytes`, but the short version is that a `bytes` object behaves like an immutable sequence of integers, with each value in the sequence restricted such that 0 <= x < 256. A `bytes` object can be declared (for testing) by prefixing a string literal with a `b`. That is, `x = b"ABC"` assigns a `bytes` object with three elements to the variable `x`, and `x[0]` is not the length-one string `'A'` as you might expect, but rather the number `65`, which corresponds to the ASCII value of `'A'`.

If this seems like a hard problem, that's because it is! If you get stuck, even on something that *feels* like it should be simple, please reach out to the course staff over Piazza. We're more than happy to help!

*Lots of credit to the Wikipedia summary for this explanation! Much of this description is shamelessly copied and modified :)*

## Extensions

What?! You still haven't had enough? Okay, your call.

The following section contains possible extensions and is **entirely optional**. If you choose to take a crack at any, regardless of how far you get, let us know how it went in your feedback!

We've added &#127798; guidelines so you can gauge how hard a given extension might be. For calibration, the Merkle-Hellman cryptosystem, given our helper functions and overview, would be rated as &#127798; &#127798;.

### Scytale Cipher
*Difficulty: &#127798; &#127798;*

The scytale was used as far back as the [Spartans](http://www.australianscience.com.au/technology/a-scytale-cryptography-of-the-ancient-sparta/), and is one example of ancient cryptography thought to be used in military campaigns. The [Wikipedia page](https://en.wikipedia.org/wiki/Scytale) has a good overview.

Below is a sample encryption of the plaintext "IAMHURTVERYBADLYHELP" using a scytale cipher with circumference 5 to generate the ciphertext "IRYYATBHMVAEHEDLURLP"

We write the message diagonally down (around) the scytale, like so:

```
I . . . . R . . . . Y . . . . Y . . . .
. A . . . . T . . . . B . . . . H . . .
. . M . . . . V . . . . A . . . . E . .
. . . H . . . . E . . . . D . . . . L .
. . . . U . . . . R . . . . L . . . . P
```

The ciphertext is then obtained by reading from left to right, top to bottom. In this example, the ciphertext is

```
IRYYATBHMVAEHEDLURLP
```

Implement the functions:

```Python
encrypt_scytale(plaintext, circumference)
decrypt_scytale(ciphertext, circumference)
```

What should you do when the length of the message is not a perfect multiple of the circumference?

Consider using list comprehensions and the slice syntax to simplify your implementation.

Want more of a challenge (&#127798; &#127798; &#127798;)? Try to decrypt an arbitrary ciphertext without knowing the circumference of the scytale.


### Railfence Cipher
*Difficulty: &#127798; &#127798; &#127798;*

Below is a sample encryption of the plaintext "WEAREDISCOVEREDFLEEATONCE" using a railfence with 3 rails to generate the ciphertext "WECRLTEERDSOEEFEAOCAIVDEN"

We write the message diagonally 

```
W . . . E . . . C . . . R . . . L . . . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . A . . . I . . . V . . . D . . . E . . . N . .
```

The ciphertext is obtained by reading the rails from left to right, top to bottom.

```
WECRLTEERDSOEEFEAOCAIVDEN
```

Implement the functions:

```Python
encrypt_railfence(plaintext, num_rails)
decrypt_railfence(ciphertext, num_rails)
```

How will you handle the cases where the last ascending (or descending) segment doesn't reach a corner?

Consider using list comprehensions and slice syntax (especially assigning into slices) to simplify your implementation.

Want more of a challenge (&#127798; &#127798; &#127798; &#127798;)? Try to decrypt an arbitrary ciphertext without knowing the number of rails used.

### Intelligent Codebreaker
*Difficulty: &#127798; &#127798; &#127798;*

Suppose that you have access to some ciphertext that you know has been encrypted using a Vigenere cipher. Furthermore, suppose that you know that the corresponding plaintext has been written using only words in `/usr/share/dict/words`, whitespace, and punctuation, although you don't know the exact message. Finally, suppose that you know that someone has encrypted a message using a Vigenere cipher with a key drawn from a preset list of words, (again, let's suppose from `/usr/share/dict/words`). Can you still decrypt the ciphertext?

For many of the incorrect keys, the resulting plaintext will be gibberish, but there will also be incorrect keys for which the resulting plaintext sounds English-y, but isn't quite right. Thus, the bulk of this problem lies in evaluating how close to a valid English sentence a given sequence of letters is.

Your top-level function should be

```Python
codebreak_vigenere(ciphertext, possible_keys)
```

Besides that, you are free to implement this program however you see fit. However, think about the Python style guidelines before continuing.

You can test your method on the text inside of `not_a_secret_message.txt`.

For more of a challenge (&#127798; &#127798; &#127798; &#127798;), broaden your definition of English-y to allow finding plaintexts in which not all words come from `/usr/share/dict/words` (a message we're interested in decrypting, for example, might contain a person's name), or perhaps where the not all possible keys come from some known list. What other signals in the text can you look for? When is a decrypted message English-y enough?

You can also try to break Vigenere encryptions by combining the above tactic with a frequency attack for a given key length.

### Error Handling
*Difficulty: &#127798;*

Currently, our library functions (`encrypt_*` and `decrypt_*`) maks a lot of strong assumptions about the input - see the Notes section in each part. Can you add code to handle cases where these assumptions are violated? Specifically, handle the cases where inputs contain non-alphabetic characters, possibly-lowercased. For more of a challenge, also try to handle unicode strings.

### Encrypt Non-Text Files
*Difficulty: &#127798; &#127798;*

So far, our ciphers have been applied solely to text-based messages full of ascii letters from the alphabet. However, it is possible to extend these encryption methods to work on arbitrary binary data, such as images, audio files, and more. For this extension, choose at least one of the encryption techniques and make it work for arbitrary binary files. You will need to use the binary flag when reading from files. You may want to read even more about the `bytes` type.

### Cracking Merkle-Hellman
*Difficulty: &#127798; &#127798; &#127798; &#127798; &#127798;*

There is a polynomial-time algorithm for cracking the Merkle-Hellman Knapsack Cryptosystem. Implement it.

The algorithm's details are described in [Shamir's 1984 paper](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.123.5840&rep=rep1&type=pdf).

What's perhaps more suprising is the fact that subset-sum is NP-hard, but there is a deterministic polynomial time algorithm to break the Merkle-Hellman Knapsack Cryptosystem, which is based on subset-sum.

## Credit
Much of this handout was shamelessly copied from Sam Redmond's version of this handout, that was used in prior iterations of CS41.

*Sam Redmond (@sredmond), Sherman Leung (@skleung), Python Tutorial, Learn Python the Hard Way, Google Python, MIT OCW 6.189, Project Euler, and Wikipedia's list of ciphers.*

> With &#129412; by @psarin and @coopermj 
