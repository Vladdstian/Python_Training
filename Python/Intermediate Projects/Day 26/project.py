import pandas

file_loc = 'nato_phonetic_alphabet.csv'

name = input('What is your name?: ').upper()
name = [lettr for lettr in name if lettr.isalpha()]

data = pandas.read_csv(file_loc)
data = {row.letter:row.code for (index, row) in data.iterrows()}
name = [data[letter] for letter in name]

print(f"Your name in NATO Phonetic alphabet is: {' '.join(name)}.")

