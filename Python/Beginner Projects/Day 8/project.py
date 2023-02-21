
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(len(alphabet))
def new_lettr(lettr, shift, direction):
    if direction == "encode":
        index = alphabet.index(lettr) + shift
        if index >= len(alphabet):
            index = index % len(alphabet)
        return alphabet[index]
    elif direction == "decode":
        index = alphabet.index(lettr) - shift
        if index < 0:
            index = len(alphabet) +  index
        return alphabet[index]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift_num = int(input("Type the shift number:\n"))
new_word = [new_lettr(lettr, shift_num, direction) if lettr.isalpha() else lettr for lettr in text]
print("".join(new_word))
     
