#Write a function takes a 64-bit integer and swap bits at indices i and j
#LSB is at rightmost bit


def swap_bits(n, i, j):
	bit0 = (1 & (n >> i))
	bit1 = (1 & (n >> j))
	if bit0 != bit1:
		if bit0:
			#reset bit0 to 0, set bit1 to 1
			n = n & (~(1 << i))
			n = n | (1 << j)
		else:
			n = n | (1 << i)
			n = n & (~(1 << j))
	print(bin(n))
	return n

print(swap_bits(73, 1, 6))





