#8.3
import random
import math

def estimatePi(n = 100):
    i = poleKola = poleKw = 0
    r = 1
    while i < n:
        i += 1
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        odl = odlOdSrodka(x, y)
        if odl <= r:
            poleKola += 1
        poleKw += 1
    if poleKw == 0:
        raise ValueError ("Dzielenie przez 0")
    return  (4 * poleKola) / float(poleKw)

def odlOdSrodka(x, y):
    return math.sqrt(math.pow(x, 2) + pow(y, 2))

if __name__ == '__main__':
    number = int(input("Podaj ilosc losowanych punktow do przyblizenia\n(im więcej tym lepsza dokladnosc): "))

    print(estimatePi(number))

  
