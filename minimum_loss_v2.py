class Node:
	def __init__(self, key=0, left=None, right=None):
		self.key = key
		self.left = left
		self.right = right 

	
	def find(self, x):
		if self.key == x:
			return self
		if self.right and self.key < x:
			return self.right.find(x)
		if self.left and self.key > x:
			return self.left.find(x)
		return None 


	def insert(self, x):
		if x < self.key:
			if self.left:
				self.left.insert(x)
			else:
				self.left = Node(x)
		elif x > self.key:
			if self.right:
				self.right.insert(x)
			else:
				self.right = Node(x)

	
	def find_min(self):
		#the left most node in the tree
		current = self
		while current.left:
			current = current.left

		return current

	
	def remove(self, x):
		
		
