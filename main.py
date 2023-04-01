# Import file where we are going to store our functions
from functions import *
import os

print("Welcome to the main center of communication")

# Get user location input
location = input('Please enter your location (HQ, FU1, FU2): ').upper()

# Determine available encryption and decryption methods based on location
if location == "HQ":
    available_encryption_methods = [1, 2, 3]  # CS, DES, 3DES
    available_decryption_methods = [1, 2, 3]  # CS, DES, 3DES
    destinations = ["FU1", "FU2"]  # HQ can send to both FU1 and FU2
elif location == "FU1":
    available_encryption_methods = [1]  # CS only
    available_decryption_methods = [1, 2, 3]  # CS, DES, 3DES
    destinations = ["HQ", "FU2"]
elif location == "FU2":
    available_encryption_methods = [1]  # CS only
    available_decryption_methods = [1, 2, 3]  # CS, DES, 3DES
    destinations = ["HQ", "FU1"]  # Adding FU1 to the list of destinations
    
else:
    print("ERROR: Invalid location entered.")
    exit()

with open("output.csv", "a") as file:
    while True:
        fInput = int(input('Please select a process: 1. Encryption, 2. Decryption: '))

        if fInput == 1:
            # This is where the encryption portion goes

            sInput = int(input('Please select an encryption method: 1. CS, 2. DES, 3. 3DES: '))

            if sInput in available_encryption_methods:
                plaintext = input("Enter the message to encrypt: ")
                if sInput == 1:
                    ciphertext = caesar_encrypt(plaintext)
                elif sInput == 2:
                    ciphertext = des_encrypt(plaintext)
                elif sInput == 3:
                    ciphertext = des3_encrypt(plaintext)

                print(f"Encrypted text: {ciphertext}")

                while True:
                    destination = input(f"Enter the destination (available: {', '.join(destinations)}): ").upper()
                    if destination != location and destination in destinations:
                        break
                    else:
                        print("ERROR: Invalid destination entered.")

                # Write the encrypted text to a file
                file.write(f"{location}, {destination}, {encryption_method_name(sInput)}, {ciphertext}, {plaintext}\n")
                print("Message saved to output.csv")

            else:
                print("ERROR: Incorrect input please try again.")

        elif fInput == 2:
            # This is where the decryption portion goes

            sInput = int(input('Please select a decryption method: 1. CS, 2. DES, 3. 3DES: '))

            if sInput in available_decryption_methods:
                ciphertext = input("Enter the message to decrypt: ")
                if sInput == 1:
                    plaintext = caesar_decrypt(ciphertext)
                elif sInput == 2:
                    plaintext = des_decrypt(ciphertext)
                elif sInput == 3:
                    plaintext = des3_decrypt(ciphertext)

                print(f"Decrypted text: {plaintext}")

            else:
                print("ERROR: Incorrect input please try again.")

        else:
            # User inputted a weird input, make them do it again
            print("ERROR: Incorrect input please try again.")
