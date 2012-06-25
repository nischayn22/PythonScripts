def coins(a):
	if(a<=0):
		return 0
	global array
	if(a in array):
		return array[a]
	array[a] = max(a,coins(a/2)+coins(a/3)+coins(a/4)) 
	return array[a]
nums = []
while(True):
	try:
		nums.append(int(raw_input()))
	except:
		break
array = {}
for i in nums:
	print coins(i)