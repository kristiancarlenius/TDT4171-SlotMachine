import random
options = ["Bar", "Lemon", "Cherry", "Bell"]
liste = []
for i in range(1000000):
    coins = 10
    rounde = 0
    while(coins>0):
        rounde += 1
        coins -= 1
        wheel1 = options[random.randint(0, 3)]
        wheel2 = options[random.randint(0, 3)]
        wheel3 = options[random.randint(0, 3)]
        if(wheel1==wheel2==wheel3=="Bar"):
            win = 20
        elif(wheel1==wheel2==wheel3=="Bell"):
            win = 15
        elif(wheel1==wheel2==wheel3=="Lemon"):
            win = 5
        elif(wheel1==wheel2==wheel3=="Cherry"):
            win = 3
        elif(wheel1==wheel2=="Cherry"):
            win = 2
        elif(wheel1=="Cherry"):
            win = 1
        else:
            win = 0
        coins += win
        #print("Round", rounde, " |", wheel1, wheel2, wheel3, "| Wow this gives:", win, " in winnings. Total coins is now at:", coins)
    liste.append(rounde)
liste = sorted(liste)
print("liste-len:", len(liste), "max:", max(liste), "avg():", sum(liste)/len(liste), "median:", liste[int(len(liste)/2)] )


    

