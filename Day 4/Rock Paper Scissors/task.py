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
print("Welcome to Rock, Paper, Scissors!\nHere you will battle against the CPU!")
game_list = [rock, paper, scissors]

user_choice = int(input("Press 0 for rock, 1 for paper, and 2 for scissors: "))
if user_choice == 0:
    print("You choose\n" + game_list[user_choice])
elif user_choice == 1:
    print("You choose\n" + paper + ":")
else:
    print("You choose\n" +scissors + ":")

cpu_choice = (random.randint(0,2))
print(f"CPU chose: {cpu_choice}" + game_list[cpu_choice])

if user_choice == 0 and cpu_choice == 2:
    print("You won!\nRock smashes Scissors!")
elif user_choice == 0 and cpu_choice == 1:
    print("CPU wins!\nPaper beats Rock!")
elif user_choice == 0 and cpu_choice == 0:
    print("It's a draw!")
elif user_choice == 1 and cpu_choice == 1:
    print("It's a draw!")
elif user_choice == 1 and cpu_choice == 0:
    print("You win!\nPaper beats Rock!")
elif user_choice == 1 and cpu_choice == 2:
    print("CPU wins!\nScissors cuts Paper!")
elif user_choice == 2 and cpu_choice == 1:
    print("You win!\nScissors cuts paper!")
elif user_choice == 2 and cpu_choice == 0:
    print("CPU wins!\nRock smashes scissors!")
else:
    print("It's a draw!")
