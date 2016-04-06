# Assignment 1: Cryptography
**Due: 11:59:59 PM, Wed April 13th**

## Overview
In this assignment, you will build a cryptography suite that implements three different cryptosystems - Caesar cipher, Vigenere cipher, and the Merkle-Hellman Knapsack Cryptosystem. This handout will walk you through the details of building this text-based cryptography tool. We want to instill good Pythonic practices from the beginning - so we encourage you to think critically about writing clean Python code.

*Expected Time: 6 hours (if it takes much longer than that, email us)*

Note: Get started early! Merkle-Hellman is by *far* the hardest of the ciphers.

## Review

Get a quick refresher by flipping through our slides from the first few weeks on [the course website](http://stanfordpython.com)

## Starter Files

We’ve provided a starter zip file available on the website as a skeleton for this assignment. Here’s an overview of what’s in it:

1. `crypto.py` is the primary file you will modify. It will contain all the functions to decrypt/encrypt strings and also the logic behind the text-based console menu.
2. `feedback.txt`
See the second-to-last section for some questions we’d love to ask you
3. Sample text files to test the File I/O 
`caesar-plain.txt`, `caesar-cipher.txt`, `vigenere-plain.txt`, `vigenere-cipher.txt`, `railfence-plain.txt`, `railfence-cipher.txt`
4. Tests


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

A non-exhaustive list of test cases, represented by a tab-delimited (plaintext, ciphertext) pair are given in the text file `caesar-tests.txt`.

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

Another list of non-exhaustive tests are available at `vigenere-tests.txt`.

### Merkle-Hellman Knapsack Cryptosystem

Public-key cryptography is essential to modern society. You may have heard of RSA - one of the most popular public-key cryptosystems. Less well known, however, is the Merkle-Hellman Knapsack Cryptosystem, one of the earliest public-key cryptosystems (invented in 1978!), which relies on the NP-complete subset sum problem. Although it has been broken, it illustrates several important concepts in public-key cryptography and gives you lots of practice with Pythonic constructs.

Building the Merkle-Hellman Cryptosystem involves three parts:

1. Key Generation
2. Encryption
3. Decryption

At a high-level, in the Merkle-Hellman Cryptosystem, all participants go through key generation once to build a public key and a private key. Public keys are made publicly available, whereas private keys are kept under lock and key. Usually, public keys lead to some sort of encryption function, and private keys lead to some sort of decryption function, and in many ways they act as inverses.

For Person A to send message m to Person B, Person A encrypts message m using Person B's public key. Person B then decrypts the encrypted message using Person B's private key.


#### Key Generation
Choose a fixed integer `n` for the size (in bits) of messages to send so that We will be encrypting and decrypting n-bit messages. For this assignment, we'll use `n = 8` bits, so we can encrypt and decrypt messages one byte at a time.

First, we choose a superincreasing sequence of n nonzero natural numbers:

```
w = (w_1, w_2, ..., w_n)
```

A superincreasing sequence is one in which every element is greater than the sum of all previous elements. For example, `(1, 3, 6, 13, 27, 52)` is a superincreasing sequence, but `(1, 3, 4, 9, 15, 25)` is not.

Next, pick a random integer `q`, such that `q` is greater than the sum of the the elements in `w`. For good performance, choose `q` between 1x and 2x the sum of the elements in `w`.

After, choose a random integer `r` such that `gcd(r, q) = 1` (i.e. r and q are coprime).

Finally calculate the tuple

```
beta = (b_1, b_2, ..., b_n)
```

where

```
b_i = r × w_i mod q
```

The public key is `beta`, while the private key is `(w, q, r)`.

#### Encryption

To encrypt an n-bit message

```
alpha = (a_1, a_2, ..., a_n)
```

where `a_i` is the `i`-th bit of the message and `a_i` is either 0 or 1, calculate

```
c = sum of a_i × b_i for i = 1 to n
```

The ciphertext is then `c`.

#### Decryption

In order to decrypt a ciphertext `c` a receiver has to find the message bits `alpha_i` such that they satisfy

```
c = sum of a_i × b_i for i = 1 to n
```

This would be a hard problem if the `b_i` were random values because the receiver would have to solve an instance of the subset sum problem, which is known to be NP-hard (i.e. very hard). However, `beta` was chosen such that decryption is easy if the private key `(w, q, r)` is known.

The key to decryption is to find an integer `s` that is the modular inverse of `r` modulo `q`. That means `s` satisfies the equation `s r mod q = 1` or equivalently there exist an integer k such that `sr = kq + 1`. Since `r` was chosen such that `gcd(r,q) = 1` it is possible to find `s` and `k` by using the Extended Euclidean algorithm, which we've implemented for you. 

Once `s` is known, the receiver of the ciphertext computes

```
c' = cs mod(q)
```

Because of `rs mod q = 1` and `b_i = r × w_i (mod q)`, we know

```
b_i s =  w_i r s = w_i (mod q).
```

Therefore,

```
c' = cs = sum of a_i × b_i × s for each i = a_i × w_i (mod q).
```

The sum of all values `w_i` is smaller than `q` and hence `sum of a_i × w_i` is also in the interval `[0,q-1]`. Thus the receiver has to solve the subset sum problem

```
c' = sum of a_i × w_i for i = 1 to n
```

This problem is computationally easy because `w` was chosen to be a superincreasing sequence. Take the largest element in `w`, say `w_k`. If `w_k > c` , then `a_k = 0`, and if `w_k  <= c`, then `a_k = 1`. Then, subtract `w_k × a_k` from `c` , and repeat these steps until you have figured out all of `alpha`.

Still confused? This stuff can get complicated. Wikipedia provides [a great example](https://en.wikipedia.org/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem#Example) to work through if you prefer concrete numbers over abstract symbols.

What do you actually have to implement? We've taken care of a lot of the math behind-the-scenes (if you want to check out how, look into `utils.py`).

```
def create_public_key(private_key):
    pass  # Build a public key corresponding to the private key
    # Hint: this can be written in one line using a list comprehension
    
def encrypt_mh(message, public_key):
    """Encrypt an outgoing message using a public key.
    
    1. Separate the message into byte-sized chunks
    2. For each byte, determine the 8 bits
    3. Encrypt the 8 message bits by computing
         c = sum of a_i * b_i for i = 1 to n
    4. Return a list of encrypted ciphertexts

    @param message The message to be encrypted
    @type message bytes
    @param public_key The public key of the desired recipient
    @type public_key n-tuple of ints
    
    @return list of ints
    """
    return message
    
    # Hint: think about using zip
    
def decrypt_mh(message, private_key):
    """Decrypt an incoming message using a private key
    
    1. Extract w, q, and r from the private key
    2. Compute s using the Extended Euclidean algorithm
    3. For each bite-sized chunk, compute
         c' = cs (mod q)
    4. Solve the superincreasing subset sum using c' and w
    5. Use the resulting message bits to reconsitute the message
    
    @param message Encrypted message chunks
    @type message list of ints
    @param private_key The private key of the recipient
    @type private_key 3-tuple of w, q, and r
    """
```

Note: 

*Full credit to the Wikipedia summary for this explanation! The description is shamelessly copied and modified :)*
## Console Menu
This program is user-driven, so your first step is to write a function that asks the user if they want to (e)ncrypt or (d)ecrypt a (f)ile or a (s)tring, and lastly whether to do so using a (c)aesar cipher, a (v)igenere cipher, or a (r)ailfence cipher. If the Vigenere or railfence ciphers are selected, either for encryption or decryption, you should make sure to ask the user for additional information. In the case of the Vigenere cipher, you should ask them for the phrase to be used as a secret key. In the case of the railfence cipher, you should request a positive integer number of rails. 

The program should be case-insensitive. A sample run of the program might look like this:

```
$ python3 crypto.py
Welcome to the Cryptography Suite!
*Input*
(F)ile or (S)tring? S
Enter the string to encrypt: I’m not dead yet
*Transform*
(E)ncrypt or (D)ecrypt? E
(C)aesar, (V)igenere, or (R)ailfence? v
Passkey? Python
Encrypting IMNOTDEADYET using Vigenere cipher with key PYTHON
...
*Output*
(F)ile or (S)tring? f
Filename? output.txt
Writing ciphertext to output.txt...
Again (Y/N)? Y
*Input*
(F)ile or (S)tring? F
Filename: secret_message.txt
*Transform*
(E)ncrypt or (D)ecrypt? D
(C)aesar, (V)igenere, or (R)ailfence? C
Decrypting contents of secret_message.txt using Caesar cipher
...
*Output*
(F)ile or (S)tring? S
The plaintext is: HELLOWORLD
```

If the user enters an invalid option to a prompt, you should reprompt until they enter an appropriate response.

For robustness, you should strip text of all non-alphabetic characters like spaces and punctuation, which should not be encrypted, before passing the text to the encrypt_* and decrypt_* functions. The function str.isalpha() may be helpful.

Implement the function:
run_suite()
which should run a single iteration of the cryptography suite, prompting the user for information about input, transformation, and output.

## File I/O

No cryptography tool would be complete without the ability to encrypt and decrypt files! In this final section, you will incorporate file input and output into the program.

You will need to update the console menu in order to allow the user to supply a filename to use.


Notes:

- You may assume that all filenames supplied by the user represent valid files with the appropriate read/write flags set.
- You only need to implement file I/O for Caesar and Vigenere ciphers. Merkle-Hellman is 

Implement the functions:

```
get_text()
write_text(content)
```

Recall that you can open a file for writing by passing the `w` flag to open.

## Extensions

The following section is an extension and is entirely optional. If you choose to give it a crack, give us some documentation and let us know how it went in your feedback!

### Intelligent Codebreaker
Suppose that you have access to ciphertext that you know has been encrypted using a Vigenere cipher. Furthermore, suppose that you know that the corresponding plaintext has been written using only words in /usr/share/dict/words, although you don’t know the exact message. Finally, suppose that you know that someone has encrypted a message using a Vigenere cipher with a key drawn from a preset list of words. Can you still decrypt the ciphertext?

For many of the incorrect keys, the resulting plaintext will be gibberish. Thus, the bulk of this problem lies in evaluating how close to an English sentence a given sequence of letters is.

Your top-level function should be

```
decrypt_vigenere(ciphertext, possible_keys)
```

Besides that, you are free to implement this program however you see fit. However, think about the Python style guidelines before continuing.

You can test your method on “SEOEYMIDWTGFAGAXSEAOQYAIXTRROTY”

### Error Handling
Currently, our program makes a lot of strong assumptions - see the Notes section in each part. Can you add code to handle cases where these assumptions are violated? For example, you should reprompt the user for a file if the file she supplied is invalid.

### Encrypt Non-Text Files
So far, our encryption techniques have been applied solely to letters from the alphabet. However, it is possible to extend these encryption methods to work on arbitrary binary data, such as images, audio files, and more. For this extension, choose at least one of the encryption techniques and make it work on binary files. You will need to use the binary flag when reading from files, which you can read more about here. You may want to read about text sequence types compared with binary sequence types as well.

## Design

Please submit a short design document (`design.txt`) describing your approach to each of the parts of the assignment. "Short" means a few sentences (2-4) per part discussing the rationale behind your decision to implement this program in the way you did.

## Feedback

We hope you have been enjoying the course so far, and would love to hear from you about how this first assignment went! It's the first assignment we've ever written from scratch, and there's definitely room for us to improve on structuring and pacing the various parts of the class and assignments. 

To help us out, please answer the following questions in the `feedback.txt` file provided with the starter code:

1. How long did this assignment take you to complete?
2. What has been the best part of the class so far?
3. What can we do to make this class more enjoyable for you?
4. What types of assignments would excite you in this class?

Thank you for being our guinea pigs this quarter - we're learning from you as well as we teach this course!

## Grading

Your grade will be assessed on both functionality and style.

Functionality will be determined entirely by your program's correctness on a suite of unit tests (some of which are provided with the starter code).

Stylistically, you will be evaluated on your general program design (a la 106 series: decomposition, logic, etc) as well as your Python-specific style. In particular, we will be looking for "Pythonic" approaches to solving problems, as opposed to "non-Pythonic" solutions, that emphasize the Zen of Python. We will also be looking at your Python syntax and mechanics. We encourage you to format your code in accordance with [Python style guidelines](https://www.python.org/dev/peps/pep-0008/). You can find a tool to help format your code [online](http://pep8online.com/).

## Submitting

Stay tuned for assignment submission instructions!

## Credit
*Sherman Leung (@skleung), Python Tutorial, Learn Python the Hard Way, Google Python, MIT OCW 6.189, and Project Euler.*

> With <3 by @sredmond 
