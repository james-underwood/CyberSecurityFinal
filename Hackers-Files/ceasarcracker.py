import string

# Load the English dictionary
with open("/usr/share/dict/american-english", "r") as f:
    words = set([line.strip().upper() for line in f])

def decrypt(text, key):
    """Decrypt the given text using the specified key."""
    result = ""
    for char in text:
        if char in string.ascii_uppercase:
            index = (string.ascii_uppercase.index(char) - key) % 26
            result += string.ascii_uppercase[index]
        else:
            result += char
    return result

def caesar_crack(ciphertext):
    """Crack the Caesar cipher used to encrypt the given ciphertext."""
    for key in range(26):
        plaintext = decrypt(ciphertext, key)
        words_in_plaintext = set(plaintext.split())
        if words_in_plaintext.intersection(words):
            return key, plaintext
    return None, None

# Open the input file and crack the cipher for each line
with open("separated/CS.txt", "r") as f:
    for line in f:
        line = line.strip()
        key, plaintext = caesar_crack(line)
        if key is not None:
            print(f"Key: {key}  Plaintext: {plaintext}")
