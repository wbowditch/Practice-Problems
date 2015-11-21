def ED(word1,word2):
    distance = 0
    for x in range(min(len(word1),len(word2))):
        print x
        if word1[x] != word2[x]:
            distance+=1
            word2 = word2.replace(word2[x],word1[x])

    distance+= abs(len(word1)-len(word2))
    print word2
    return distance


def phrase_count(word1):
    d ={}
    the_list = word1.split()
    for word in the_list:
        if word not in d:
            d[word] = 1
        else:
            d[word]+=1
    for key in d:
        print "Phrase: ",key
        print "Count: ",d[key]
        print
    
        
        


    # so are you supposed to give it a word and a phrase in the word?


        
