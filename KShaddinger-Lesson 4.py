import random   # to use the random number generator

# ask user to pick rock, paper, or scissors
def get_user_weapon():
    print("SELECT YOUR WEAPON (1-3):")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = int(input("Enter your weapon: "))
    while choice < 1 or choice > 3:
        print("Please enter 1, 2, or 3.")
        choice = int(input("Enter your weapon: "))
    return choice

# computer picks a random weapon
def get_opponent_weapon():
    weapon = random.randrange(1, 4)
    return weapon

# decide who wins (using only if and else)
def determine_winner(user_weapon, opponent_weapon):
    if user_weapon == opponent_weapon:
        print("It's a tie!")
    else:
        # Rock = 1, Paper = 2, Scissors = 3
        if user_weapon == 1 and opponent_weapon == 3:
            print("You win, rock crushes scissors!")
        else:
            if user_weapon == 2 and opponent_weapon == 1:
                print("You win, paper covers rock!")
            else:
                if user_weapon == 3 and opponent_weapon == 2:
                    print("You win, scissors cuts paper!")
                else:
                    print("You lose!")

# main function to run the game
def main():
    play_again = "y"
    while play_again == "y":
        user_weapon = get_user_weapon()
        opponent_weapon = get_opponent_weapon()
        determine_winner(user_weapon, opponent_weapon)
        play_again = input("Want to play again (y/n): ")
    print("Completed by, Kari Shaddinger")

# call main function correctly
if __name__ == "__main__":
    main()
