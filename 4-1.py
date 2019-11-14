#count the number of set bit 
def count_bits(x):
	num = 0
	while x:
		#bit = x & 1
		#if bit:
		#	num += 1 
		num += x & 1	
		x >>= 1
	
	return num

x = 150
print(bin(x))
print(count_bits(x))
