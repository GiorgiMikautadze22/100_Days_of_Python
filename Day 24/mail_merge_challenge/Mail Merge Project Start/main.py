#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".



with open('./Input/Names/invited_names.txt') as names_data:
    names = names_data.readlines()

with open('./Input/Letters/starting_letter.txt') as letter_data:
    letter = letter_data.read()
    for name in names:
        name = name.strip()
        with open(f'./Output/ReadyToSend/{name}_letter.txt', mode='w') as invitation:
            letter = letter.replace('[name]', name)
            invitation.write(letter)

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp