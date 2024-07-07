def caesar_cipher_encrypt(plaintext, shift):
    ciphertext = []
    for char in plaintext:
        if char.isalpha():  # Check if character is a letter
            # Determine the appropriate case (uppercase or lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Perform the shift and handle wrap-around using modulus
            shifted = chr((ord(char) - base + shift) % 26 + base)
            ciphertext.append(shifted)
        else:
            ciphertext.append(char)  # Non-alphabet characters remain unchanged
    return ''.join(ciphertext)

def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher_encrypt(ciphertext, -shift)  # Decrypting is just shifting in reverse

# Example usage:
plaintext = "Hello, World!"
shift = 3

encrypted_text = caesar_cipher_encrypt(plaintext, shift)
print(f'Encrypted: {encrypted_text}')

decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
print(f'Decrypted: {decrypted_text}')
