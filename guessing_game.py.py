import random

List_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
user_guess_number = int(input("Guess the Number 'From 0 to 10': "))
random_computer_number = random.choice(List_of_numbers)

while  user_guess_number != random_computer_number:
 if user_guess_number > random_computer_number:
    print("Too high")

 elif user_guess_number < random_computer_number:
    print("Too low")
 user_guess_number = int(input("Guess again: "))
print("Congratulations! 🎉 You guessed the correct number!")






