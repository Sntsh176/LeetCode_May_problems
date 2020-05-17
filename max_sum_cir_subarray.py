"""
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

 

Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
Example 5:

Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1
 

Note:

-30000 <= A[i] <= 30000
1 <= A.length <= 30000
   Hide Hint #1  
For those of you who are familiar with the Kadane's algorithm, think in terms of that. For the newbies, Kadane's algorithm is used to finding the maximum sum subarray from a given array. This problem is a twist on that idea and it is advisable to read up on that algorithm first before starting this problem. Unless you already have a great algorithm brewing up in your mind in which case, go right ahead!

"""






"""
Kadane Algorithm
circular array = [5,-3,5] this means the index sequence will be (012 012 012 012 012 .......) fashion
so for above max_sum is = index 2 and 0 , as this is circular array
for example
[1,-2,3,-2] circular index will have sequence ( 0123 0123 0123 0123 ....)
so here max_sum will be 3 as making other conbination gives less then 3
Next Example
[3,-2,2,-3] here max will be = 3
array = [-2,-3,-1] then in this case max_sum will be = -1 ( as including other will make it smaller )

According to Kadane algorithm 
if total sum != max_subarray_sum  OR  total sum != min then 
for circular array the max sum will be (tot_sum - min)

if tot_sum == min then max_subarray_sum will be min ( as this means all the items are -ve in the array)
if tot_sum == max then max_subarray_sum will be max ( as this means all the items are +ve in the array)

some sample
=================
[1,-2,3,-2]
here max_subarray_sum = 3 , min = -2 , sum = 0
so max_subarray_sum for circular array will be
condition[total sum != max_subarray_sum  OR  total sum != min] 
then sum - min = 0 - (-2) => 2 output
==================
similarly find for this one [3,-1,2,-1] answer is  = 4

"""


class Solution:
    def maxSubarraySumCircular(self, a: List[int]) -> int:
    
        max_till_here = a[0]
        max_in_total = a[0]
        min_till_here = a[0]
        min_in_total = a[0]
        sum = a[0]

        for i in range(1,len(a)):
            if max_till_here + a[i] > a[i]:
                max_till_here += a[i]
            else:
                max_till_here = a[i]

            max_in_total = max(max_in_total , max_till_here)

            if min_till_here + a[i] < a[i]:
                min_till_here += a[i]
            else:
                min_till_here = a[i]

            min_in_total = min(min_in_total , min_till_here)

            sum += a[i]

        if sum == min_in_total:
            return max_in_total
        else:
            return max(max_in_total , (sum - min_in_total))
            
            
# ==============================================================
# ==============================================================
# ==============================================================
# ==============================================================

# [3,-2,2,-3]

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        curr_max = 0
        final_max = 0
        for i in A:
            curr_max += i
            if curr_max <= 0:
                curr_max = 0
            if final_max < curr_max:
                final_max = curr_max
        if final_max == 0:
            return max(A)
        
        curr_min = 0
        final_min = 0
        for i in A:
            curr_min += i
            if curr_min >= 0:
                curr_min = 0
            if final_min > curr_min:
                final_min = curr_min
        return max(final_max, sum(A) - final_min)
