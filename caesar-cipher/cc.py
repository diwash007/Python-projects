from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
end_program = False

def caesar(text, shift, direction):
    result = ""
    if direction == "decode":
        shift *= -1
    for i in text:
        if i in alphabet:
            new_index = alphabet.index(i) + shift
            new_index = new_index % 26
            result += alphabet[new_index]
        else:
            result += i
    print(f"The {direction}d text is {result}")

print(logo)
while not end_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction == "decode" or direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
    else:
        print("Invalid input!!")

    rs = input("Would you like to restart the program?")
    
    if not rs == "yes":
        end_program = True
        print("Program exited succesfully!!")
