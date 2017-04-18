# Assignment 1: Cryptography
**Due: 11:59:59 PM, Thursday April 27th**

## Overview
In this assignment, you will build a cryptography suite that implements three different cryptosystems - Caesar cipher, Vigenere cipher, and the Merkle-Hellman Knapsack Cryptosystem. This handout will walk you through the details of building this text-based cryptography tool. We want to instill good Pythonic practices from the beginning - so we encourage you to think critically about writing clean Python code.

*Expected Time: 6 hours (if it takes much longer than that, email us)*

Note: Get started early! Merkle-Hellman is the hardest cipher to implement.

## Review

Get a quick refresher by flipping through our slides from the first few weeks on [the course website](http://stanfordpython.com)

## Starter Files

We’ve provided starter files available on the website as a skeleton for this assignment. Here’s an overview of what’s in it:

1. `crypto.py` is the primary file you will modify. It will implement all the functions to decrypt/encrypt strings.
2. `utils.py` provides useful utilities for console interaction and for Merkle-Hellman
3. `crypto-console.py` runs an interactive console that lets you test your cryptography functions.
2. `design.txt` is where you'll record the design decisions you're making.
3. `feedback.txt` is where you'll answer some questions about how the course is going overall
4. `tests/` folder contains test input and output
5. `res/` folder of sample text files to play around with file I/O. For Merkle-Hellman, the seed we used was 41

```
res/caesar-plain.txt   and res/caesar-cipher.txt
res/vigenere-plain.txt and res/vigenere-cipher.txt
res/mh-plain.txt       and res/mh-cipher.txt
```

# Cryptography Suite

## Building the Ciphers
In this section, you will build cipher functions to encrypt and decrypt messages. We'll give a brief overview of each cipher and give some pointers on how it fits it into the starter files.

### Caesar Cipher

A Caesar cipher involves shifting each character in a plaintext by three letters forward:

```
A -> D, B -> E, C -> F, etc... 
```

At the end of the alphabet, the cipher mapping wraps around the end, so:

```
X -> A, Y -> B, Z -> C.
```

For example, encrypting `'PYTHON'` using a Caesar cipher gives

```
PYTHON
||||||
SBWKRQ
```

For this part, implement the functions:

```
encrypt_caesar(plaintext)
decrypt_caesar(ciphertext)
```

Notes:

- You can assume that the plaintext/ciphertext will always have length greater than zero.
- You can assume that all alphabetic characters will be in uppercase.
- If you encounter a non-alphabetic character, do not modify it.


You should test your ciphers using the interactive interpreter:

```
(cs41) $ python3 -iq crypto.py
>>> encrypt_caesar("PYTHON")
"SBWKRQ"
>>> decrypt_caesar("SBWKRQ")
"PYTHON"
```

A non-exhaustive list of test cases, represented by a tab-delimited (plaintext, ciphertext) pair are given in the text file `tests/caesar-tests.txt`.

### Vigenere Cipher

A Vigenere cipher is very similar to a Caesar cipher; however, in a Vigenere cipher, every character in the plaintext could be shifted by a different amount. The amount of shift is determined by a keyword, where 'A' corresponds to shift of 0 (no shift), 'B' corresponds to a shift of 1, ..., and 'Z' corresponds to a shift of 25. 

The keyword is repeated or truncated as necessary to fit the length of the plaintext. As an example, encrypting `"ATTACKATDAWN"` with the key `"LEMON"` gives:

```
Plaintext:		ATTACKATDAWN
Key:			LEMONLEMONLE
Ciphertext:	    LXFOPVEFRNHR
```

Looking more closely, each letter in the ciphertext is the sum of the letters in the plaintext and the key. Thus, the first character of ciphertext is L due to the following calculations:

```
A + L = 0 + 11 = 11 -> L
```

It may be useful to use the functions ord and chr which convert strings of length one to and from, respectively, their ASCII numerical equivalents.

Implement the methods:

```
encrypt_vigenere(plaintext, keyword)
decrypt_vigenere(ciphertext, keyword)
```

Notes:

- You can assume that there will be no non-alphabetic characters in the plaintext, ciphertext, or keyword.
- You can assume that all of the characters will be in uppercase.
- You can assume that plaintext/ciphertext/keyword will always have at least one character in it.

Then, try testing the methods using the interactive interpreter again.

```
(cs41) $ python3 -iq crypto.py
>>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
"LXFOPVEFRNHR"
>>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
"ATTACKATDAWN"
```

Another list of non-exhaustive tests are available at `tests/vigenere-tests.txt`.

### Merkle-Hellman Knapsack Cryptosystem

Public-key cryptography is essential to modern society. You may have heard of RSA - one of the most popular public-key cryptosystems. Less well known, however, is the Merkle-Hellman Knapsack Cryptosystem, one of the earliest public-key cryptosystems (invented in 1978!), which relies on the NP-complete subset sum problem. Although it has been broken, it illustrates several important concepts in public-key cryptography and gives you lots of practice with Pythonic constructs.

Building the Merkle-Hellman Cryptosystem involves three parts:

1. Key Generation
2. Encryption
3. Decryption

At a high-level, in the Merkle-Hellman Knapsack Cryptosystem, all participants go through key generation once to construct both a public key and a private key, linked together in some mathematical way. Public keys are made publicly available, whereas private keys are kept under lock and key (no pun intended). Usually, public keys will lead to some sort of encryption function, and private keys will lead to some sort of decryption function, and in many ways they act as inverses.

For Person A to send message m to Person B, Person A encrypts message m using Person B's public key. Person B then decrypts the encrypted message using Person B's private key. Often, long messages are send in shorted chunks, with each chunk respectively encrypted before it is sent to the recipient.

Make sure you understand the general idea behind public-key cryptosystems before moving forward. You don't need to know all of the details, but you should be able to explain why Person A doesn't encrypt an outgoing message with her own public key.

First, we'll discuss the mathematics behind Merkle-Hellman Knapsack Cryptosystem, and then we'll dive into what functions you have to write for this assignment.


#### Key Generation
In the key generation step, we will construct a private key and a public key.

Choose a fixed integer `n` for the chunk size (in bits) of messages to send. For this assignment, we'll use `n = 8` bits, so we can encrypt and decrypt messages one byte at a time.

First, we must build a superincreasing sequence of `n` nonzero natural numbers:

```
w = (w_1, w_2, ..., w_n)
```

A superincreasing sequence is one in which every element is greater than the sum of all previous elements. For example, `(1, 3, 6, 13, 27, 52)` is a superincreasing sequence, but `(1, 3, 4, 9, 15, 25)` is not. One way to construct a superincreasing sequence is to start with some small number - say, a random number between 2 and 10. You can generate the next number by selecting randomly from a range like `[total + 1, 2 * total]` or something similar, where `total` is the sum of all of the elements so far. In this way, we can gradually build up our sequence to whatever size we need - in this case, until `n = 8`.

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

Both `w` and `beta` should be converted to tuples.

*Implementation Note:*

To find random integers, you can use the `randint(a, b)` function (returns a random integer in the range [a, b], including both end points) from the `random` module. For example,

```
import random
x = random.randint(1, 6)  # returns either 1, 2, 3, 4, 5, 6 with uniform probability

```

#### Encryption

To encrypt a character, first convert it into it's equivalent bits. For example, `'A'`, which is 65 in ASCII, becomes `[0, 1, 0, 0, 0, 0, 0, 1]`.

To encrypt this character, we just have to encrypt an 8-bit message. Call it:

```
alpha = (a_1, a_2, ..., a_n)
```

where `a_i` is the `i`-th bit of the message and `a_i` is either 0 or 1. With that, we can calculate

```
c = sum of a_i × b_i for i = 1 to n
```

The ciphertext is then `c`.

*Implementation Note:*

Whenever you're encrypting or decrypting data using Merkle-Hellman, you'll want to deal with bits. Fortunately, the `utils` module exports the `bits_to_byte(bits)` and `byte_to_bits(byte)` functions which respectively convert an array of length 8 containing 1s and 0s to an integer between 0-255 (conceptually, a byte).

#### Decryption

In order to decrypt a ciphertext `c`, a receiver has to find the message bits `alpha_i` such that they satisfy

```
c = sum of a_i × b_i for i = 1 to n
```

This is generally a hard problem, if the `b_i` are random values, because the receiver would have to solve an instance of the subset sum problem, which is known to be NP-hard (i.e. very hard). However, we constructed `beta` in a very special way, such that if we *also* know the private key `(w, q, r)`, then we can decrypt the message more easily.

The key to decryption will be a special integer `s` that has some nice properties - namely, that `s` is the modular inverse of `r` modulo `q`. That means `s` satisfies the equation `r × s mod q = 1`, and since `r` was chosen such that `gcd(r, q) = 1`, it will always be possible to find such an `s` using something called the Extended Euclidean algorithm, which we've implemented for you (in `utils.modinv(r, q)`). It's a really cool algorithm! If you're interested, go read about it on Wikipedia.

Once `s` is known, the receiver of the ciphertext computes

```
c' = cs mod(q)
```

Because we know `r × s mod q = 1` and `b_i = r × w_i (mod q)`, it's also true that

```
b_i s =  w_i × r × s = w_i (mod q).
```

Therefore,

```
c' = c × s = sum of a_i × b_i × s for each i = a_i × w_i (mod q).
```

Wow! We've converted our problem of solving a subset sum problem over the `b_i`s, which might be a very nasty sequence, to an equivalent problem over the `w_i`s, which form a very nice sequence.

Thus the receiver has to solve the subset sum problem

```
c' = sum of a_i × w_i for i = 1 to n
```

This problem is computationally easy because `w` was chosen to be a superincreasing sequence! Take the largest element in `w`, say `w_k`. If `w_k > c'` , then `a_k = 0`, and if `w_k  <= c'`, then `a_k = 1`. Then, subtract `w_k × a_k` from `c'` , and repeat these steps until you have figured out all of `alpha`.

Still confused? This stuff can get complicated. Wikipedia provides [a great example](https://en.wikipedia.org/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem#Example) to work through if you prefer concrete numbers over abstract symbols.

#### Implementation

What do you actually have to implement? We've taken care of a lot of the math behind-the-scenes (if you want to check out how, look into `utils.py`), so you're job focuses more on the data structures. In particular, you need to write the following four functions.

```
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
```

Note: We're aware this is a hard problem. It's supposed to challenge you! If you're stuck, even on something that *seems* simple, please please reach out to the course staff over Piazza or during office hours. We'll be more than happy to help!

*Full credit to the Wikipedia summary for this explanation! The description is shamelessly copied and modified :)*
## Console Menu
In order to better test this program, we've provided a console menu to interact with the cryptography suite. This shouldn't replace your normal debugging process - rather, view it as an augmentation of the tools you have to track down any elusive bugs.

In general, we don't do very much error handling (since the console menu is intended as a tool for you to debug), so it may crash gracelessly on bad input. You're welcome to modify or change the console menu as you see fit. We'll only be testing your application-level functions.

A sample run of the program might look like:

```
(cs41) $ python3 crypto-console.py
Welcome to the Cryptography Suite!
----------------------------------
* Tool *
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
* Tool *
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
(cs41) $ 
```


## Extensions

What?! You still haven't had enough? Okay, your call.

The following section contains possible extensions and is **entirely optional**. If you choose to take a crack at any, regardless of how far you get, let us know how it went in your feedback!

### Scytale Cipher
*Difficulty: &#127798; &#127798;*

The scytale was used as far back as the [Spartans](http://www.australianscience.com.au/technology/a-scytale-cryptography-of-the-ancient-sparta/), and is one example of ancient cryptography (thought to be used in military campaigns). The [Wikipedia page](https://en.wikipedia.org/wiki/Scytale) has a good overview.

Below is a sample encryption of the plaintext "IAMHURTVERYBADLYHELP" using a scytale cipher with circumference 5 to generate the ciphertext "IRYYATBHMVAEHEDLURLP"

We write the message diagonally down (around) the scytale, and then 

```
I . . . . R . . . . Y . . . . Y . . . .
. A . . . . T . . . . B . . . . H . . .
. . M . . . . V . . . . A . . . . E . .
. . . H . . . . E . . . . D . . . . L .
. . . . U . . . . R . . . . L . . . . P
```

The ciphertext is obtained by reading from left to right, top to bottom. In this example, the ciphertext is

```
IRYYATBHMVAEHEDLURLP
```

Implement the functions:

```
encrypt_scytale(plaintext, circumference)
decrypt_scytale(ciphertext, circumference)
```

What will you do when the length of the message is not a perfect multiple of the circumference?

Consider using list comprehensions and slice syntax to simplify your implementation.

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

```
encrypt_railfence(plaintext, num_rails)
decrypt_railfence(ciphertext, num_rails)
```

How will you handle the cases where the last ascending (or descending) segment doesn't reach a corner?

Consider using list comprehensions and slice syntax (especially assigning into slices) to simplify your implementation.

Want more of a challenge (&#127798; &#127798; &#127798; &#127798;)? Try to decrypt an arbitrary ciphertext without knowing the number of rails used.

### Intelligent Codebreaker
*Difficulty: &#127798; &#127798; &#127798;*

Suppose that you have access to some ciphertext that you know has been encrypted using a Vigenere cipher. Furthermore, suppose that you know that the corresponding plaintext has been written using only words in `/usr/share/dict/words`, whitespace, and punctuation, although you don’t know the exact message. Finally, suppose that you know that someone has encrypted a message using a Vigenere cipher with a key drawn from a preset list of words, (again, let's suppose from `/usr/share/dict/words`). Can you still decrypt the ciphertext?

For many of the incorrect keys, the resulting plaintext will be gibberish, but there will also be incorrect keys for which the resulting plaintext sounds English-y, but isn't quite right. Thus, the bulk of this problem lies in evaluating how close to a valid English sentence a given sequence of letters is.

Your top-level function should be

```
decrypt_vigenere(ciphertext, possible_keys)
```

Besides that, you are free to implement this program however you see fit. However, think about the Python style guidelines before continuing.

You can test your method on the text inside of `secret_message.txt`.

For more of a challenge (&#127798; &#127798; &#127798; &#127798;), broaden your definition of English-y to allow finding plaintexts in which not all words come from `/usr/share/dict/words` (a message we're interested in decrypting, for example, might contain a person's name). What other signals in the text can you look for?

You can also try to break Vigenere encryptions using a combination of the above tactic and a frequency attack for a given key-length.

### Error Handling
*Difficulty: &#127798;*

Currently, our library functions (`encrypt_*` and `decrypt_*`) maks a lot of strong assumptions about the input - see the Notes section in each part. Can you add code to handle cases where these assumptions are violated?

### Encrypt Non-Text Files
*Difficulty: &#127798; &#127798;*

So far, our ciphers have been applied solely to text-based messages full of ascii letters from the alphabet. However, it is possible to extend these encryption methods to work on arbitrary binary data, such as images, audio files, and more. For this extension, choose at least one of the encryption techniques and make it work on binary files. You will need to use the binary flag when reading from files. You may want to read about text sequence types compared with binary sequence types as well.

### Cracking Merkle-Hellman
*Difficulty: &#127798; &#127798; &#127798; &#127798; &#127798;*

Unfortunately, there is a polynomial-time algorithm for breaking the Merkle-Hellman Knapsack Cryptosystem. Implement it.

The algorithm's details are described in [Shamir's 1984 paper](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.123.5840&rep=rep1&type=pdf).

## Design

Please submit a short design document (`design.txt`) describing your approach to each of the parts of the assignment. "Short" means just a few sentences (1-3) per part discussing the rationale behind your decision to implement this program in the way you did. Consider answering the following questions:

1. What data structures did you use to handle transformation of data?
2. What Pythonic ideas or strategies did you incorporate in your approach, if any? 

## Feedback

We hope you have been enjoying the course so far, and would love to hear from you about how this first real assignment went!

To help us out, please answer the following questions in the `feedback.txt` file provided with the starter code:

1. How long did this assignment take you to complete?
2. What has been the best part of the class so far?
3. What can we do to make this class more enjoyable for you?

Thank you for being our guinea pigs this quarter - we're learning from you as well as we teach this course!

## Grading

Your grade will be assessed on both functionality and style.

Functionality will be determined entirely by your program's correctness on a suite of unit tests (some of which are provided with the starter code).

Stylistically, you will be evaluated on your general program design (a la 106 series: decomposition, logic, etc) as well as your Python-specific style. In particular, we will be looking for "Pythonic" approaches to solving problems, as opposed to "non-Pythonic" solutions, that emphasize the Zen of Python. We will also be looking at your Python syntax and mechanics. We encourage you to format your code in accordance with [Python style guidelines](https://www.python.org/dev/peps/pep-0008/). You can find a tool to help format your code [online](http://pep8online.com/). If you have any questions, please don't hesitate to let us know. Think about the [Zen of Python](https://www.python.org/dev/peps/pep-0020/) when making design decisions. 

## Deliverables

1. Your modified `crypto.py`
2. The `design.txt` file documenting your design decisions
3. The `feedback.txt` letting us know how we're doing!

## Submitting

See the [submission instructions](https://github.com/stanfordpython/python-handouts/blob/master/submitting-assignments.md) on the course website.

For assignment 1, the key ideas are:

```
$ ssh <sunetid>@myth.stanford.edu "mkdir -p ~/cs41/assign1"
$ scp -r <path/to/assign1> <sunetid>@myth.stanford.edu:~/cs41/assign1/
$ ssh <sunetid>@myth.stanford.edu
<... connect to myth ...>
myth$ cd ~/cs41/assign1/
myth$ /usr/class/cs41/tools/submit
```

## Credit
*Sherman Leung (@skleung), Python Tutorial, Learn Python the Hard Way, Google Python, MIT OCW 6.189, Project Euler, and Wikipedia's list of ciphers.*

> With <3 by @sredmond 
