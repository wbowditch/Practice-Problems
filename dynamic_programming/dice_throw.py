#Will Bowditch
#Dynamic Programming | Set 30 (Dice Throw)

#Given n dice each with m faces, numbered from 1 to m, find the number
#of ways to get sum X. X is the summation of values on each face when
#all the dice are thrown.

#The main function that returns number of ways to get sum 'x'
#with 'n' dice and 'm' with m faces.

def findWays(m,n,x):
##    Create a table to store results of subproblems.  One extra 
##    // row and column are used for simpilicity (Number of dice
##    // is directly used as row index and sum is directly used
##    // as column index).  The entries in 0th row and 0th column
##    // are never used.

##    table = [0]*(n+1)
##    for y in table:
##        y = [0]*(x+1)
##
##    j = 1
    table = [[0 for z in range(x+1)] for z in range(n+1)]
    j = 1
    #print table
    while(j<=m and j<=x):  #table entries for only one dice
        table[1][j] =1
        j+=1
    #print table
    #Fill rest of the entries in table using recurse relation
    #i: number of dice, z: sum


    for i in range(2,n+1):
        #print table
        for z in range(1,x+1):
            k =1
            while(k<=m and k<=z):
                table[i][z] += table[i-1][z-k]
                k+=1
            print table
    print 
    return table[n][x]

