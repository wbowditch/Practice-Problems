def run_length_encoding(word):
    index = 0
    out = ""
    for index2 in range(len(word)+1):
        count = 0
        index2 = index
        if(index2 > len(word)-1): break
        while word[index2] == word[index]:
            count+=1
            index+=1
            if (index > len(word)-1): break
        out = out + str(count) + word[index2]
    return out
        
        
        
            
        
        
            
            


        
    
