import random
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
correct_number = random.choice(numbers)
number_choice = int(input("Enter a number: "))
if number_choice == correct_number:
    print("You won!")
else:
    print("You lost!Correct number was: ", correct_number)

