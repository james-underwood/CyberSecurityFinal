import binascii
import pyDES
import os

def caesar_encrypt(plaintext):
    ciphertext = ""
    shift = int(input("Enter the shift amount: "))
    for char in plaintext:
        if char.isalpha():
            # shift the character by the specified number of positions
            encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted_char = char
        ciphertext += encrypted_char
    return ciphertext

def caesar_decrypt(ciphertext):
	plaintext = ""
	shift = input("Enter the shift amount: ")
	for char in ciphertext:
		if char.isalpha():
			# shift the character back by the specified number of positions
			decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
		else:
			decrypted_char = char
		plaintext += decrypted_char
	return plaintext

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
