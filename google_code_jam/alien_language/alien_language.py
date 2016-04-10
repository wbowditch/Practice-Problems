import re
def alien_language():
    #t = int(raw_input())
    m = [int(s) for s in raw_input().split(" ")]
    d = m[1]
    l = m[0]
    n = m[2]
   # print m
    dct = [raw_input() for _ in range(m[1])]
   # print dct

    for i in range(1,n+1):#each test case
        pattern = raw_input()
       # print pattern
        possible_words = list(dct)
        pattern_list = []
        z = 0
        while(z<len(pattern)):
            if pattern[z] == "(":
                sub = ""
                while(pattern[z]!=")"):
                    sub+=(pattern[z])
                    z+=1
                pattern_list.append(sub)
            else:
                if(pattern[z]!= "(" or pattern[z]!=")"):
                   pattern_list.append(pattern[z])
            z+=1
            
                
        #pattern_list1 = re.findall('\[[^\]]*\]|\([^\)]*\)|\"[^\"]*\"|\S+',pattern)
        #print pattern_list
        #pattern_list = []
    
    
        for index,choice in enumerate(pattern_list):
            letter = [k[index] for k in possible_words]

            possible_words =[word for word in possible_words if word[index] in choice]
        print "Case #{}: {}".format(i, len(possible_words))
    
        

#alien_language()
    
