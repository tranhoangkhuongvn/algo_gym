

def has_character_map_stupid(str1, str2):
	n = min(len(str1), len(str2))
	mapping_dict = dict()	
	
	for i in range(n):
		if str1[i] not in mapping_dict and str2[i] not in mapping_dict:
			mapping_dict[str1[i]] = str2[i]
			mapping_dict[str2[i]] = str1[i]
		elif str1[i] in mapping_dict and str2[i] not in mapping_dict:
			if str2[i] != mapping_dict[str1[i]]:
				return False
		elif str2[i] in mapping_dict:
			if str1[i] != mapping_dict[str2[i]]:
				return False

	print(mapping_dict)
	
	return True




def has_character_map(str1, str2):
	if len(str1) != len(str2):
		return False
	
	occurence1 = [False] * 128 
	occurence2 = [False] * 128 
	mapping = [-1] * 128 
	for i in range(len(str1)):
		first = ord(str1[i]) - 0 
		second = ord(str2[i]) - 0 
		print(str1[i], str2[i])
		if not occurence1[first] and not occurence2[second]:
			occurence1[first] = True
			occurence2[second] = True
			mapping[first] = second

		elif occurence1[first] and occurence2[second]:
			if mapping[first] != second:
				return False

		else:
			return False
					

	return True


print("abc vs def")
print(has_character_map('abc', 'def'))
#True


print("aac vs def")
print(has_character_map('aac', 'def'))
#False


print("ab vs ca")
print(has_character_map('ab', 'ca'))
#True

print("ab vs aa")
print(has_character_map('ab', 'aa'))
#False


print("paper vs title")
print(has_character_map('paper', 'title'))

print("aba vs baa")
print(has_character_map('aba', 'baa'))
