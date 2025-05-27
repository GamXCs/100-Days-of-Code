alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# def encrypt(original_text, shift_amount):
#     encoded_str = ""
#     for letter in original_text:
#         old_index = alphabet.index(letter)
#         new_index = (old_index + shift_amount) % 26
#         encoded_str += alphabet[new_index]
#     print(f"Your encrypted message is: {encoded_str}")
#
# encrypt(text,shift)
#
# def decrypt(original_text,shift_amount):
#     decrypted_str = ""
#     for letter in original_text:
#         old_index = alphabet.index(letter)
#         new_index = (old_index - shift_amount) % 26
#         decrypted_str += alphabet[new_index]
#     print(f"Your decrypted message is: {decrypted_str}")
#
# decrypt(text,shift)

def caesar(direction, text, shift):
    if direction == "encode":
            encoded_str = ""
            for letter in text:
                old_index = alphabet.index(letter)
                new_index = (old_index + shift) % 26
                encoded_str += alphabet[new_index]
            print(f"Your encrypted message is: {encoded_str}")
    else:
            decrypted_str = ""
            for letter in text:
                old_index = alphabet.index(letter)
                new_index = (old_index - shift) % 26
                decrypted_str += alphabet[new_index]
            print(f"Your decrypted message is: {decrypted_str}")

caesar(direction, text, shift)

