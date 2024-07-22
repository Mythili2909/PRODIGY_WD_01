def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption and Decryption")
    choice = input("Would you like to (e)ncrypt or (d)ecrypt? ").strip().lower()
    if choice not in ['e', 'd']:
        print("Invalid choice! Please choose 'e' for encryption or 'd' for decryption.")
        return
    
    text = input("Enter the message: ").strip()
    shift = int(input("Enter the shift value: ").strip())
    
    if choice == 'e':
        encrypted_text = caesar_cipher_encrypt(text, shift)
        print(f"Encrypted message: {encrypted_text}")
    else:
        decrypted_text = caesar_cipher_decrypt(text, shift)
        print(f"Decrypted message: {decrypted_text}")

if __name__ == "__main__":
    main()
