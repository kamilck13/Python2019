#4.5
def odwracanie_rek(L, left, right):
    if(left < right):
        L[left], L[right] = L[right], L[left]
        odwracanie_rek(L, left+1, right-1)
    return L
    
def odwracanie_iter(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left+=1
        right-=1
    return L

if __name__ == "__main__":
    print(odwracanie_rek([1, 2, 3, 4], 0, 2))
    print(odwracanie_iter([1, 2, 3, 4], 0, 2))