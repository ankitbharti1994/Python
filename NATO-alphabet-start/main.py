import pandas


# TODO 1. Create a dictionary in this format:
dataframe = pandas.read_csv('nato_phonetic_alphabet.csv')
word_dictionary = {row.letter: row.code for (index, row) in dataframe.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input('Enter any word: ').upper()


def find_word(character):
    return word_dictionary[character]


possible_words = [find_word(character) for character in word]
print(possible_words)
