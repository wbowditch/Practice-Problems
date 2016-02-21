#Maximum Value Contiguous Subsequence
#Given a sequence of n real numbers A(1) ... A(n), determine a #contiguous subsequence A(i) ... A(j) for which the sum of #elements in the subsequence is maximized.

def max_cont_sub(L):
	max_so_far = L[0]
	curr_max = L[0]

	for i in range(1,len(L)):
		curr_max = max(a[i],curr_max + a[i])
		max_so_far = max(max_so_far,curr_max)

	return max_so_far

a = [-2, -3, 4, -1, -2, 1, 5, -3]

print max_cont_sub(a)