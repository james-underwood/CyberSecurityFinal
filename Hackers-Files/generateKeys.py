# This will generate 8 byte keys for john the ripper to go through for the DES

import random
import string

def generate_keys(num_keys):
    # Define the characters to be used in the keys
    chars = string.ascii_letters + string.digits + string.punctuation

    # Generate random keys
    keys = []
    for i in range(num_keys):
        key = ''.join(random.choices(chars, k=8))
        keys.append(key)

    return keys


keys = generate_keys(100000)

with open('keylist.txt', 'w') as f:
    for key in keys:
        f.write(key + '\n')


"5ceeec120d69c62d867e51eac8a8893aa548a34a4f8fb738436d59f0dc9025d41490f86af6d4bf7c" | john --wordlist=/path/to/rockyou.txt -e=des -stdin-nt

"5ceeec120d69c62d867e51eac8a8893aa548a34a4f8fb738436d59f0dc9025d41490f86af6d4bf7c" | john --wordlist=/usr/share/wordlists/rockyou.txt.gz --rules --external=gunzip --format=crypt 
