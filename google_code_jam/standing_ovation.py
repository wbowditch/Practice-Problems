def standing_ovation():

    t = int(raw_input())  # read a line with a single integer
   # print t
    
    for i in xrange(1, t + 1):
        guests = 0 #start with ideally no guests
        m = [s for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
        max_shyness = m[0] #the maximum level of shyness, is this needed? 
        shynesslist = [int(j) for j in str(m[1])] #list of shyness levels
        standing = shynesslist[0] #people already standing, no need to mess with these guyus
       
        for index,count in enumerate(shynesslist[1:]): #start at index(level), 1
            people_needed = (index+1 - (standing))
            if (people_needed<0 or count==0):
                people_needed = 0 #people needed = (this shyness level - people_already standing and previous guests)
            guests+=people_needed
            standing+=(people_needed+count) #now standing are
           # print standing
            if(standing>max_shyness):
                break
        
        print "Case #{}: {}".format(i, guests)
      ## check out .format's specification for more formatting options

standing_ovation()
