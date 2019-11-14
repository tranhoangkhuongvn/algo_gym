#https://www.hackerrank.com/contests/womens-codesprint-2/challenges/minimum-loss

from bst import *

def minimum_loss(arr, n):
	minimum_loss = 10000000 
	loss = 0 
	for i in range(n):
		#print(arr[i:])
		tree = create_tree_with_root(create_node(arr[i]), arr[i+1:], n-i-1)

		#tree_traversal(tree)
	
		if tree.left:
			result = find_rightmost_on_left(tree.left)
		else:
			loss = 0	
			continue 
		
		loss = arr[i] - result.key
		if loss > 0 and loss < minimum_loss:
			minimum_loss = loss 


		#print(result.key, minimum_loss)	
	
	return minimum_loss 


def find_rightmost_on_left(tree):
	current = tree
	while current.right:
		current = current.right

	return current


def minimum_loss_brute_force(price, n):
	minimum_loss = 100000
	for i in range(n-1):
		buy = price[i]
		min_sell = min(price[i+1: ])
		loss = buy - min_sell
		if loss > 0 and loss < minimum_loss:
			minimum_loss = loss
	
	return minimum_loss



if __name__ == '__main__':
	n = int(input())
	arr = list(map(int, input().split()))
	print(minimum_loss(arr, n))



