
def one_edit(s1, s2):
	"""
	return True if s1 differs from s2 by 1 edit, False otherwise 
	True: xyz vs xz, xyz vs xyk, xy vs xyz 
	False: xyz vs xyz, xyz vs xzy, x vs xyz 
	Example:
      pale, ple     -> true
      pales, pale   -> true
      pale, bale    -> true
      pale, bake    -> false

	Check character occurence and sequence of characters
	Compare len(s1) and len(s2) for first difference 
	if len(s1) == len(s2) --> check for order, 1 difference is acceptable 
	if len(s1) = len(s2) + 1 --> check for order --> any order difference return False 
	"""
	n1 = len(s1)
	n2 = len(s2)
	diff = 0 
	if abs(n1 - n2) > 1:
		return False 

	elif n1 == n2:
		for i in range(n1):
			if s1[i] != s2[i]:
				diff += 1
				if diff > 1:
					break 

	elif abs(n1 - n2) == 1:
		diff = 1
		n = min(n1, n2)	
		i = 0
		j = 0
		while i < n and j <	n:
			if s1[i] == s2[j]:
				i += 1
				j += 1
			else:
				if s1[i] == s2[j+1]:
					i += 1
					j += 2
				elif s1[i+1] == s2[j]:
					j += 1
					i += 2
				else:
					diff += 1
					break
		
	if diff == 1:
		return True
	else:
		return False 

s1 = 'bake'
s2 = 'pale'
print(s1, s2)
print(one_edit(s1, s2))

s1 = 'pale'
s2 = 'ple'
print(s1, s2)
print(one_edit(s1, s2))

s1 = 'pales'
s2 = 'pale'
print(s1, s2)
print(one_edit(s1, s2))

s1 = 'a'
s2 = 'ba'
print(s1, s2)
print(one_edit(s1, s2))

s1 = 'xyz'
s2 = 'xzy'
print(s1, s2)
print(one_edit(s1, s2))

s1 = 'xy'
s2 = 'xyz'
print(s1, s2)
print(one_edit(s1, s2))
