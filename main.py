import random
import subprocess

def clear_console():
    subprocess.call("clear")

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
