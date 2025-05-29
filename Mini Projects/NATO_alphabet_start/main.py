student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    print(index,row)
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
print("=================================================================================================================")
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row['letter']:row['code'] for (index,row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def nato_alfabet():
    user_input = input("Enter your name: ").upper()
    try:
        output = [phonetic_dict[letter] for letter in user_input]
    except KeyError as err_message:
        print(f"{err_message} not a word.")
        nato_alfabet()

    else:
        print(output)
nato_alfabet()
