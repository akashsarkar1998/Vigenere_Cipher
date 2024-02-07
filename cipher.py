# Define the plaintext message and the key for encryption and decryption
text = 'password'
custom_key = 'strongpassword'

def vigenere(message, key, direction=1):
    # Initialize the index for the key and the alphabet used in the cipher
    key_index = 0
    characters = 'abcdefghijklmnopqrstuvwxyz'
    # Initialize the final message variable
    final_message = ''

    # Iterate through each character in the message
    for char in message.lower():

        # Append any non-letter character to the final message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode based on the key index
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = characters.index(key_char)
            index = characters.find(char)
            new_index = (index + offset*direction) % len(characters)
            final_message += characters[new_index]
    
    return final_message

# Function to encrypt a message using the Vigenère cipher
def encrypt(message, key):
    return vigenere(message, key)
    
# Function to decrypt a message using the Vigenère cipher
def decrypt(message, key):
    return vigenere(message, key, -1)

# Print the original text, the key used for encryption, and the encrypted text
print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')

# Decrypt the encrypted text using the key and print the result
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')


#  https://www.freecodecamp.org/learn/scientific-computing-with-python/
 #learn-string-manipulation-by-building-a-cipher 