"""
CP1404/CP5632 - Practical 2
Score menu
"""

# Import
import random

# Constants
MIN_SCORE = 0
MAX_SCORE = 100
EXCELLENT_SCORE = 90
PASS_SCORE = 50


def main():
    score = score_validation()
    menu = "(G)et a valid score\n(P)rint Result\n(S)how Stars\n(Q)uit"
    print(menu)
    user_choice = input(str("What's your choice?: ")).lower()
    while user_choice != "q":
        if user_choice == "g":
            print(getting_random_valid_score())
        elif user_choice == "p":
            print(f"Your Score is {determining_results_score(score)}."
                  f"Your Random Score is {determining_results_score(getting_random_valid_score())}")
        elif user_choice == "s":
            print('*' * score)
        else:
            print("Invalid choice ")
        user_choice = input(str("What's your choice?: ")).lower()


def getting_random_valid_score():
    random_score = random.uniform(MIN_SCORE, MAX_SCORE)
    return random_score


def score_validation():
    score = int(input("Enter score: "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("Invalid Score")
        score = float(input("Enter score: "))
    return score


def determining_results_score(score):
    """Getting Results according to the CONSTANTS parameter"""
    if score >= MIN_SCORE or score <= MAX_SCORE:
        if score >= EXCELLENT_SCORE:
            result_score = "Excellent"
        elif score >= PASS_SCORE:
            result_score = "PASS"
        else:
            result_score = "BAD"
    else:
        result_score = "Invalid score"

    return result_score


main()
