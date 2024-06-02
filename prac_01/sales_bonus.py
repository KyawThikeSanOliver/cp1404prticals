BONUS_MARGIN = 1000
MIN_BONUS = 0.1
MAX_BONUS = 0.15

sales = float(input("Enter sales:$"))

while sales >= 0:
    if sales >= BONUS_MARGIN:
        bonus = sales * MAX_BONUS
    else:
        bonus = sales * MIN_BONUS
    print("Your Bonus is $", bonus)
    sales = float(input("Enter sales:$"))