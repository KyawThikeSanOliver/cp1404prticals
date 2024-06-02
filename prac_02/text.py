import random
menu = "(G)et a valid score\n(P)rint Result\n(S)how Stars\n(Q)uit"
print(menu)

user_choice = input(str("What's your choice?: ")).lower()
while user_choice != "q":
    if user_choice == "g":
        random_score = random.uniform(MIN_SCORE, MAX_SCORE)

