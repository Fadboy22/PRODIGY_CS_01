def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
            if char.islower() == False:
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char
    
    return result

# Encryption function
def encrypt(message, shift):
    return caesar_cipher(message, shift, "encrypt")

# Decryption function
def decrypt(encrypted_message, shift):
    return caesar_cipher(encrypted_message, -shift, "decrypt")

# Get user inputs
message = input("Enter your message: ")
shift = int(input("Enter the shift value (integer between 1 and 25 inclusive): "))

# Perform encryption or decryption based on user choice
choice = input("Do you want to 'encrypt' or 'decrypt' your message? ")
if choice == "encrypt":
    print("Encrypted Message:", encrypt(message, shift))
elif choice == "decrypt":
    print("Decrypted Message:", decrypt(message, shift))
else:
    print("Invalid Choice.")