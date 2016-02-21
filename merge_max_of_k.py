def merge_two_list(arr1,arr2,k):
	result = []
	index1 = 0
	index2 = 0

	while len(result<k):
		if arr1[index1]<= arr2[index2]:
			result.append(arr1[index1])
			index1+=1
		else:
			result.append(arr=2[index2])
			index2+=1
	return result

	