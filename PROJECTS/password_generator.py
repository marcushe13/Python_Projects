import string
import random

pass_length = int(input("Insert desired password length: "))

# setting password to blank, initializing variable
password = ""

# setting the character bank
char_bank = (
    string.ascii_letters +
    string.ascii_lowercase +
    string. ascii_uppercase +
    string.punctuation
)

# For loop
for _ in range(pass_length):
    password += random.choice(char_bank)

print(f"Your Password is: {password}")

