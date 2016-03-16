#Will Bowditch
#Write a function called rotateRight ( L , x ), which receives a list of elements L and a integer x.
#The function should rotate the elements in the list rightward x positions.
#By “rotate” we mean that the elements that fall of the right (end of the list) will move to the left
#(front of the list).

def rotateRight(arr,n):
    for x in range(n):
        arr.insert(0,arr.pop(len(arr)-1))
        print arr
    return arr


arr = [1,2,3,4,5,6]
n = 4

print rotateRight(arr,n)
