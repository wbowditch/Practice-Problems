#Will Bowditch
#Recursion and Dynamic Programming Problems

def child_staircase(n,map):
	if(n<0): return 0
	elif n==0: return 1
	elif (map[n]>-1):
		return map[n]
	else:
		map[n] = child_staircase(n-1,map) + child_staircase(n-2,map) + child_staircase(n-3,map)

	return map[n]


n = 10
map = [-1 for x in range(0,n+1)]

print child_staircase(n,map)

def getSubsets(set,index):
	#print "to do"
	if (len(set) == index):  #Base case - add empty set (when index eventually equals 3)
		print index
		all_subsets = []
		all_subsets.append([]) # empty set
		#print all_subsets
	else:
		all_subsets = getSubsets(set,index+1)  #first round, index = 2, all_subsets = [ [] ]
		#print all_subsets
		item = set[index]			#get item c from llist
		more_subsets = []
		#print set

		for subset in all_subsets:   
			new_subset = []
			new_subset+= subset  # newbuset = [[]]
			print new_subset,subset
			new_subset.append(item)  #new subset = [[],c]
			more_subsets.append(new_subset)
			#print new_subset
		all_subsets+=more_subsets
	return all_subsets

set = ['a','b','c']

print getSubsets(set,0)


def all_permutations(str):
	#if (str == null): return null

	permutations = []

	if (len(str) == 0): #base case
		permutations.append("")
		return permutations

	first = str[0] #get the first character
	remainder = str[1:]
	words = all_permutations(remainder)
	for word in words:
		for j in range(len(word)+1):
			s = word[:j] + first + word[j:]
			permutations.append(s)
	#print permutations, str
	return permutations

#print all_permutations("testing")




