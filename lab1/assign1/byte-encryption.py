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

fileName = "GH010024.MP4"
file = open(fileName, "rb")

paths = fileName.split(".")
extension = paths[len(paths)-1]

text = bytes(len(extension)) + bytes(extension) + file.read()
encrypted_file = open("cipher_text", "wb")

encrypted_text = encrypt_scytale(text, 4)
encrypted_file.write(encrypted_text)

decrypted_text = decrypt_scytale(encrypted_text, 4)
extLen = decrypted_text[0]
ext = ''
for i in range(int(extLen)):
    ext += decrypted_text[i+1]
decrypted_file = open("decrypted."+ext, "wb")
decrypted_file.write(decrypted_text[(int(extLen)+1):])





