message = input("Enter the message: ")
shift = int(input("Enter the shift value : "))

encrypted_message = ""

for letter in message:
    ascii_value = ord(letter)
    alphabet_position = ascii_value - 65
    shifted_position = (alphabet_position + shift) % 26
    shifted_ascii = shifted_position + 65
    encrypted_letter = chr(shifted_ascii)
    encrypted_message = encrypted_message + encrypted_letter

    print(encrypted_message)
    
