
import random
def happybday(n):
    liste = []
    for x in range(10000):
        liste2 = []
        for i in range(n):
            liste2.append(random.randint(1, 365))
        if(len(set(liste2)) != len(liste2)):
            liste.append(1)
        else:
            liste.append(0)
    return sum(liste)/len(liste)
count = 9
while 8<count<50 :
    count += 1
    k = happybday(count)
    print("count:", count, "prob:", k)
