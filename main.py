print("Welcome to the main center of communication")
while True:
    fInput = int(input('Please select a process 1: Encryption, 2: Decryption'))
    if fInput == 1:
        #This is where the encryption portion goes
        sInput = int(input('Please select a encryption method 1.AES? 2. DES 3. 3DES'))
        if sInput == 1:
                print("AES ENCRYPT")
            elif sInput == 2:
                print("DES ENCRYPT")
            elif sInput == 3:
                print("3DES ENCRYPT")
            else
                print("ERROR: Incorrect input please try again")
    elif fInput == 2:
        #This is where the decryption portion goes
        sInput = int(input('Please select a decryption method 1.AES? 2. DES 3. 3DES'))
            if sInput == 1:
                print("AES DECRYPT")
            elif sInput == 2:
                print("DES DECRYPT")
            elif sInput == 3:
                print("3DES DECRYPT")
            else
                print("ERROR: Incorrect input please try again")
    else:
        #User inputted a weird input make them do it again
        print("ERROR: Incorrect input please try again")
