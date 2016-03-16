#Will Bowditch
#Write a function called flatten (L) that receives a nested list of integers and returns a flatten list.

def flatten(arr):
    result = []
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            result.append(arr[x][y])
    return result




L=[ [5,6,7],[1,2,3],[9] ]

print flatten(L)
