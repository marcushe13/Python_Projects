import random

print("Hello! Please Choose a random number (1-100)")
random_number = random.randint(1,100)
guess = int(input())

print()
print(f"Your Guess: {guess}")
print(f"The Number Was: {random_number}")

if guess == random_number:
    print("Congrats! You got the number.")
else:
    print("Nice try!")

