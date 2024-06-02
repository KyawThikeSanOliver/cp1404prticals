user_name = input("Enter name:")

MENU = """(H)ello
(G)oodbye
(Q)uit"""
print(MENU)

user_choice = input(">>>").lower()
while user_choice != "q":
    if user_choice == "h":
        print(f"Hello {user_name}")
    elif user_choice == "g":
        print(f"Good Bye {user_name}")
    else:
        print("Invalid Choice")
    print(MENU)
    user_choice = input(">>>").lower()
print("Finished")