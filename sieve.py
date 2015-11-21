def sieve(n):
    prime_list = []
    number_list = list(range(2,n+1))
    for x in number_list:
        for y in number_list:
            if y%x==0 and y!=x:
                number_list.remove(y)
    return number_list
    
    
