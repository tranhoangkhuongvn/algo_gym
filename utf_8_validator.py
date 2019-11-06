class Solution:
    def validUtf8_1(self, data):
        n = len(data)

        if n < 1:
            #violates problem constraint: size from 1 to 4
            return False
        expect_next_bytes = -1

        for byte in data:

            bit0 = byte >> 7 & 1
            bit1 = byte >> 6 & 1
            bit2 = byte >> 5 & 1
            bit3 = byte >> 4 & 1
            bit4 = byte >> 3 & 1

            if expect_next_bytes > 0:
                if bit0 and not bit1:
                    expect_next_bytes -= 1

            else:
                if bit0 == 0:
                    expect_next_bytes = 0

                elif bit1 and not bit2:
                    expect_next_bytes = 1

                elif bit1 and bit2 and not bit3:
                    expect_next_bytes = 2

                elif bit1 and bit2 and bit3 and not bit4:
                    expect_next_bytes = 3

                else:
                    expect_next_bytes = -1
                    break

            print(byte, bin(byte), expect_next_bytes)

        return expect_next_bytes == 0

    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """

        # Number of bytes in the current UTF-8 character
        n_bytes = 0

        # Mask to check if the most significant bit (8th bit from the left) is set or not
        mask1 = 1 << 7

        # Mask to check if the second most significant bit is set or not
        mask2 = 1 << 6
        for num in data:

            # Get the number of set most significant bits in the byte if
            # this is the starting byte of an UTF-8 character.
            mask = 1 << 7
            if n_bytes == 0:
                while mask & num:
                    n_bytes += 1
                    mask = mask >> 1

                # 1 byte characters
                if n_bytes == 0:
                    continue

                # Invalid scenarios according to the rules of the problem.
                if n_bytes == 1 or n_bytes > 4:

                    return False
            else:

                # If this byte is a part of an existing UTF-8 character, then we
                # simply have to look at the two most significant bits and we make
                # use of the masks we defined before.
                if not (num & mask1 and not (num & mask2)):
                    return False
            n_bytes -= 1
            print(num, bin(num), n_bytes)
        return n_bytes == 0     

solution = Solution()
arr = [32,196,147,225,184,165,246,149,170,129,204,153,243,188,141,147,0,217,149,234,176,176,243,178,133,144,213,181,193,187,238,137,134,218,155,33,231,134,162,243,184,144,131,71,201,131,244,133,189,140,242,178,128,156,207,154,230,165,181,240,181,134,180,227,129,199,172,226,158,164,214,183,224,137,141,20,194,188,232,177,151,242,157,180,153]
solution.validUtf8(arr)
