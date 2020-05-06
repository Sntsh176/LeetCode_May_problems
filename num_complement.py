# This is a simple approach where we use the logic that the XOR operation between a number and its complement results in 111..111
# Taking an example 5
# We find the smallest (2^n)-1 number greater than 5 (101) which in this case is 7 (111)
# Performing XOR with these two numbers will result in the bitwise complement of the original number.
# 101 ^ 111 -> 010

def findComplement(self,num):
    t=1
    while num>t:
        t=2*t+1
    return t^num
    

# ====================================================================================
# ====================================================================================
# ====================================================================================

"""
This is a simple approach where we use the logic that the XOR operation between a number and its complement results in 111..111
Taking an example 5
We find the smallest (2^n)-1 number greater than 5 (101) which in this case is 7 (111)
Performing XOR with these two numbers will result in the bitwise complement of the original number.
101 ^ 111 -> 010
"""
class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0: return 1
        t = num
        res = 0
        while t > 0:
            t = t >> 1
            
            # here for res variable we are shifting one left and adding 1 to it means making each binary bit as '1'
            res = res << 1
            res += 1
        return res ^ num
        

        
# ====================================================================================
# ====================================================================================
# ====================================================================================

# Simple for loop approach , very easy one

def bitwiseComplement(self, N: int) -> int:
    return int(''.join('1' if x == '0' else '0' for x in bin(N)[2:]),2)