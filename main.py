import random

def play_game():
    random_number = random.randint(1, 10)
    print("I chose a number between one and ten. Guess it!\n")

    while True:
        x = input()
        try:
            x = int(x)

            if (x == random_number):
                print("Congratulations!")
                break
            else:
                if (x < random_number):
                    print("Too low!\n")
                elif (x > random_number):
                    print("Too high!\n") 

        except ValueError:
            print("Only numbers are allowed!\n")

def start_service():
    answer = "Y"

    while (answer != "n"):
        play_game()
        answer = input("You want to quit? Type n to quit the game. Otherweise continue with any letter!\n")


    print("Thanks for playing!")


start_service()
