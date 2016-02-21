def longest_common_substring(word1,word2):
    k = []
    j= []
    for x in range(len(word1)+1):
        for y in range(len(word1)+1):
            k.append(word1[x:y])

    k  = filter(lambda a: a != '', k)

    
   # print k
    for x in range(len(word2)+1):
        for y in range(len(word2)+1):
            j.append(word2[x:y])

    j  = filter(lambda a: a != '', j)

    max_word = ""
    max_length = 0
    for word1 in k:
        for word2 in j:
            if word1 == word2:
                if len(word1) > max_length:
                    max_length = len(word1)
                    max_word = word1
    return max_word


    
