import random

# Function to generate a random number within a given range
def generate_random_number(start, end):
    return random.randint(start, end)

# Function to check if the user wants to generate another random number
def continue_generation():
    while True:
        choice = input("Do you want to generate another random number? (y/n): ")
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

# Main program
print("Welcome to the Random Number Generator!")
while True:
    start = int(input("Enter the start value of the range: "))
    end = int(input("Enter the end value of the range: "))

    if start >= end:
        print("Start value must be less than end value. Please try again.")
    else:
        random_num = generate_random_number(start, end)
        print("Random number generated:", random_num)

        if not continue_generation():
            print("Thank you for using the Random Number Generator. Goodbye!")
            break
