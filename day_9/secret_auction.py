#TODO 1: Ask the names and bids of participant and push it in the dictionary
import os

participant_dict = {}

def find_highest_bidder(winner):
    winner['name'] = max(participant_dict, key=participant_dict.get)
    winner['bid'] = participant_dict[max(participant_dict, key=participant_dict.get)]
    print(f'The winner is {winner["name"]} with ${winner["bid"]} bid')

def add_participant():
    participant = {
        'bid' : 0,
        'name' : ''
    }
    name = input('What is your name? \n')
    bid = int(input('What is your bid? \n'))

    participant_dict[name] = bid

    add_another_participant = input('Do you want to add another participant? \n').lower()
    # TODO 2: If there are more participant do the process again ELSE loop over the dictionary and display max bid
    if add_another_participant == 'yes':
        os.system('cls')
        add_participant()
    else:
        find_highest_bidder(participant)

add_participant()