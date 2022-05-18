student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     print(key)
#     print(value)


import pandas

# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     print(index,row)
#     print(row.student)
#     print(row.score)

# Keyword Method with iterrows()
df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_words = {row.letter: row.code for (index, row) in df.iterrows()}
# print(phonetic_words)
# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    name = input("Enter a name:").upper()
    try:
        code_words = [phonetic_words[c] for c in name]
    except:
        print("Name shuld contain only Alphabets!")
        continue
    else:
        print(code_words)
        break
