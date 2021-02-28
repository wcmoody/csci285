from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from binascii import unhexlify, hexlify

#place secret message here
data = b'Secret Message goes here'

# generate a random key and IV
key = get_random_bytes(16)
iv = get_random_bytes(16)

# load a defined random key and IV
key = unhexlify('deadbeefdeadbeefdeadbeefdeadbeef')
vi = unhexlify('0123456789abcdeffedcba9876543210')


# Available Modes are:
# AES.MODE_ECB (does not require an IV)
# AES.MODE_CBC
# AES.MODE_CFB
# AES.MODE_OFB
# AES.MODE_CTR

# Create an AES object called cipher1
cipher1 = AES.new(key,AES.MODE_CBC, iv)
# Encrypt the message with padding
ct = cipher1.encrypt(pad(data,16))
# Print the ciphertext in hexadecimal format
print("Ciphertet (in hex) ", hexlify(ct))

# Create another AES object this time called cipher2
cipher2 = AES.new(key,AES.MODE_CBC, iv)
# Decrypt the previously encrypted message (ct)
pt = unpad(cipher2.decrypt(ct),16)
# Print out the original message, showing it did not change
print('Plaintext message: ', pt)


# Asset will ensure the statement is true
# or the program will fail hard
assert(data==pt)
