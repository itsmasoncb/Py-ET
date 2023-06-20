def main():
    # Asks user for input.
    name = input("What is your name? ")

    # Calls defined function, takes name input, uses it for "to" above.
    hello(name)


# Define here takes the parameter of "to" and fills it with input name below.
def hello(to="world"):
    print("Hello,", to)


main()
