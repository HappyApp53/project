# The following program checks if a message is valid using digital signatures

# Signing a message
def sign_message(message, key):
    message_int = 0
    for c in message:
        message_int += ord(c)
    a = key[0]
    b = key[1]
    mac_tag = (a * message_int + b) % p
    return mac_tag


# Publicly known information
p = 491
message = "Tell us your middle name Luigi!!"

# Privately known information
key = [15,20]

# Message is broadcast alongside its MAC
mac = sign_message(message, key)


# Verify the message
def check_mac(old_mac, new_mac):
    if old_mac == new_mac:
        print("Message is valid!")
    else:
        print("Message is compromised!")


# Recipient check messages received
message1 = "Tell us your middle name Luigi!!"
message2 = "Tell us your last name Luigi!!"

# Verify message 1
mac1 = sign_message(message1, key)
check_mac(mac, mac1)

# Verify message 2
mac2 = sign_message(message2, key)
check_mac(mac, mac2)