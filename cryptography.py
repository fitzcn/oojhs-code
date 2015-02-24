alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '(', ')', '.']

message = "a cipher (or cypher) is a pair of algorithms that create the encryption and the reversing decryption."

encrypt = ""
for l in message:
	encrypt += alphabet[alphabet.index(l) - 7]

print encrypt