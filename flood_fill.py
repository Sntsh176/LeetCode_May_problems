"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        Here will apply the depth first search algorithm
        for the starting r,c ( row , column ) will check in all 4 direction of the matrix
        will check the boudary condition if no then go with resusive function calls
        """
        
        # will take the value in color variable and use this in recursive check
        color = image[sr][sc]
        # length of rows and column , needed for applying the boundary condition
        row , col = len(image) , len(image[0])
        
        # if the new color is already done then simply return the same.
        if color == newColor:
            return image
            
        # recusrsive funtion 
        def dfs(r , c):
            # will check with the color and if matches then assign the newColor
            if image[r][c] == color:
                image[r][c] = newColor
            # else return the recursive function call to avoid further function calls
            else:
                return
            
            # now will call the function recursively in all 4 direction keeping in mind the boudary condition
            if r < row: dfs(r+1 , c)
            if r >= 0: dfs(r-1 , c)
            if c < col: dfs(r , c+1)
            if c >= 0: dfs(r, c-1)
            
        # finally call the function with starting row and column position
        dfs(sr,sc)
        
        return image