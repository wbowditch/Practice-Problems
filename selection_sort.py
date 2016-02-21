import sys
def selection_sort(L):
    new_L = []
    min_x = 99999
    while(L):
        for x in range(len(L)+1):
            if L[x]<min_x:
                min_x = L[x]
        print L
        print min_x
        L.remove(min_x)
        new_L.add(min_x)
    return new_L

