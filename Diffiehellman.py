# The following program implements the diffie-hellman algorithm

# Function to encode a message
def encrypt(message, key):
    cipher = ""
    for c in range(len(message)):
        number = ord(message[c])
        number += key
        cipher += chr(number)
    return cipher


# Function to decode a message
def decrypt(ciphertext, key):
    message = ""
    for c in range(len(ciphertext)):
        number = ord(ciphertext[c])
        number -= key
        message += chr(number)
    return message


# Function to find the shared key
def find_shared_key(private_key, public_key):
    shared_key = public_key ** private_key % public_modulus
    return shared_key


# Private Information
bond_private_key = 5
Luigi_private_key = 7
Jonathan_message = "Cheerio mate"

# Public Information
public_base = 8
public_modulus = 29
bond_public_key = public_base ** bond_private_key % public_modulus
Luigi_public_key = public_base ** Luigi_private_key % public_modulus

# Alice sends Bob an encrypted message
bond_shared_key = find_shared_key(bond_private_key, Luigi_public_key)
bond_cipher = encrypt(Jonathan_message, bond_shared_key)
print(bond_cipher)

# Bob receives message and decrypts using shared key
Luigi_shared_key = find_shared_key(Luigi_private_key, bond_public_key)
Luigi_message = decrypt(bond_cipher, Luigi_shared_key)
print(Luigi_message)