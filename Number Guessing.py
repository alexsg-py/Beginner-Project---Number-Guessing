import random

print("Welcome to the number guessing game!")

player_name = input("What is your name? ")
print(f"Hello {player_name}! You have 5 tries to guess the number!")

number_of_tries = 5
guess_counter = 0

random_number = random.randint(0,1000)

guess = int(input())

for _ in range(1, number_of_tries + 1):
    if guess > random_number:
        guess_counter += 1
        print("Lower!")
    elif guess < random_number:
        guess_counter += 1
        print("Higher!")
    elif guess == random_number:
        print(f"Congratulations! You guessed the number with {guess_counter} tries!")

    if guess_counter == 5:
        print(f"You used up all of your tries! The number was {random_number}")
        break
    guess = int(input())






