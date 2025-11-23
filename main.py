import random


def validate_input(user_guess):
    if not user_guess.isdigit():
        print("invalid input. please try again")
        return False
    
    user_guess = int(user_guess)
    if user_guess > 100 or user_guess < 1:
        print("you guess is out of range. please try again. guess should be between 1 and 100.")
        return False
    return True


def main():
    rand_num = random.randint(1, 100)

    score = 100

    while True:
        user_guess = input("Guess a number between 1 and 100: ")
        if user_guess == 'q':
            print("thank you for playing. goodbye!")
            break

        if not validate_input(user_guess):
            continue

        user_guess = int(user_guess)
    
        if rand_num > user_guess:
            print("your guess is too low. please try again.")
        elif rand_num < user_guess:
            print("your guess is too high. please try again.")
        else:
            print("congratulation!. you guess the correct number!")
            print(f"your score is: {score}")
            break
    
        score -= 10
        score = max(score, 0)

if __name__ == '__main__' :

    while True:
        main()
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == 'y':
            continue
        elif play_again.lower() == 'n':
            print("Goodbye!")
            break