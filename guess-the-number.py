import random

def value_pick():
    return random.randint(0,100)

def play_round(value):
    try_count = 0

    while True:
        try:
            guess = int(input("Enter value from 0 to 100: "))
        except ValueError:
            print("Value needs to be a whole number!")
            continue

        try_count += 1

        if guess == value:
            print(f"Success! You correctly guessed the value {value}! You needed {try_count} attempt{'s' if try_count > 1 else ''}")
            break
        elif guess < value:
            print(f"Your guess {guess} is lower than the expected value")
        else:
            print(f"Your guess {guess} is higher than the expected value")


value = value_pick()
play_round(value)
