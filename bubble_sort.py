def bubble_sort(L):
    for x in range(len(L),0,-1):
        for y in range(0,x-1):
            if L[y]>L[y+1]:
                temp = L[y]
                L[y] = L[y+1]
                L[y+1] = temp
    return L
                
