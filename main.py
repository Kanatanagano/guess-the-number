import random

def guessTheNumber():
    n = int(input("please enter mininum number : "))
    m = int(input("please enter maximum number : "))

    while n > m:
        print("The mininum number should be less than or equal to the maximun number.")
        n = int(input("please enter mininum number again: "))
        m = int(input("please enter maximum number again: "))
    
    targetNumber = random.randint(n, m)
    maxAttempts = 5


    for attempt in range(maxAttempts):
        guess = int(input(f"Enter a number between {n} and {m}: "))

        if guess == targetNumber:
            print(f"Correct! You guessed it in {attempt + 1} attempts.")
            break
        else:
            print("Incorrect. please try again.")
    else:
        print(f"the correct answer was {targetNumber}.")
    3
guessTheNumber()