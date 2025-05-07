import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors):")

  options = ["rock","paper","scissors"]
  computer_choice = random.choice(options)

  choices = {"player": player_choice, "computer": computer_choice}
  return choices


def check_win(player,computer):
  print(f" You choose {player}, Computer choose {computer}")

  if player == computer:
    return "Its a Tie" 

  elif player =="rock":
   if computer == "scissors":
    return "Rock smashes scissors! You win!"
   else:
    return "Paper covers rock! You lose."

  elif player =="paper":
   if computer == "rock":
    return "Rock smashes scissors! You win!"
   else:
    return "Scissors cuts Paper! You lose."

  elif player =="scissors":
   if computer == "paper":
    return "Scissors cuts Paper! You win!"
   else:
    return "Rock smashes scissors!,You lose."


choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print (result)