#11.1
import random
import math

def losowe_liczby(N):
    L = []
    for i in range(0, N):
        L.append(random.randint(0, N-1))
    return L

def prawie_posortowana(N):
    L = []
    for i in range(0, N):
        a = i % N
        if a % 2 == 0:
            L.append(a+1)
        else:
            L.append(a-1)
    return L

def prawie_posortowana_odwrotnie(N):
    L = prawie_posortowana(N)
    L.reverse()
    return L

def losowe_gauss(N, mu, sigma):
    L = []
    for x in range(0, N):
        L.append(random.gauss(mu, sigma))
    return L

def losowe_powtarzajace_sie(N):
    L = []
    X = []
    for i in range(0, int(math.sqrt(N))):
        X.append(random.randint(0, int((random.random())*1000)))
    for i in range(0, N):
        L.append(random.choice(X))
    return L

#print(losowe_liczby(9))
#print(prawie_posortowana(9))
#print(prawie_posortowana_odwrotnie(9))
#print(losowe_gauss(1, 9, 1))
#print(losowe_powtarzajace_sie(9))