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
    x = 0
    n = 1
    while(x+n**2<1000000):
        x= x+(n**2)
        print x
        n= n+1

def nestedloop():
    row = 0
   
    x=0
    while(row<10):
        col = 0 
        while(col<10):
            x+=1
            print x,
            col+=1
        row+=1
        print


def reviewfour():
    x = raw_input("x: ")


def g(n):
    count = 0
    while n%3 ==0:
        n=n/3
        count+=1
    return count

def reviewsixtwo():
    print "x=g(48)-g(36)= ", g(48)-g(36)
    print "The function g(n) returns the highest power of 3 that is a factor of n"
