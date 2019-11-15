


def flatten_dictionary(d):
	result = {}
	for k, v in d.items():
		if isinstance(v, dict):
			temp = flatten_helper(k, v)
			for k, v in temp.items():
				result[k] = v
		else:
			result[k] = v


	return result


def flatten_helper(parent, d):
	"""
	ins: parent key, value as a dictionary
	outs: a dictionary of parent_key.child_key: inner_value
	"""
	result = dict()
	temp = dict()
	for k, v in d.items():
		if isinstance(v, dict):
			parent = parent + '.' + k
			temp = flatten_helper(parent, v)

		else:
			temp_k = parent + '.'  + k
			result[temp_k] = v

	for k, v in temp.items():
		result[k] = v

	return result



d = {
	'a': 1,
	'b': {
		'c': 2,
		'd': {
			'e': 3
		}
	}
}


print(flatten_dictionary(d))
# {'a': 1, 'b.c': 2, 'b.d.e': 3}
