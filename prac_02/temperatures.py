"""
CP1404/CP5632 - Practical
temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def celsius_to_fahrenheit(celsius):
    """Simple Calculation of celsius to fahrenheit"""

    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    """Simple Calculation of fahrenheit to celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        celsius_to_fahrenheit(fahrenheit)
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        # TODO: Write this section to convert F to C and display the result
        fahrenheit = float(input("fahrenheit: "))
        fahrenheit_to_celsius(fahrenheit)
        print(f"Result: {celsius:.2f} C")

    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
