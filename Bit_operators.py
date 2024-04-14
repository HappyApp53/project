# The following program demonstrates the logic gates.

# And Gate
A = 0b1101
B = 0b1010
C = A & B
print(bin(C))

# Or Gate
D = A | B
print(bin(D))

# Not Gate
E  =  ~ A
print ( bin ( E ))

# XOR Gate
F = A ^ B
print(bin(F))

# Bit Shifting
G = A << 1
H = A >> 2
I = A << 2
print(bin(G))
print(bin(H))
print(bin(I))