import numpy as np

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
end_program = False

def matrix(text,is_key=False):
    text_matrix = []
    for i in range(0,len(text),2):
        row = []
        row.append(alphabet.index(text[i]))
        try:
            row.append(alphabet.index(text[i+1]))
        except:
            row.append(0)
        if not is_key:
            row = np.array(row)
        text_matrix.append(row)
    if is_key:
        return np.array(text_matrix)
    return text_matrix

def encode(plain_matrix, key_matrix):
    encoded_matrix = []
    result = ""
    for i in range(len(plain_matrix)):
        encoded_matrix.append(np.mod(key_matrix@plain_matrix[i],26))
    for i in range(len(encoded_matrix)):
        for j in range(2):
            result += alphabet[encoded_matrix[i][j]]
    return result

def decode(text_matrix, key_matrix):
    decoded_matrix = []
    result = ""
    key_inverse = np.linalg.inv(key_matrix)
    key_det = round(np.linalg.det(key_matrix))
    adjoint = key_inverse*key_det*-1
    det_multiplier = np.mod(pow(key_det,-1,26)*-1,26)
    decoder_matrix = np.mod(adjoint*det_multiplier,26)

    for i in range(len(text_matrix)):
        decoded_matrix.append(np.mod(decoder_matrix@text_matrix[i],26))
    for i in range(len(decoded_matrix)):
        for j in range(2):
            result += alphabet[int(decoded_matrix[i][j])]
    return result

print("HILL CYPHER\n")
while not end_program:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Enter text: ")
    key = input("Enter key [of 4 letters]: ")
    plain_matrix = matrix(text)
    key_matrix = matrix(key, True)
    try:
        result = decode(plain_matrix, key_matrix)
    except:
        print(f"\nThe key '{key}' cannot work with hill cypher. Please try with different key.\n")
        continue
    if direction == "decode":
        print(f"The {direction}d text is {result}.")
    elif direction == "encode":
        result = encode(plain_matrix, key_matrix)
        print(f"The {direction}d text is {result}.")
    else:
        print("Invalid input!!\n")
        continue

    rs = input("\nWould you like to restart the program?[yes/no]")
    if not rs == "yes":
        end_program = True
        print("Program exited succesfully!!")