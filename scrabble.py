from Tkinter import *

def getwordlist():
    f=open('sowpods.txt','r')
    wl=[]
    for line in f:
        wl.append(line[:len(line)-1])
    return wl

#####PART A######
word_list = getwordlist()
length = len(word_list)
print "(a) There are", length,"words in the dictionary"

#####PART B######
max_length = len(max(word_list, key = len))
print "(b) Length of the longest word in the dictionary:", max_length

#####PART C######
fifthteen_list1 = [word for word in word_list if len(word)==15]
fifthteen_list2 = fifthteen_list1[:10]
print "(c)", fifthteen_list2

#####PART D######
five_a_list= [word for word in word_list if word.count('a')>=5]
print "(d)",five_a_list

#####PART E######
max_e = 0
for word in word_list:
    if word.count('e') > max_e:
        max_e = word.count('e')
max_e_list = [word for word in word_list if word.count('e') == max_e]
print "(e)", max_e_list

#####PART F######
palindrome = []
for word in word_list:
    if word == word[::-1]:
        palindrome.append(word)
palindrome_max = [word for word in palindrome if len(word) == len(max(palindrome, key = len))]
print "(f)", palindrome
print palindrome_max

#####PART G######
qu_list = [word for word in word_list if 'q' in word and 'qu' not in word]
print "(g)",qu_list

#####PART H######
length_list = [len(word) for word in word_list]
#print len(length_list)
length_list2 = [length_list.count(x) for x in range(2,max_length+1)]
print "(h)",length_list2

########################################################################
########################################################################

#####PART 2######
def find_anagrams(w,s):
    anagrams = [word for word in w if ''.join(sorted(s))==''.join(sorted(word))]
    return anagrams

########################################################################
########################################################################

#####PART 4: Finding all the words######
def all_subsequences(word):
    sub_list = ['']
    for ch in word:
        temp_list = list(sub_list)
        for i in temp_list:
            if i+ch not in sub_list: sub_list.append(i + ch)
    return sub_list

def find_all_words(s):
    all_anagrams = []
    sub_list = all_subsequences(s)[1:]
    #print sub_list
    anagram_list =[]
    for word in getwordlist():
        anagram_list.append(string_with_sortkey(word))
    anagram_list = sorted(anagram_list,key = lambda x: x[0])
    #print anagram_list
    for word in sub_list:
        all_anagrams.extend(new_find_anagrams(anagram_list,word,all_anagrams))
        #print all_anagrams
    return all_anagrams

def find_all_words2(s):
    all_anagrams = []
    sub_list = all_subsequences(s)[1:]
    for word in sub_list:
        all_anagrams.extend(find_anagrams(getwordlist(),word))
    return all_anagrams


        
########################################################################
########################################################################

#####PART 5: Faster Searching######
def string_with_sortkey(word):
    return [''.join(sorted(word)),word]

def new_find_anagrams(w,s,k):
    updated_list = []
    low = 0
    high = len(w)-1
    while low<=high:
        mid = ((low+high)/2)
##        if w[mid][1] in updated_list and w[mid+1][0] >''.join(sorted(s)):
##            mid = ((low+high)/2)-1
##        elif w[mid][1] in updated_list and w[mid+1][0] <''.join(sorted(s)):
##            mid = ((low+high)/2)+1
##        else:
##            mid = ((low+high)/2)
##            
        if w[mid][0] == ''.join(sorted(s)) and w[mid][1] not in k:
            #print w[mid][0]
            #updated_list.append(w[mid][1]);
            temp = mid
            temp2 = mid
            while(w[temp][0] <= ''.join(sorted(s))):
                updated_list.append(w[temp][1]);
                temp = temp+1
            while(w[temp2][0] >= ''.join(sorted(s))):
                updated_list.append(w[temp2][1]);
                if temp2==0:
                    break
                else:
                    temp2 = temp2-1
                
            #updated_list = [word[1] for word in w if word[0] == w[mid][0]]
            return updated_list
        elif w[mid][0] < ''.join(sorted(s)):
            low = mid+1
        else:
            high = mid-1
    return updated_list
            
    #updated_list = [y[1] for y in anagram_list if y[0]==''.join(sorted(s))]
    #return updated_list

def largest_anagrams():
    max1 = 0
    max_word = ""
    for word in word_list:
        length  = len(find_all_words(word))
        if length>max1:
            print max1, word
            max_word = word
            max1 = length
    return max1
               
    #anagrams = [find_all_words(word) for word in word_list]
    #max_length = len(max(anagrams, key = len))
    return max_length
########################################################################
########################################################################

#####PART 3: GUI######
def button_handler(event):
    window.update()
    w=event.widget
    if w==anagram_button:
        word=the_text.get()
        anagrams = find_anagrams(getwordlist(),word)
        anagram_text.delete(0.0,END)
        if(len(anagrams)==1):
            anagram_text.insert(0.0,"None found")
        else:
            anagram_text.insert(0.0,anagrams)
            
window = Tk()
textlabel=Label(window,text='Word')
textlabel.grid(row=0,column=0,columnspan=1)
the_text=Entry(window,width=40)
the_text.grid(row=0,column=1,columnspan=1)
anagram_text=Text(window,width=40)
anagram_text.grid(row=3,column=0,columnspan=2)
anagram_button=Button(window,text='Display Anagrams')
anagram_button.grid(row=2,column=0)
anagram_button.bind('<Button-1>',button_handler)
window.mainloop()
