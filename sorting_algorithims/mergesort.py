#Will Bowditch
#Merge Sort

#first break the list into two smaller lists
#of roughly the same size, and then use merge sort recursively on the
#subproblems, until they cannot subdivide anymore (i.e. when they
#contain zero or one elements). Then, we can merge by stepping through
#the lists in linear time.
def mergesort(arr): #O(nlogn) time, requires O(n)
    if (len(arr)<2): return arr
    first_half = arr[:len(arr)/2]
    second_half = arr[len(arr)/2:]
    #print first_half
    #print second_half

    sorted_first = mergesort(first_half)
    sorted_second = mergesort(second_half)

    return merge(sorted_first,sorted_second)

def merge(a,b):
    c = []
    #print c
    while len(a)>0 and len(b)>0:
        if a[0] < b[0]:
            c.append(a[0])
            a.pop(0)
        else:
            c.append(b[0])
            b.pop(0)
    while len(a)>0:
        c.append(a[0])
        a.pop(0)
    while len(b)>0:
        c.append(b[0])
        b.pop(0)
    print c
    return c


arr = [4,6,2,7,2,4,6,8,3,6,66,3,4,7]
#print len(arr)
print mergesort(arr)
    
            
    
