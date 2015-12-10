def get_product_of_all_ints_except_at_index(L):
    new_list =[]
    for x in L:
        j = 1
        for y in L:
            if y!=x:
                j = j*y
        new_list.append(j)
    return new_list
                
    
