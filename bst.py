class Node:
	def __init__(self):
		self.key = 0
		self.left = None
		self.right = None


def create_node(x):
	newNode = Node()
	newNode.key = x 
	return newNode 


def insert_node(root, x):
	if root == None:
		return create_node(x)
	
	if x > root.key:
		insert_node(root.right, x)
	elif x < root.key:
		insert_node(root.left, x)
	
	return root


def create_tree(a, n):
	root = None
	for i in range(n):
		root = insert_node(root, a[i])
	return root


def search_node(root, x):
	if root == None or root.key == x:
		return root 

	if root.key < x:
		return search_node(root.right, x)
		
	return search_node(root.left, x)	
	

def delete_node(root, x):
	if root == None: #Cannot find x to delete 
		return root 

	if x < root.key: #find and delete x in the left branch
		root.left = delete_node(root.left, x)
	elif x > root.key: #find and delete x in the right branch 
		root.right = delete_node(root.right, x)
	else: #root.key == x --> find x to delete
		if root.left == None:
			temp = root.right
			del root 
			return temp
		elif root.right == None:
			temp = root.left
			del root
			return temp
		temp = minValueNode(root.right)
		root.key = temp.key
		root.right = delete_node(root.right, temp.key)
	
	return root


def minValueNode(root):
	current = root 
	while current.left != None:
		current = current.left
	
	return current



def traverse_tree(root):
	if root == None:
		return
	
	print(root.key)	
	traverse_tree(root.left)
	traverse_tree(root.right)


def tree_traversal(root):
	if root != None:
		tree_traversal(root.left)
		print(root.key, end=' ')
		tree_traversal(root.right)


def size(root):
	if root == None:
		return 0
	return size(root.left) + 1 + size(root.right)


def delete_tree(root):
	if root == None:
		return
	
	delete_tree(root.left)
	delete_tree(root.right)
	del root


arr = [1,2,3,4,5,6,7,8,9,10]
tree = create_tree(arr, 10)
traverse_tree(tree)
tree_traversal(tree)
