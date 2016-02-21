def string_unique_characters(str):  #returns true if the string has only unique characters, and not using any other data structure
	for index1 in range(len(str)):
		for index2 in range(index1+1,len(str)):
			if str[index1] == str[index2]:
				return False
	return True


#print string_unique_characters("worlfsdafsd")

def check_permutation(str1,str2):  #Given two strings, write a method to decide if one is a permutation of the other.
	str1 = ''.join(sorted(str1)) 
	str2 = ''.join(sorted(str2))


	return str1 == str2

#print check_permutation("dick","kicd")

def replace_spaces(str1): #Replace all spaces with %20
	str2 = list(str1)
	for ch in range(len(str2)):
		if str2[ch] == " ":
			str2[ch] = '%20'
	return "".join(str2)


#print replace_spaces("hello world")

def string_compressor(str1):
	d_count = {}
	output = ""
	temp = str1[0]
	for ch in str1:
		if ch !=temp:
			output+= temp + str(d_count[temp])
			del d_count[temp]
		if ch in d_count:
			d_count[ch]+=1
		else:
			d_count[ch] = 1
		temp = ch
	output += temp + str(d_count[temp])
	if len(output)>len(str1):
		return str1 
	else:
		return output

#print string_compressor("aabcccccaaa")

def row_col_zero(matrix):
	zeros = []
	row = [False for x in range(len(matrix))]
	col = [False for y in range(len(matrix[0]))]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 0:
				row[i] = True
				col[j] = True

	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if row[i] or col[j]:
				matrix[i][j] = 0
	return matrix

