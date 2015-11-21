#Will Bowditch
#Lab 2: Pyramid 
numRows = 5
def pyramid():
    for i in range(1,numRows+1):
        s =""

        for j in range(0,numRows-i):
            s+= " "

        for j in range(i,0,-1):
            s+= str(j)

        for j in range(2,i+1):
            s+= str(j)

        print s
