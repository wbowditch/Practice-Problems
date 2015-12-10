#Will Bowditch
#Quick Sort

##Like merge sort, quicksort uses divide-and-conquer, and so it's a
##recursive algorithm. The way that quicksort uses divide-and-conquer is
##a little different from how merge sort does. In merge sort, the divide
##step does hardly anything, and all the real work happens in the
##combine step. Quicksort is the opposite: all the real work happens in
##the divide step. In fact, the combine step in quicksort does
##absolutely nothing

##And its worst-case running time is as bad as selection sort's and
##insertion sort's: Θ n 2 Θ(n ​2 ​​ ). But its average-case running time
##is as good as merge sort's: Θ n lg n Θ(nlgn). So why think about
##quicksort when merge sort is at least as good? That's because the
##constant factor hidden in the big-Θ notation for quicksort is quite
##good. In practice, quicksort outperforms merge sort, and it
##significantly outperforms selection sort and insertion sort.v

##Mathematical analysis of quicksort shows that, on average, the
##algorithm takes O(n log n) comparisons to sort n items. In the worst
##case, it makes O(n2) comparisons, though this behavior is rare.

def quicksort(arr):
   # print arr
    if (len(arr)<1 or len(arr)==2 and arr[0]<arr[1]): return arr
    pivot = arr[len(arr)-1]
    for x in range(len(arr)-2):
        if arr[x] != pivot:
            if arr[x]>pivot:
                a = arr.pop(x)
                arr.append(a)
            else:
                a = arr.pop(x)
                arr.insert(0,a)
    #print arr
    pivot_index = arr.index(pivot)
    
    first_half = arr[:pivot_index]
    second_half = arr[pivot_index:]

    first_sorted = quicksort(first_half)
    second_sorted = quicksort(second_half)
    print first_sorted
    return first_sorted + second_sorted

def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array


        


arr = [4,6,2,5,2,4,6,8,3,6,66,3,4,7]
#print len(arr)
print sort(arr)
    
        
