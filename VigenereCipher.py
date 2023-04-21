# Daet, Joshua Adrian O.
# Assignment No. 2
# Question No. 3


# This program will encrypt a message using the Vigenère Cipher
# Create a header
print("")
name = "Hi! I am Joshua Adrian O. Daet of BSCpE 1-4"
print(name.center(158))

sentence = "This is a program where you can cipher text with Vigenère Cipher"
print("")
print(sentence.rjust(110))
print("")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("")

# Ask the user for the message and the key
message = input("Please enter the message: ")
message = message.upper().replace(" ", "")
print("")
print("Your message is: " +message)
print("")
key = input("Please enter the key: ")
key = key.upper().replace(" ", "")
print("")
print("Your key is: " +key)

 # Translate the key into corresponding letter values 0 - 25
key_map = [ord(i) - 65 for i in key]

# Encrypt the message
ciphertext = ""
for i in range(len(message)):
        encrypted_num = (ord(message[i]) - 65 + key_map[i % len(key_map)]) % 26
        ciphertext += chr(encrypted_num + 65)
print("")

# Output of the ciphertext
print("The ciphertext is: " +ciphertext)
print("")