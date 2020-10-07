# Guessing Game
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Enter your guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You Won!")
        break
else:
    print("Try again")



