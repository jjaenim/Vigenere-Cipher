# Encrypt the message
ciphertext = ""
for i in range(len(message)):
        encrypted_num = (ord(message[i]) - 65 + key_map[i % len(key_map)]) % 26
        ciphertext += chr(encrypted_num + 65)
print("")