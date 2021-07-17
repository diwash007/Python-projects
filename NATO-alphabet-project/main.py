import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

not_success = True

while not_success:
	word = input("Enter a word: ").upper()
	try:
		output_list = [phonetic_dict[letter] for letter in word]
	except KeyError:
		print("Only alphabets please!!")
	else:
		not_success = False
		print(output_list)
