import pandas 
def application_run():
#TODO 1. Create a dictionary in this format:
    alphabet_dt = pandas.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")
    alphabet_dict = {row.letter:row.code for (index, row) in alphabet_dt.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


    user_input = input("Please enter a word : ").upper()

    try:
        each_letter = [alphabet_dict[letter] for letter in user_input if letter != ' ']

        print(each_letter)

    except KeyError:
        print("Please Enter Letters Only.")
        application_run()
        


application_run()

