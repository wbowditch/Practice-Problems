#Will Bowditch
#Minimum number of jumps to reach end

##Given an array of integers where each element represents the max
##number of steps that can be made forward from that element. Write a
##function to return the minimum number of jumps to reach the end of the
##array (starting from the first element). If an element is 0, then
##cannot move through that element.

def minJumps(arr):
    n = len(arr)
    max_int = 999999
    jumps = [0]*n  # jumps[n-1] will hold the result
    if(n==0 or arr[0] == 0):
        #print 1
        return max_int

    jumps[0] = 0

    # Find the minimum number of jumps to reach arr[i]
    # from arr[0] and assign this value to jumps[i]
    for i in range(1,n):
        #print i
        jumps[i] = max_int
        print jumps
        for j in range(0,i):
            if( i<= (j + arr[j]) and jumps[j] != max_int):
                #print 1
                jumps[i] = min(jumps[i],jumps[j]+1)
               # break
    return jumps[n-1]
        
arr = [1, 3, 6, 1, 0, 9]
print minJumps(arr)
