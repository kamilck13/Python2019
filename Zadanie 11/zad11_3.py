#11.3
def cmp(number1, number2):
    if number1 > number2:
        return 1
    elif number1 < number2:
        return -1
    return 0

def selectsort(L, left, right, cmpfunc = cmp):
    for i in range(left, right):
        k = i
        for j in range(i+1, right+1):
            if cmpfunc(L[j], L[k]) < 0:
                k = j
        L[i], L[k] = L[k], L[i]

#L = [5,1,3,2,4]
#print(L)
#selectsort(L, 0, 4)
#print(L)