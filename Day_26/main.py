import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')
data = {row.letter:row.code for (index, row) in df.iterrows()}

user_input = input('Write a Name: ')
split_name = [char.upper() for char in user_input]

coded_name = [data[char] for char in split_name]

print(coded_name)

