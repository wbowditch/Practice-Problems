def n_sum_from_1_3_4(n):  #given n, find the number of different ways to write n as the sum of 1, 3, 4
	d =[]
	d.insert(0,1)
	d.insert(1,1)
	d.insert(2,1)
	d.insert(3,2)

	for i in range(4,n+1):
		d.append(d[i-1]+d[i-3]+d[i-4])
	return d[n]

#print n_sum_from_1_3_4(6)


def lcs(x,y): #given two strings x and y, find the longest common subsequence (LCS) and print its length
	d = [[0 for j in range(0,len(x)+2)] for k in range(0,len(y)+2)]
	for i in range(1,len(x)):
		for j in range(1,len(y)):
			#print i,j
			if(x[i]==y[j]):
				d[i][j] = d[i-1][j-1] +1
			else:
				d[i][j] = max(d[i-1][j],d[i][j-1])
	return d[len(x)][len(y)]
print lcs("ABCBDAB","BDCABC")

k = 99
memo = [-1 for x in range(k+1)] #memoization
def getMinSteps(n): # On a positive integer, you can perform any one of the following 3 steps. 1.) Subtract 1 from it. ( n = n - 1 )  , 2.) If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2  )  , 3.) If its divisible by 3, divide by 3. ( if n % 3 == 0 , then n = n / 3  ). Now the question is, given a positive integer n, find the minimum number of steps that takes n to 1
	if(n==1): return 0 #base case
	if(memo[n]!= -1): return memo[n]  #we solved this already
	r = 1 + getMinSteps(n-1) #-1 step, r will contain the optimal answer finally
	if(n%3 == 0): r = min(r,1+getMinSteps(n/3))
	if(n%2 == 0): r = min(r,1+getMinSteps(n/2))
	memo[n] = r
	#print memo
	return r

#print getMinSteps(k)
	

def getMinSteps2(n):
	dp = [-1 for x in range(n+1)]
	dp[1] = 0
	for i in range(2,n+1):
		dp[i] = 1 + dp[i-1]
		if(i%2==0): dp[i] = min(dp[i],1+dp[i/2])
		if(i%3==0): dp[i] = min(dp[i],1+dp[i/3])

	return dp[n]


#print getMinSteps2(99)