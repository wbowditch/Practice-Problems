import string
base_dict = {}

for x in range(10):
    base_dict[x] = x

for ch,y in zip(string.ascii_uppercase,range(10,37)):
    base_dict[y] = ch 
    
def base_converter(num,base):
    return base_converter_helper(num,base,[])

def base_converter_helper(num,base,rem_list):
    if num == 0:
        rem_list.reverse()
        for x in rem_list:
           print x,
        return
      
    else:
        rem = num%base
        
        
        rem_list.append(base_dict[rem])
        return base_converter_helper(num/base,base,rem_list)

    
        
