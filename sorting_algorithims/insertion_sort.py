#Will Bowditch
#Insertion Sort

##Insertion sort iterates, consuming one input element each
##repetition, and growing a sorted output list. Each iteration,
##insertion sort removes one element from the input data, finds the
##location it belongs within the sorted list, and inserts it there. It
##repeats until no input elements remain.

##Suppose there exists a function called Insert designed to insert a
##value into a sorted sequence at the beginning of an array. It operates
##by beginning at the end of the sequence and shifting each element one
##place to the right until a suitable position is found for the new
##element. The function has the side effect of overwriting the value
##stored immediately after the sorted sequence in the array.
##
##To perform an insertion sort, begin at the left-most element of the
##array and invoke Insert to insert each element encountered into its
##correct position. The ordered sequence into which the element is
##inserted is stored at the beginning of the array in the set of indices
##already examined. Each insertion overwrites a single value: the value
##being inserted.

def insertion_sort(arr):
    for index in range(1,len(arr)):
        #current_value = arr[index]

        position = index
        while (position>0 and (arr[position-1] > arr[position])):
            temp = arr[position]
            arr[position] = arr[position-1]
            arr[position-1] = temp
            position=position-1
    return arr

#arr = [64, 25, 12, 22, 11]
arr = [4,6,2,7,2,4,6,8,3,6,66,3,4,7]
print insertion_sort(arr)
            
