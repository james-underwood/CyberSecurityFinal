import binascii
import pyDES
import os

def caesar_encrypt(plaintext):
    ans = ""
    n = int(input("Enter the key to encrypt: "))
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        
        # check if space is there then simply add space
        if ch==" ":
            ans+=" "
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    
    return ans

def caesar_decrypt(plaintext):
    letters="abcdefghijklmnopqrstuvwxyz"
    
    #enter the key value to decrypt
    k = int(input("Enter the key to decrypt: "))
    decrypted_message = ""

    for ch in plaintext:

        if ch in letters:
            position = letters.find(ch)
            new_pos = (position - k) % 26
            new_char = letters[new_pos]
            decrypted_message += new_char
        else:
            decrypted_message += ch
    return decrypted_message

def des_encrypt(plaintext):
    # Prompt the user to enter the key for encryption
	key = input("Enter the key for encryption (must be at least 8 characters long): ").encode()

    # Truncate or pad the key to ensure it is exactly 8 bytes long
	key = key[:8].ljust(8, b'\0')

    # Set the initialization vector (IV) for encryption and pad it to 8 bytes
	iv = os.urandom(8)

    # Convert the plaintext to bytes and pad it to a multiple of 8 bytes using PKCS5 padding
	plaintext = plaintext.encode()
	plaintext = plaintext.ljust(len(plaintext) + 8 - (len(plaintext) % 8), b"\0")

    # Create a DES cipher object using the key and IV
	cipher = pyDES.des(key, pyDES.CBC, iv, pad=None, padmode=pyDES.PAD_PKCS5)

    # Encrypt the plaintext using the cipher object
	ciphertext = cipher.encrypt(plaintext)

    # Combine the IV and ciphertext and return it as a hexadecimal string
	return binascii.hexlify(iv + ciphertext).decode()
	
def des3_decrypt(ciphertext):
    # Convert the ciphertext from hexadecimal to bytes
	ciphertext = binascii.unhexlify(ciphertext.encode())

    # Prompt the user to enter the key for decryption
	key = input("Enter the key for decryption (must be at least 24 characters long): ").encode()

    # Truncate or pad the key to ensure it is exactly 24 bytes long
	key = key[:24].ljust(24, b'\0')

    # Extract the initialization vector (IV) from the ciphertext
	iv = ciphertext[:8]

    # Create a 3DES cipher object using the key and IV
	cipher = pyDES.triple_des(key, pyDES.CBC, iv, pad=None, padmode=pyDES.PAD_PKCS5)

    # Decrypt the ciphertext using the cipher object
	plaintext = cipher.decrypt(ciphertext[8:])

    # Remove the PKCS5 padding from the plaintext
	plaintext = plaintext.rstrip(b"\0")

    # Convert the plaintext to a string and return it
	return plaintext.decode()


def des_decrypt(ciphertext):
    # Convert the ciphertext from hexadecimal to bytes
	ciphertext = binascii.unhexlify(ciphertext.encode())
    
    # Prompt the user to enter the key for decryption
	key = input("Enter the key for decryption (must be at least 8 characters long): ").encode()

    # Truncate or pad the key to ensure it is exactly 8 bytes long
	key = key[:8].ljust(8, b'\0')

    # Extract the initialization vector (IV) from the ciphertext
	iv = ciphertext[:8]

    # Create a DES cipher object using the key and IV
	cipher = pyDES.des(key, pyDES.CBC, iv, pad=None, padmode=pyDES.PAD_PKCS5)

    # Decrypt the ciphertext using the cipher object
	plaintext = cipher.decrypt(ciphertext[8:])

    # Remove the PKCS5 padding from the plaintext
	plaintext = plaintext.rstrip(b"\0")

    # Convert the plaintext to a string and return it
	return plaintext.decode()

    

def des3_encrypt(plaintext):
    # Prompt the user to enter the key for encryption
	key = input("Enter the key for encryption (must be at least 24 characters long): ").encode()

    # Truncate or pad the key to ensure it is exactly 24 bytes long
	key = key[:24].ljust(24, b'\0')

    # Set the initialization vector (IV) for encryption and pad it to 8 bytes
	iv = os.urandom(8)

    # Convert the plaintext to bytes and pad it to a multiple of 8 bytes using PKCS5 padding
	plaintext = plaintext.encode()
	plaintext = plaintext.ljust(len(plaintext) + 8 - (len(plaintext) % 8), b"\0")

    # Create a 3DES cipher object using the key and IV
	cipher = pyDES.triple_des(key, pyDES.CBC, iv, pad=None, padmode=pyDES.PAD_PKCS5)

    # Encrypt the plaintext using the cipher object
	ciphertext = cipher.encrypt(plaintext)

    # Convert the ciphertext to a hexadecimal string and return it
	return binascii.hexlify(iv + ciphertext).decode()



# EXTRA BITS

def encryption_method_name(method_id):
    """
    Returns the name of the encryption method given an ID
    """
    if method_id == 1:
        return "CS"
    elif method_id == 2:
        return "DES"
    elif method_id == 3:
        return "3DES"
    else:
        return "Unknown"
