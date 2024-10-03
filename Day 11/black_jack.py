import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def compare(u_hand, c_hand):
  if calculate_score(u_hand) ==  calculate_score(c_hand):
    print('Its a draw')
  elif calculate_score(u_hand) == 0:
    print('You win. You got the blackjack')
  elif calculate_score(u_hand) > 21:
    print('You lose. You went over 21')
  elif calculate_score(c_hand) > 21:
    print('You win. Computer Went over 21')
  elif calculate_score(u_hand) > calculate_score(computer_hand):
    print('You win. You have more')
  elif calculate_score(u_hand) < calculate_score(c_hand):
    print('You lose computer has more')

def deal_card(hand):
  hand.append(random.choice(cards))

def calculate_score(hand):
  hand_sum = sum(hand)

  if 11 in hand and hand_sum > 21:
    hand.remove(11)
    hand.append(1)

  if hand_sum == 21:
    return 0
  else:
    return hand_sum

def black_jack():
  computer_hand = []
  user_hand = []
  game_over = False

  for _ in range(2):
    deal_card(computer_hand)
    deal_card(user_hand)

  while not game_over:
    if calculate_score(user_hand) == 0 or calculate_score(computer_hand) == 0 or calculate_score(user_hand) > 21:
      game_over = True
    else:
      print(f'Your hand: {user_hand}. Your score is: {calculate_score(user_hand)}')
      print(f'Computer hand: {computer_hand[0]}')
      ask_deal_card = input("Do you want to add a card? y or n: ").lower()
      if ask_deal_card == 'y':
        deal_card(user_hand)
      else:
        game_over = True

  while calculate_score(computer_hand) < 17 and calculate_score(computer_hand) != 0:
    deal_card(computer_hand)

  print(f'Your hand: {user_hand}. Your score is: {calculate_score(user_hand)}')
  print(f'Computer hand: {computer_hand}. Computer score is: {calculate_score(computer_hand)}')
  compare(user_hand, computer_hand)
  play_again = input('Do you want to play again? y or no: ').lower()
  return play_again

while black_jack() == "y":
  black_jack()