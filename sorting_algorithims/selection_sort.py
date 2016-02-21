#Will Bowditch

##The algorithm divides the input list into two parts: the sublist of
##items already sorted, which is built up from left to right at the
##front (left) of the list, and the sublist of items remaining to be
##sorted that occupy the rest of the list. Initially, the sorted sublist
##is empty and the unsorted sublist is the entire input list. The
##algorithm proceeds by finding the smallest (or largest, depending on
##sorting order) element in the unsorted sublist, exchanging (swapping)
##it with the leftmost unsorted element (putting it in sorted order),
##and moving the sublist boundaries one element to the right.

##It has O(n2) time complexity, making it inefficient on large lists,
##and generally performs worse than the similar insertion sort.
##Selection sort is noted for its simplicity, and it has performance
##advantages over more complicated algorithms in certain situations,
##particularly where auxiliary memory is limited.

import sys
def selection_sort(L):
    new_L = []
    while(L):
        min_x = 99999
        for x in L:
            if x<min_x:
                min_x = x
        L.remove(min_x)
        new_L.append(min_x)
    return new_L
        
arr = [64, 25, 12, 22, 11]

print selection_sort(arr)
