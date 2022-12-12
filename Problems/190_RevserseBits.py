'''
190. Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

Note:
- Note that in some languages, such as Java, there is no unsigned integer type. In this case, 
  both input and output will be given as a signed integer type. They should not affect your 
  implementation, as the integer's internal binary representation is the same, whether 
  it is signed or unsigned.

- In Java, the compiler represents the signed integers using 2's complement notation. Therefore, 
  in Example 2 above, the input represents the signed integer -3 and the output represents 
  the signed integer -1073741825.


Example: 
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned 
integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example: 
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer
 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
'''


class Solution:

    def decimal_to_binary(self,num): 
        
        res = ''

        while num != 0: 
            res = res + str(num % 2)
            num = num//2
        
        res = res[::-1].zfill(32)

        return res


    def reverseBits(self, n):
        
        n_binary = self.decimal_to_binary(n)

        res = 0

        for i, d in enumerate(n_binary): 
            # print(i, d)
            res += int(d) * (2**i) 
        
        return res

    def reverseBits1(self, n):
        
        res = 0

        for i in range(32): 
            bit = (n >> i) & 1
            print(n>>i)
            print(bit)
            res = res | (bit << (31-i))
        
        return res
        

# n = 4294967293
n = 4

print(Solution().reverseBits1(n))
