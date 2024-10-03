#TODO: Choose random number from 1 to 100
#TODO: Ask difficulty of a game and print remaining guesses
#TODO: Let the user guess
#TODO: Create function that checks weather the guess is higher or lower.
#TODO: If the user guessed the word stop the game.
#TODO: If the user run out of attempts stop the game.
#TODO: After the game has ended ask user if they wish to play again
import random

random_number = random.randint(1, 100)
difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
attempts = 0

def higher_lower():
    global attempts

    if users_guess > random_number:
        print('Too High')
        print('Guess again')
        print(f'You have {attempts} remaining')
    else:
        print('Too low')
        print('Guess again')
        print(f'You have {attempts} remaining')

if difficulty == 'easy':
    attempts += 10
else:
    attempts += 5

print(f'You have {attempts} guesses remaining')

while attempts > 0:
    users_guess = int(input('Make a guess: '))
    attempts -= 1
    if users_guess == random_number:
        attempts = 0
        print(f"You guessed the number. It was {random_number}")
    elif attempts == 0:
        print(f'You run out of guesses. The number was {random_number}')
    else:
        higher_lower()

