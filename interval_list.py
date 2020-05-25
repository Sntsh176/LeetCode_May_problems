"""
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 

Example 1:



Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
 

Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""


# A = [[0,2],[5,10],[13,23],[24,25]]
# B = [[1,5],[8,12],[15,24],[25,26]]


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        a_i = 0
        b_i = 0

        while a_i < len(A) and b_i < len(B):
            start_a, end_a = A[a_i]
            start_b, end_b = B[b_i]

            if end_a < start_b:
                a_i += 1
            elif end_b < start_a:
                b_i += 1
            else:
                if end_a <= end_b:
                    a_i += 1
                else:
                    b_i += 1
                res.append([max(start_a, start_b), min(end_a, end_b)])
        return res
		
# ==================================================================		
# ==================================================================
# ==================================================================
		

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        m = len(A)
        n = len(B)
        i = 0
        j = 0
        res = []
        
        while i<m and j<n:
            low_lim = max(A[i][0] , B[j][0])
            high_lim = min(A[i][1] , B[j][1])
            
            if low_lim <= high_lim:
                res.append([low_lim,high_lim])
            
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
                
        return res