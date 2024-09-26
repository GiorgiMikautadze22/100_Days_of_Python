# print("Welcome to the tip calculator!")
#
# total_bill = float(input("What is your total bill? $"))
# tip = int(input("How much tip would you like to give? "))
# number_of_people = int(input("How many people would you like? "))
#
# tip_count = total_bill * (tip / 100)
# bill_with_tip = tip_count + total_bill
# each_pay_count = round(bill_with_tip / number_of_people, 2)
#
# result = f"Each person should pay: ${each_pay_count}"
#
# print(result)

# print('Welcome to pizza delivery')
# size = input('What size of pizza do you want? S, M or L: ')
# peperoni = input('Do you want peperoni on your pizza? Y or N: ')
# extra_cheese = input('Do you want extra cheese? Y or N: ')
#
# bill = 0
#
# if size == 'S':
#     bill += 15
#     if peperoni == 'Y':
#         bill += 2
#     if extra_cheese == 'Y':
#         bill += 1
# elif size == 'M':
#     bill += 20
#     if peperoni == 'Y':
#         bill += 3
#     if extra_cheese == 'Y':
#         bill += 1
# elif size == 'L':
#     bill += 25
#     if peperoni == 'Y':
#         bill += 3
#     if extra_cheese == 'Y':
#         bill += 1
# else:
#     print('Invalid input')
#
# print(f'Your bill is {bill}$ ')

# print('Welcome to the treasure island')
#
# road_direction = input('Your mission is to find the treasure. You are at the cross road. Where do you want to go? \n Type "left" or "right". \n').lower()
#
#
# if road_direction != "left":
#     print('You fell into a hole. Game Over!')
# else:
#     print('You have come to lake. There is island in the middle of the lake.')
#     swim = input('Type "wait" to wait for the boat. Type "swim" to swim across. \n')
#     if swim != "wait":
#         print('You were attacked by trout. Game Over!')
#     else:
#         print('You have arrived at the island unharmed. There is a house with 3 doors.')
#         door = input('One red, one yellow and one blue. Which colour do you choose?\n')
#         if door == 'red':
#             print('Burned By fire. Game Over!')
#         elif door == 'Blue':
#             print('Eaten by beasts. Game Over!')
#         elif door == 'yellow':
#             print('You have found treasure. You Win!')

import random

# random_integer = random.randint(1,100)
# print(random_integer)

# random_number = random.random()
#
# if random_number < 0.5:
#     print('Heads')
# else:
#     print('Tails')

# random_integer = random.randint(0, 1)
#
# if random_integer == 1:
#     print("Tails")
# else:
#     print("Heads")

# friend = ['Gela', 'Gocha', 'Gia', 'Vaxushti', 'Tamazi']
#
# random_list_index = random.randint(0, len(friend) - 1)
#
# random_choice = random.choice(friend)
#
# print(random_choice)

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# rock_paper_scissors = [rock, paper, scissors]
#
# your_choice = input('Type 0 for rock, 1 for paper, 2 for scissors: ')
#
# computer_choice = random.choice(rock_paper_scissors)
#
# print(f'Your Choice \n{rock_paper_scissors[int(your_choice)]} \n Computers Choice \n {computer_choice}')
#
# if rock_paper_scissors[int(your_choice)] == computer_choice:
#     print("It's a tie!")
# elif your_choice == '0' and computer_choice == scissors or your_choice == '1' and computer_choice == rock or your_choice == '2' and computer_choice == paper:
#     print('You Won!')
# else:
#     print("You Lost!")


# student_scores = [100, 45, 11, 50,30,150, 20, 22, 96, 101, 9, 10]
#
# highest_score = 0
#
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
#
# print(highest_score)

#Password Generator Project
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# password = []
# result = ""
#
# for letter in range (0, nr_letters):
#     password.append(random.choice(letters))
#
# for symbol in range(0, nr_symbols):
#     password.append(random.choice(symbols))
#
#
# for number in range(0, nr_numbers):
#     password.append(random.choice(numbers))
#
#
# for item in range(0, len(password)):
#     a = random.randint(0, len(password) - 1)
#     b = random.randint(0, len(password) - 1)
#
#     password[a], password[b] = password[b], password[a]
#
# for item in password:
#     result += item
#
# print(result)


