import random

def play_game():
    random_zahl = random.randint(1, 10)
    print("Ich habe eine Zahl zwischen 1 bis 10 ausgesucht. Raten sie, welche es ist!\n")

    while True:
        x = input()
        try:
            x = int(x)

            if (x == random_zahl):
                print("Herzlichen Glückwunsch!")
                break
            else:
                if (x < random_zahl):
                    print("Die Schätzung ist kleiner als die zu erratende Zahl!\n")
                elif (x > random_zahl):
                    print("Die Schätzung ist größer als die zu erratende Zahl!\n") 

        except ValueError:
            print("Bitte geben sie eine Zahl ein!\n")

def start_service():
    answer = input("You want to quit? Type n to quit the game. Otherweise continue with any letter!\n")

    while (answer != "n"):
        play_game()
        answer = input("You want to quit? Type n to quit the game. Otherweise continue with any letter!\n")


    print("Thanks for playing!")


start_service()
