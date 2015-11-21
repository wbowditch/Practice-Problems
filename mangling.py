# -*- coding: utf-8 -*-
def mangle(sentence):
    new_sentence = []
    weird = ["'",'.',',',';','-']
    sentence = sentence.split(' ')
    for word in sentence:
        mangled_word = word.lower()
        pos = []
        for ch in weird:
            if word.find(ch)!=-1:
                print ch
                pos.append(word.find(ch))
        mangled_word = sorted(mangled_word)
        i = -1
        for ch in weird:
            if word.find(ch)!=-1:
                i=0
                mangled_word.remove(ch)
                mangled_word.insert(pos[i],ch)
                i= i+1
        mangled_word= ''.join(mangled_word)  
        if word[0].isupper():
            print word
            mangled_word = mangled_word.title()
        new_sentence.append(mangled_word)
    return ' '.join(new_sentence)
            
