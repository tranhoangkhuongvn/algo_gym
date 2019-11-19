class Node:
	def __init__(self, data, next_node=None):	
		self.data = data
		self.next = next_node


	def set_data(self, data):
		self.data = data 

	
	def get_data(self):
		return self.data

	
	def set_next_node(self, next_node):
		self.next = next_node


	def get_next_node(self):
		return self.next 

	
class LinkedList:
	def __init__(self):
		self.head = None 

	
	def print_linked_list(self):
		temp = self.head
		while temp != None:
			print(temp.data)
			temp = temp.next


	def insert_at_start(self, data):
		new_node = Node(data, None)
		new_node.set_next_node(self.head)
		self.head = new_node
		

	def insert_at_end(self, data):
		new_node = Node(data, None)
		if not self.head:
			self.head = new_node
		else:
			temp = self.head
			while temp.next:
				temp = temp.next

			temp.set_next_node(new_node)

	
	def insert_after(self, prev_node, data):
		temp = self.head
		new_node = Node(data)
		if not self.head:
			self.head = new_node
		else:
			while temp != prev_node:
				temp = temp.next
				if not temp:
					print('Node not found')
					break

			new_node.set_next_node(temp.next)
			prev_node.set_next_node(new_node)


	#delete an item based on the data of the node
	def delete(self, data):
		temp = self.head
		prev_node = self.head
		if not self.head:
			print('Empty list')
			return None
		else:
			if self.head.data == data:
				self.head = temp.next
				return

			while temp and temp.data != data:
				prev_node = temp
				temp = temp.next

			if not temp:
				print('{} not found'.format(data))
				return None
			
			prev_node.set_next_node(temp.next)


	def search(self, node, data):
		if node == None:
			return 0
		if node.data == data:
			return 1
		return self.search(node.next, data)


if __name__ == '__main__':
	my_list = LinkedList()
	my_list.head = Node(1)
	print('Linked list created')
	my_list.print_linked_list()
	node2 = Node(2)
	my_list.head.set_next_node(node2)
	node3 = Node(3)
	node2.set_next_node(node3)

	my_list.print_linked_list()
	my_list.insert_at_start(4)
	print('Insert 4 at head')
	my_list.print_linked_list()
	my_list.insert_at_end(5)
	print('Insert 5 at end')
	my_list.print_linked_list()
	print('Insert 6 after 3')
	my_list.insert_after(node3, 6)
	my_list.print_linked_list()
	print('Delete 4 from linked list')
	my_list.delete(4)
	my_list.print_linked_list()
	print('Delete 5 from linked list')
	my_list.delete(5)
	my_list.print_linked_list()
	print('Search 6 in list: ', my_list.search(my_list.head, 6))
	print('Search 10 in list: ', my_list.search(my_list.head, 10))
