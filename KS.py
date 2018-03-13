N = 4 					# number of items
V = [100, 70, 50, 10]	# value of each item
W = [10, 4, 6, 12]		# weight of each item
S = 12					# max cap 

# Creates a list containing N lists, each of S+1 items, all set to -1
memo = [[-1 for x in range(S+1)] for y in range(N)] 

# recursion conditions:
# 1- val(it, 0) = 0 -> is full
# 2- val(n, remW) = 0 -> all item considered
# 3- if W[it] > remW -> val(it, remW) = val(it+1, remW) this item is too heavy
# 4- if w[it] <= remW -> val(it, remW) = max( val(it+1, remW), V[it] + val(it+1, remW - W[it]) )


def value(id, w):
	if(id == N or w == 0):			# recursion conditions 1 and 2
		return  0
	
	if(memo[id][w] != -1):			# checking if alredy pass by this state 	
		return memo[id][w]

	if(W[id] > w):  				# recursion condition 3
		memo[id][w] = value(id+1, w)
		return memo[id][w]

	memo[id][w] = max(V[id] + value(id+1, w - W[id]), value(id+1, w))  #recusion condition 4
	return memo[id][w] 






print(value(0, S))