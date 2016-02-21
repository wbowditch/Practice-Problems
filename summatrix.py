def sumMatrix(L,M):
    sum1 = []
    for i in range(len(L)):
        x = []
        for j in range(len(L[0])):
            output = L[i][j]+M[i][j]
            x.append(output)
        sum1.append(x)
    return sum1
