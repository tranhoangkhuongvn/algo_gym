class TrieNode:
	def __init__(self):
		self.count_word = 0 #if this node is the end of a word --> count_word != 0
		self.child = dict()


def add_word(root, s):
	tmp = root
	for ch in s:
		if ch not in tmp.child:
			tmp.child[ch] = TrieNode()

		tmp = tmp.child[ch]

	tmp.count_word += 1
	

def find_word(root, s):
	tmp = root
	for ch in s:
		if ch not in tmp.child:
			return False
		tmp = tmp.child[ch]

	return tmp.count_word > 0


def is_word(node):
	return node.count_word != 0


def is_empty(node):
	return len(node.child) == 0


def remove_word(root, s, level, length):
	if root == None:
		return False 

	if level == length:
		if root.count_word > 0:
			root.count_word -= 1
			return True
		return False

	ch = s[level]
	flag = remove_word(root.child[ch], s, level + 1, length)

	if flag == True and is_word(root.child[ch]) == False and  \
		is_empty(root.child[ch]) == True:
		del root.child[ch]

		root.child[ch] = None

	return flag


def traverse_trie(root):
	if root == None:
		return None
	
	for k, v in root.child:
		print(k, v)


if __name__ == '__main__':
	root = TrieNode()
	add_word(root, 'the')
	add_word(root, 'then')
	add_word(root, 'bigo')
	print(root.child)

	traverse_trie(root)	
	exit(0)
	print(find_word(root, 'there'))
	print(find_word(root, 'th'))
	print(find_word(root, 'the'))

	remove_word(root, 'bigo', 0, 4)
	remove_word(root, 'the', 0, 3)
	remove_word(root, 'then', 0, 4)
