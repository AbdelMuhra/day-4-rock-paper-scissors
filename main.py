#to use the the random functions to generate random computer choice.
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

#create a list to store the rock,paper,scissors ascii images
images = [rock,paper,scissors]

#the user will input a number
user_choice = int(input("Wha do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors\n"))
#use the input as an index to the images
print(images[user_choice])

#generate random computer output
myRandom = random.randint(0,2)
computer_choice = images[myRandom]
print("Computer Chose:\n")
print(computer_choice)

#determine the winner using if/else

if user_choice==myRandom:
  print("Draw")
elif user_choice==0:
  if myRandom==1:
    print("You lose")
  else:
    print("You win")
elif user_choice==1:
  if myRandom==2:
    print("You lose")
  else:
    print("You win")
elif user_choice==2:
  if myRandom==0:
    print("You lose")
  else:
    print("You win")
