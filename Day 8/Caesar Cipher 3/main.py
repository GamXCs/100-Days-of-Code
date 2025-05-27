
import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, text, shift):
            result_str = ""
            for letter in text:
                if letter in alphabet:
                    old_index = alphabet.index(letter)
                    if direction == "encode":
                        new_index = (old_index + shift) % 26
                    elif direction == "decode":
                        new_index = (old_index - shift) % 26
                    result_str += alphabet[new_index]
                else:
                    result_str += letter
            print(f"Your {direction}d message is: {result_str}")

run_again = True
while run_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)

    restart = input("Type 'yes' to run again. Type 'no' to exit. ").lower()
    if restart != 'yes':
        run_again = False




