# Floating point numbers, input for both.
x = float(input("What's x? "))
y = float(input("What's y? "))

# z for rounded default of x + y, can specify.
z = round(x + y)

# f-string, print z from above and format to have a comma.
print(f"{z:,}")
