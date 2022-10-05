from characters_list import characters


def caesar_cipher(direction, text, shift):
    index = []
    counter = 0
    result = ""
    for char in text:
        index.append(characters.index(char))

    for position in index:
        if direction == "encode":
            index[counter] = position + shift
        elif direction == "decode":
            index[counter] = position - shift

        counter += 1

    for position in index:
        if shift == 1:
            result += (characters * 2)[position]
        else:
            result += (characters * shift)[position]

    print(result)


def run_caesar_cipher():
    run = "yes"
    while run == "yes":

        command = input('What would you like to do? Enter "encode" to encrypt '
                        'or "decode" to decrypt.\n').lower()
        if command == "encode" or command == "decode":
            text_input = input("Enter the text:\n")
            shift_input = int(input("Enter the shift amount:\n"))
            caesar_cipher(direction=command, text=text_input, shift=shift_input
                          )
        else:
            print("Invalid command, please try again with a valid one. ")

        run = input('Type "yes" to go again otherwise type "no":\n').lower()

    print("Goodbye!")
