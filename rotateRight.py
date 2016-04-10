def smallest(arr):
    print "current array: ",arr
    if len(arr) == 1:
        return arr[0]
    else:
        small = smallest(arr[1:])
        print "current minimum: ",small
        if arr[0]<small:
            return arr[0]
        else:
            return small

print "result: ", smallest([1,2,-4,24423,234243,-10,2423234])


def reverse (L):
       if len(L) == 0 :
              return  [] # if L is empty , just return empty list
       else:
              return  [L[-1]] + reverse ( L[:-1] )


def rotateRight(arr,x):
    if x == 0:
        return arr
    else:
            print arr
            item = arr.pop(-1)
            arr.insert(0,item)
            return rotateRight(arr,x-1)

