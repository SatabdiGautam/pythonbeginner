from RockPaperScissor import get_choices, check_win

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
