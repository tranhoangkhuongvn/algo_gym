def start_with(word, key_list):
	for key in key_list:
		if key.startswith(word):
			return True 

	return False


def shortest_unique_prefix_v0(words):
	my_dict = dict()
	for word in words:
		for i in range(1, len(word)):
			if word[:i] not in my_dict.keys() and not start_with(word[:i], my_dict.keys()):
				my_dict[word[:i]] = word
				break
			else:
				current_word = my_dict[word[:i]]
				new_key = current_word[:len(word[:i])+1]
				del my_dict[word[:i]]
				my_dict[new_key] = current_word

		print(word, my_dict)


def shortest_unique_prefix(words):
	my_dict = dict()
	for word in words:
		my_dict[word] = word  #create key == value --> uniqueness
	
	for key in my_dict.keys():
		n = len(key)
		new_key = key
		while new_key




word_ar = ['joma', 'john', 'jack', 'techlead']
shortest_unique_prefix(word_arr)
