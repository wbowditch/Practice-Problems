def answer(x):
    if(len(str(x))==1):
        return x
    else:
        str_x = str(x)
        sum = 0
        for digit in str_x:
            sum+= int(digit)
        return answer(sum)

print answer(12345)
