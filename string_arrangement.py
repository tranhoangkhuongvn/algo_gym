import heapq

class Char:
	def __init__(self, count, char):
		self.count = count
		self.char = char

	
	def __lt__(self, other):
		return self.count < other.count


	def __repr__(self):
		return "{} - {}".format(abs(self.count), self.char)


def arrange_string(s):
	result = ''	
	if len(s) == 0:
		return result
	
	my_dict = dict()
	character_count = []
	for ch in s:
		if ch not in my_dict:
			my_dict[ch] = 1
		else:
			my_dict[ch] += 1

	for k, v in my_dict.items():
		item = Char(-v, k)
		character_count.append(item)

	heapq.heapify(character_count)
	first_ch = heapq.heappop(character_count)
	result += first_ch.char
	first_ch.count += 1
	if first_ch.count < 0:
		heapq.heappush(character_count, first_ch)

	while len(character_count) > 0:
		print(character_count)
		n = len(result) - 1
		temp_ch = heapq.heappop(character_count)
		if temp_ch.char == result[n]:
			if len(character_count)	== 0:
				return ''
			second_ch = heapq.heappop(character_count)
			result += second_ch.char
			second_ch.count += 1
			if second_ch.count < 0:
				heapq.heappush(character_count, second_ch)
			
			heapq.heappush(character_count, temp_ch)
		
		else:
			result += temp_ch.char
			temp_ch.count += 1
			if temp_ch.count < 0:	
				heapq.heappush(character_count, temp_ch)
	
		heapq.heapify(character_count)

	return result


if __name__ == '__main__':
	#s = 'aaab'
	#s = 'vvvlo'
	s = input()
	print(arrange_string(s))

