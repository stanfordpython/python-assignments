import math as math

def encrypt_railfence(plaintext, num_rails):
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

print(encrypt_railfence("ABCDEFGHIJ", 4))
print(decrypt_railfence(encrypt_railfence("ABCDEFGHIJ", 4), 4))