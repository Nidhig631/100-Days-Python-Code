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

game_imges = [rock, paper, scissors]
user_input = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
if user_input >= 3 or user_input < 0:
    print("loss game invalid number")
else:    
    print(game_imges[user_input])
    computer_choice = random.randint(0,2)
    print("computer choice:")
    print(game_imges[computer_choice])


    if user_input ==0 and computer_choice ==2:
        print("You wins!")
    elif computer_choice > user_input:
        print("You lose!")
    elif computer_choice < user_input:
        print("You Win!")    
    elif computer_choice == user_input:
        print("It's a draw")
    elif computer_choice == 0  and user_input ==2:
        print("you lose!")      
    elif user_input >= 3 and user_input < 0:
        print("loss game invalid number")


