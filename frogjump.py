def frog_jump2(a,x,d):
    #jump = 3
    time = 0
    L = [0] * (x+1)
    F = 0 #position F is the furthest place you can reach with the avaliable leaves at the next step
    #for time,position in enumerate(a):
    count = 0
    for position in a:
        print time, position, F
        print L
        L[position] = 1
        if F+d >= x:
            print "done"
            return time-1
        
        if F < position and (F + d) >= position:
            F = position
            print L
            for i in range(len(L)):
                if L[i] ==1:
                    if i > F and (F+d) >= i:
                        print i, F
                        F = i
                        #time+=1
        time+=1
    if F + d >= x:
        return time-1
    return 0
            #L[time_arr[x]] = F
        


# Expected Time O(N) Space O(X)
def frog_jump(a,x,d):
    if x <= d:
        return 0
    mid_low = 0
    mid_high = 0
    last_position = 0

    for time, position in enumerate(a):
    #a.each_with_index do |position, time|
        if position > last_position and (position - last_position) <= d:
            last_position = position
        elif x > position and (x - position) <= d:
            x = position
        elif position > last_position and position < x:
            if not mid_low and not mid_high:
                mid_low = position
                mid_high = position
        else:
            if position > mid_high and (position - mid_high) <= d:
                mid_high = position
            elif position < mid_low and (mid_low - position) <= d:
                mid_low = position
        
    #puts "start: #{last_position} mid: #{mid_low} #{mid_high} dest: #{x}"

    # check for solution
    if not mid_low or not mid_high:
        if (x - last_position) <= d:
            return time
    elif (mid_low - last_position) <= d and (x - mid_high) <= d:
        return time
    return -1

##def frog_jump3(a,x,d):
##    if x<=d:
##        return 0
##    max_pos = 0
##    time = 0
##    for index, leaf_pos in enumerate(a):
##        if

#a = [1,3,5,10,7,9]
#x = 12
#d= 2
#a=[12,10,8,6,4,2]

a = [1,3,5,7,10,5]
x = 9
d =3


