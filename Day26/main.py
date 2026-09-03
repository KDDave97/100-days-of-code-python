import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row["letter"]:row["code"] for (index, row) in data.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ")

    if len(word) == 0:
        generate_phonetic()

    try:
        word_in_nato = [data_dict[letter.upper()] for letter in word]
    except KeyError:
        print("Only letters in the alphabet")
        generate_phonetic()
    else:
        print(word_in_nato)

generate_phonetic()