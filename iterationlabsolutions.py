#Lab Solutions
#Will Bowditch


def problemone():
    x = 20
    while(x>0):
        print x
        x= x-1

def problemtwo():
    x = 0
    n = 1
    while(n<20):
        x= x+(n**2)
        print x
        n= n+1


def problemthree():
    x= 0
    n = 1
    while((x+n**2)<1000000):
        x= x+(n**2)
        print x
        n= n+1

def problemfour():
    x1 = 0
    x2 = 1
    x5 = 0
    x4 = 1
    x3 = 0
    while(x3<100):
        print x4
        x4 = x1 + x2
        x1 = x2
        x2 = x4
        x3 = x3+1

def problemfive():
    x = 1
    while(x<10):
        y = 1
        print '\n',
        while(y<10):
            b=y
            a=x
            print a*b, '\t',
            y = y+1
        print '\n',
        x= x+1

def problemsix():
    x = 0
    row = 1
    while(row<=10):
        col = 1
        while(col <= row):
            x = x+1
            print x,
            col = col+1
        print
        row = row+1



    
        
    
        
        
        
