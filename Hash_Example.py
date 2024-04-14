# The following program demonstrates a hash function
def new_hash(message):
    digest = 0
    for c in message:
        digest += ord(c)
        print(ord(c))
        digest = digest % 256
    return digest


print(new_hash("iD Tech"))

# Youtube video - https://www.youtube.com/watch?v=GI790E1JMgw
