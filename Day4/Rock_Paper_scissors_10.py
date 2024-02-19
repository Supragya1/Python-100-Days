import secrets
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
print("Welcome to Rock, Paper, Scissors")
print("You are playing against the computer")
print("You can choose Rock, Paper or Scissors")
list1 = [rock, paper, scissors]
choice = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors\n"))
comp = secrets.randbelow(3) + 1 
if(choice < 1 or choice > 3):
    print("Invalid Choice")
    print("Please select the correct choice")
    exit()
print(list1[choice-1])
print("You chose")
print(list1[comp-1])
print("Computer chose")
if(choice == comp):
    print("It's a tie")
elif(choice == 1 and comp == 2):
    print("You lose")
elif(choice == 1 and comp == 3):
    print("You win")
elif(choice == 2 and comp == 1):
    print("You win")
elif(choice == 2 and comp == 3):
    print("You lose")
elif(choice == 3 and comp == 1):
    print("You lose")
elif(choice == 3 and comp == 2):
    print("You win")

