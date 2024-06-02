"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
# Import
import random

# Constants
MIN_SCORE = 0
MAX_SCORE = 100
EXCELLENT_SCORE = 90
PASS_SCORE = 50


def main():

    score = float(input("Enter score: "))
    print(determining_results_score(score))

    # Generate a random score and print the result
    random_score = random.uniform(MIN_SCORE, MAX_SCORE)
    result = determining_results_score(random_score)
    print(f"Random Score: {random_score}, Result: {result}")


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
