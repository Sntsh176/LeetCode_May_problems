"""
Count Square Submatrices with All Ones
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
"""


class Solution:
    def countSquares(self, matrix) -> int:
        count = 0
        m = len(matrix)
        n = len(matrix[0])
        # here will use dynamic programming so taking 1 extra length
        temp_mat = [[0]*(n+1) for _ in range(m+1)]

        for row in range(1,m+1):
            for col in range(1,n+1):
                if matrix[row - 1][col - 1] == 1:
                    temp_mat[row][col] = 1 + min(temp_mat[row][col-1], temp_mat[row-1][col], temp_mat[row-1][col-1])
                    count += temp_mat[row][col]
        
        return count


if __name__ == "__main__":
    sample_obj = Solution()
    val = sample_obj.countSquares([
    [0,1,1,1],
    [1,1,1,1],
    [0,1,1,1]
    ])

print(val)

# ===========================================================
# ===========================================================
# ===========================================================


class Solution:
    def countSquares(self, matrix):
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] and matrix[i][j - 1] and matrix[i - 1][j - 1]:
                    k = min(matrix[i - 1][j], matrix[i][j - 1])
                    matrix[i][j] = k + 1 if matrix[i - k][j - k] else k
        return sum(sum(row) for row in matrix)
		
		

# ===========================================================
# ===========================================================
# ===========================================================


class Solution:
    def countSquares(self, matrix) -> int:
        m = len( matrix )
        if m == 0 : return 0
        n = len( matrix[0] ) 
        result = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0: continue
                if i == 0 or j == 0:
                    result += 1
                    continue
                min_val = min(matrix[i-1][j], matrix[i][j-1] , matrix[i-1][j-1])
                
                matrix[i][j] += min_val
                result += matrix[i][j]
                
        return result
