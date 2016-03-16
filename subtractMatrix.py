#Will Bowditch
#Write a function called subtractMatrix (L, M) that receives two matrices L and
#M, and returns a matrix S that represents the result of L minus M. Both
#matrices are represented as nested lists and you can assume they are of the
#same size.

def subtractMatrix(arr1,arr2):
    difference = []
    for x in range(len(arr1)):
        sub = []
        for y in range(len(arr1[x])):
            sub.append(arr1[x][y]-arr2[x][y])
        difference.append(sub)
    return difference

L = [ [ 5, 2] , [8, 4] , [3,2] ]

M = [[2,6], [4,2],[2,1]]


print subtractMatrix(L,M)