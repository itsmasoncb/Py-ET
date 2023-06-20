# Define main function, goal of printing the square of number x.
def main():
    x = int(input("What's x"))
    print("x square is", square(x))


# Define square function called above as number n, n passes return value to main.
def square(n):
    return n * n


# Calls main to get square.
main()
