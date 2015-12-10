#Will Bowditch
#bubble sort

##The bubble sort makes multiple passes through a list. It compares
##adjacent items and exchanges those that are out of order. Each pass
##through the list places the next largest value in its proper place. In
##essence, each item “bubbles” up to the location where it belongs.

def bubble_sort(L):
    for x in range(len(L),0,-1):
        for y in range(0,x-1):
            if L[y]>L[y+1]:
                temp = L[y]
                L[y] = L[y+1]
                L[y+1] = temp
    return L
                
