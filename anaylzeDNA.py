#Will Bowditch

def analyzeDNAv1(dna):  #iteration using counters
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0
    for x in dna:
        if x == "A":
            a_count+=1
        if x == "C":
            c_count+=1
        if x == "G":
            g_count+=1
        if x == "T":
            t_count+=1
    print "A:",a_count,", C:",c_count,", G:",g_count,", T:",t_count


def analyzeDNAv2(dna):  #iteration using dictionary
    dna_dict = {"A":0,"C":0,"G":0,"T":0}

    for x in dna:
        for ch in "ACGT":
            if x==ch:
                dna_dict[ch]+=1
    for item,value in dna_dict.items():
        print item+":",value,


def analyzeDNAv3(dna):  #iteration using built-in string functions
    for x in "ACGT" :
        print x+":",dna.count(x),

def isPrime(n):
    if n<2:
        return False
    for x in range(2,int(n**.5)+1):
        if n%x==0: return False
    return True

def sumPrime(l):
    total = 0
    for x in l:
        if isPrime(x): total+=x
    return total

l = [2,3,6,7,5,235,3]

def longest_str(l):
    return max(l,key=len)




