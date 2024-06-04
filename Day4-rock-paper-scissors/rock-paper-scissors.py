import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps = [rock, paper, scissors]

computer_choice = random.randint(0, 2)

user_choice = int(input('Choose 0 for Rock, 1 for Paper, 2 for Scissors'))
print('You chose:\n', rps[user_choice])
print('Computer chose: \n', rps[computer_choice])

s = ''
if user_choice == computer_choice:
    s = ''
if (user_choice + computer_choice) == 1:
    s = 'win' if user_choice == 1 else 'lose'
if (user_choice - computer_choice) == 2:
    s = 'win' if user_choice == 0 else 'lose'
if user_choice == 0 and computer_choice == 3:
    s = 'win' if user_choice == 2 else 'lose'
print(f'You {s}') if s != '' else print('It\'s a tie')
