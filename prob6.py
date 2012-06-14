import math
def squaressum(n):
	return n*(n+1)*(2*n+1)/6
def sumsquares(n):
	return math.pow(n*(n+1)/2,2)
print sumsquares(100)-squaressum(100)