def encrypt_caesar(plaintext):
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

def main():
    print(decrypt_caesar(encrypt_caesar("F1RST P0ST")))

if __name__ == "__main__":
    main()