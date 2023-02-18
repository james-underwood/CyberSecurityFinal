def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # shift the character by the specified number of positions
            encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted_char = char
        ciphertext += encrypted_char
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # shift the character back by the specified number of positions
            decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            decrypted_char = char
        plaintext += decrypted_char
    return plaintext

def des_encrypt():
    print("DES ENCRYPT")

    

def des3_encrypt():
    print("3DES ENCRYPT")



def aes_decrypt():
    print("AES DECRYPT") #DONT USE AES 

def des_decrypt():
    print("DES DECRYPT")

    

def des3_decrypt():
    print("3DES DECRYPT")
