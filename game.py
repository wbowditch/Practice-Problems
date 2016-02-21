#Will Bowditch
#Lab Solutions 3

def valid(x,y,z):
    if(1<=x<=10 and 1<=y<=10 and 1<=z<=10):
        return True
    return False

def score(x,y,z):
    if(x!=y and x!=z and y!=z):
        return x+y+z
    elif(x==y and x==z and y==z):
        return (x+y+z)*3
    else:
        return (x+y+z)*2
    
x=int(raw_input('Enter x: '))
y=int(raw_input('Enter y: '))
z=int(raw_input('Enter z: '))

if(valid(x,y,z)):
    print "Your score is: ",score(x,y,z)
else:
    print "Invalid inputs."
    
