


if __name__ == '__main__':
	t = int(input())
	my_dict = dict()
	for _ in range(t):
		name = input()
		if name not in my_dict:
			my_dict[name] = 1
		else:
			my_dict[name] += 1
	
	items = []
	for k, v in my_dict.items():
		items.append((v, k))
	print(sorted(items, reverse=True)[0][1])
