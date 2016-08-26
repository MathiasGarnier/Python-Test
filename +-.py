# -*-coding:Latin-1 -*

import random as rand

gameLoop = True
randomNum = rand.randrange(1000)

while gameLoop:

    print(randomNum)
    choice = int(input("Nombre choisi :"))

    if choice > randomNum: print("<")
    elif choice < randomNum: print(">")
    elif choice == randomNum: gameLoop = False
