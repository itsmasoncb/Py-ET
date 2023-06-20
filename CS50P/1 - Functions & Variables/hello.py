# Ask user for name
name = input("What's your name? ").strip().title()

# Remove whitespace from str, and capitalize user's name, combined with above.
# name = name.strip().title()

# Split users name into first and last.
first, last = name.split(" ")

# Say hello to user
# print("hello, ", end="")  # Overwrite default end='\n' for new line with nothing.
print(f"Hello, {first}")
