# The following program uses checksums to verify messages.
def byte_checksum(message):
    parity_byte = 0
    for c in message:
        parity_byte += ord(c)
        parity_byte = parity_byte % 256
    parity_byte = (~parity_byte + 1) % 256
    return message + chr(parity_byte)


# Create a message
message1 = "Cheerio"
message2 = byte_checksum(message1)
print(message2)


# Verify the Message
def verify_byte(message):
    parity_check = 0
    for c in message:
        parity_check += ord(c)
        parity_check = parity_check % 256
    if parity_check == 0:
        print("Valid checksum")
    else:
        print("Invalid checksum")


# Verify Messages
verify_byte(message2)

new_message = "Tell me your last name!"
print(new_message)
verify_byte("Tell me your last name!")
