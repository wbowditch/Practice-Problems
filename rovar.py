# -*- coding: utf-8 -*-
u"/ËstraÉªkÉªÅ/"
import re
def rovar(word):
    others = ['a','e','i','o','u','y','ö','å','å',' ','.','!',',',"'",'A','E','I','O','U','Ö','Ä','Å','Y']
    trans = ""
    for ch in word:
        trans = trans + ch
        if ch not in others:
            trans = trans + 'o'+ ch.lower()
    return trans


def rovar_decode(rov_word):
    others = ['a','e','i','o','u','y','ö','å','å',' ','.','!',',',"'",'A','E','I','O','U','Ö','Ä','Å','Y']
    decode = ""
    rov_iter = iter(rov_word)
    for ch in rov_iter:
        #print ch
        #print ch_index
        decode = decode + ch
        if rov_iter not in others:
            #print rov_iter.getitem()
            #print decode
            next(rov_iter,None)
            next(rov_iter,None)
    if(rov_word.endswith('o')):
       decode = decode + 'o'
    return decode 
            
    
