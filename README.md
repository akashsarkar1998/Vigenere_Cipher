# Vigenere Cipher Encryption and Decryption

This Python program implements the Vigenere cipher encryption and decryption methods. The Vigenere cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution.

## Usage

The Vigenere cipher can be used for secure communication by encrypting plaintext messages with a key, making it unreadable to anyone who does not possess the key to decrypt it. Here are some common use cases for using Vigenere cipher codes:  
1. The Vigenere cipher can be used to encrypt sensitive information, such as personal messages, financial data, or any other confidential communication  
2. For scenarios where a simple encryption method is sufficient, such as encrypting personal notes, passwords, or small pieces of data, the Vigenère cipher can serve as a lightweight encryption solution  
3. Overall, while the Vigenère cipher may not provide the same level of security as modern cryptographic algorithms, it remains a valuable tool for learning cryptography concepts and for applications where lightweight encryption is acceptable.

#### Here a example of the code:
```python
text = 'password'
custom_key = 'strongpassword'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')
```

### Contributor:
Akash Sarkar   
email: akashsarkarcob98@gmail.com  
##### My Linkedin profile: &nbsp; [Akash's-Linkedin-Account][Linkedin_Account]

Feel free to contribute or provide feedback!


<!--Linkedin profile link here:-->
[Linkedin_Account]: https://www.linkedin.com/in/akash-sarkar59/
