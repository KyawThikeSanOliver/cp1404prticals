"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

MIN_SCORE = 0
MAX_SCORE = 100
EXCELLENT_SCORE = 90
PASS_SCORE = 50

score = float(input("Enter score: "))

if score >= MIN_SCORE or score <= MAX_SCORE:
    if score >= EXCELLENT_SCORE:
        print("EXCELLENT")
    elif score >= PASS_SCORE:
        print("PASS")
    else:
        print("BAD")
else:
    print("Invalid score")
