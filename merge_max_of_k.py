#Given two sorted lists and an integer k, merge the lists up to a maximum of k elements.
def merge_k ( arr1 , arr2 , k):

    count = 0
	result = []
	index1 = 0
	index2 = 0
	if len(arr1) == 0:
		if len(arr2) ==0:
			return result
		else:
			return arr2
	if len(arr2) ==0:
		return arr1

	while len(result)<=k:
		if arr1[index1]<= arr2[index2]:
			result.append(arr1[index1])
			index1+=1
		else:
			result.append(arr2[index2])
			index2+=1
		if index1 >= len(arr1):
			if index2 < len(arr2):
				while(len(result)<=k):
					result.append  #add in conditions
			break


	return result


arr1 = [3,4,5,8,23,45,67,89]
arr2 = [0,2,5,9,13,23,49]


print merge_k(arr1,arr2,15)
