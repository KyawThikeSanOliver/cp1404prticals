def main():
    """ Asking the password and checking the input valid variable """
    MIN_PASSWORD_LENGTH = 8
    password = get_password(MIN_PASSWORD_LENGTH)
    print_asterisks(password)


def print_asterisks(password):
    """function for printing the asterisks according to length of the password """
    print('*' * len(password))


def get_password(MIN_PASSWORD_LENGTH):
    """Getting the password then error checking with while loop """
    get_password = input("Enter Your Password:")
    while len(get_password) != MIN_PASSWORD_LENGTH:
        print(f"Password must be at least {MIN_PASSWORD_LENGTH} characters long. Try again.")
        get_password = input("Enter Your Password:")
    return get_password


main()
