import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors):")

  options = ["rock","paper","scissors"]
  computer_choice = random.choice(options)

  choices = {"player": player_choice, "computer": computer_choice}
  
  check_win(choices["player"], choices["computer"])

def check_win(player,computer):
  print(f"You choose {player}, Computer choose {computer}")

  if player == computer:
    print ("Its a Tie") 

  elif player =="rock":
   if computer == "scissors":
    print("Rock smashes scissors! You win!") 
   else:
    print("Paper covers rock! You lose.")

  elif player =="paper":
   if computer == "rock":
    print("Rock smashes scissors! You win!")
   else:
    print("Scissors cuts Paper! You lose.")

  elif player =="scissors":
   if computer == "paper":
    print ("Scissors cuts Paper! You win!")
   else:
    print("Rock smashes scissors!,You lose.") 
