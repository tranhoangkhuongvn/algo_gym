

#[1, 2, 3, [4, 5, 6, [7,8], [9]], 10, 11, [12]]

def weighted_sum(arr):
	#return weighted_sum_helper_recursive(1, arr)
	return weighted_sum_helper_iterative(arr)


def weighted_sum_helper_recursive(depth, arr):
	current_sum = 0
	if len(arr) == 0:
		return 0

	for element in arr:
		if not isinstance(element, list):
			current_sum += element * depth
		else:
			current_sum += weighted_sum_helper(depth+1, element)

	return current_sum


import queue 
def weighted_sum_helper_iterative(arr):
	depth = 1
	q = queue.Queue()
	current_sum = 0
	for element in arr:
		q.put((element, 1))
	
	while not q.empty():
		node, depth = q.get()
		if not isinstance(node, list):
			current_sum += node * depth
		else:
			depth += 1
			for sub_element in node:
				q.put((sub_element, depth))

	return current_sum



#arr = [[1,1], 2, [1,1]] 
arr = [1, 2, 3, [4, 5, 6, [7,8], [9]], 10, 11, [12]]
#arr = [1, [4, [6]]]
print(weighted_sum(arr))
