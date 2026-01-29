import random

def reveal_ans(randd):
    a = input("Do you want to reveal the number? (y/n): ").lower()
    if a == "y":
        print(f"The correct number was: {randd}")
    elif a == "n":
        print("You chose not to reveal the number.")
def asking(user_times):
    if user_times == "easy":
        rand = random.randint(1,15)
        user = int(input("Enter the number of attempts you want: "))
        for i in range(user,0,-1):
            print(f"Attempts remaining: {i}")
            guess = int(input("Enter your guess: "))
            if guess == rand:
                print("Congratulations! You have guessed correctly 🎉")
                return True
            elif guess < rand:
                print("Your guess is lower than the correct number.")
            elif guess > rand:
                print("Your guess is higher than the correct number.")

        reveal_ans(rand)
    elif user_times == "hard":
        rand2 = random.randint(16,70)
        user2 = int(input("Enter the number of attempts you want: "))
        for i in range(user2,0,-1):
            print(f"Attempts remaining: {i}")
            guess = int(input("Enter your guess: "))
            if guess == rand2:
                print("Congratulations! You have guessed correctly 🎉")
                return True
            elif guess < rand2:
                print("Your guess is lower than the correct number.")
            elif guess > rand2:
                print("Your guess is higher than the correct number.")

        reveal_ans(rand2)
times = input("Select difficulty level (easy/hard): ").lower()
asking(times)


