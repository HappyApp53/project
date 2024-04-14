# The following program implements a stream cipher.
code = "010101001011010"
key = "010101011010011"

code_ints = [int(i) for i in str(code)]
key_ints = [int(i) for i in str(key)]
cipher_ints = []

for x in range(len(code_ints)):
    cipher_bit = code_ints[x] ^ key_ints[x]
    cipher_ints.append(cipher_bit)
    cipher = "".join(str(b) for b in cipher_ints)
print(cipher)
