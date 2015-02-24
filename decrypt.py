alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '(', ')', '.']

encryptedMessage = "xtzbia(ktuhktzria(kvtbltxtixbkth)txe.hkbmafltmaxmtzk(xm(tma(t(gzkrimbhgtxg tma(tk(o(klbg.t (zkrimbhgw"

decryptedMessage = ""

"""
for l in encryptedMessage:
	decryptedMessage += alphabet[alphabet.index(l) - 23]
print decryptedMessage
"""

for ind in range(0,len(alphabet):
	decryptedMessage = ""
	for l in encryptedMessage:
		decryptedMessage += alphabet[alphabet.index(l) - ind]
	print decryptedMessage

