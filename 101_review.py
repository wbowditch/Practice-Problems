#Will Bowditch
#Exam 1 Review Solutions

def reviewone():
    print "3/2+5.0: ",(3/2+5.0),type((3/2+5.0))
    print "2**3/2: ",(2**3/2),type((2**3/2))
    print "'ade' > 'fab'[1:]: ",'ade' > 'fab'[1:],type('ade' > 'fab'[1:])
    print "'ba'*5+'b': ", 'ba'*5+'b', type('ba'*5+'b')
    print "(3*3>7) and (2*3 !=7)",(3*3>7) and (2*3 !=7), type((3*3>7) and (2*3 !=7))
    print "len('abcdef')/3.0",len('abcdef')/3.0,type(len('abcdef')/3.0)
    print "'workbook'[7]+'workbook'[1:6]+'workbook'[0]",'workbook'[7]+'workbook'[1:6]+'workbook'[0],type('workbook'[7]+'workbook'[1:6]+'workbook'[0])

def reviewthree(x):
    y = ''
    for c in x:
        if not(c in 'aeiou'):
            y = y+c
    return y

def reviewfour():
    x = raw_input("x: ")
    result = ((x>9) or (-3<=x<4))
    print result

    
def reviewfive(s):  #Draw out the grid as integers rather than letters (x instead of s[x])
    row = 0         #Label the column and row numbers.
    max = len(s)
    while(row<max):      
        col = 0
        while(col<max):
            if(col>=row):  
                x = row
            else:
                x = col
            print s[x], 
            col+=1
        print
        row+=1

def reviewsix():
    power = 1
    while(power<1000000):
        print power
        power = power*3

def g(n):
    count = 0
    while n%3 ==0:
        n=n/3
        count+=1
    return count

def reviewsixtwo():
    print "x=g(48)-g(36)= ", g(48)-g(36)
    print "The function g(n) returns the highest power of 3 that is a factor of n"


def dist(x1,y1,x2,y2):
    xdiff = x1-x2
    ydiff = y1-y2
    diff_squares = xdiff**2 + ydiff**2
    return float((diff_squares)**1/2)

def reviewseven():
    x1 = float(raw_input('Enter the x coordinate of the first vertex.'))
    y1 = float(raw_input('Enter the y coordinate of the first vertex.'))
    x2 = float(raw_input('Enter the x coordinate of the second vertex.'))
    y2 = float(raw_input('Enter the y coordinate of the second vertex.'))
    x3 = float(raw_input('Enter the x coordinate of the third vertex.'))
    y3 = float(raw_input('Enter the y coordinate of the third vertex.'))
    d1=dist(x1,y1,x2,y2)
    d2=dist(x1,y1,x3,y3)
    d3=dist(x2,y2,x3,y3)
    print d1
    print d2
    print d3
    print min(d1,d2,d3)    

