get_bin = lambda x, n: x >= 0 and str(bin(x))[2:].zfill(n) or "-" + str(bin(x))[3:].zfill(n)
output =["0000000001","0000000010","0000000100","0000001000","0000010000","0000100000","0001000000","0010000000","0100000000","1000000000"]
count = 0
index = -1
print get_bin(34,2)
for x in range(15):
    for y in range(10):
        if count%15 ==0:
            index+=1
       # print get_bin(x,4)+"_"+get_bin(y,4)+"_"+output[index]
        count+=1
        
