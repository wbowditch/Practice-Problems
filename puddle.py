#Will Bowditch
def puddle(walls):
    volume = left_max = right_max = left = 0
    right = len(walls) -1
    while(left<right):
        if walls[left] > left_max:
            left_max = walls[left]
        if walls[right] > right_max:
            right_max = walls[right]
        if(left_max>= right_max):
            volume += right_max-land_right
            right-=1
        else:
            volume+= left_max-walls[left]
            left+=1;

    return volume


print puddle([1,7,1,4,2,6,1,6,1,1,1,1,9,1,9])