"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
"""



class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        # will check slope between two points
        # if they are in straight line then the slope will be same for each pair of two points
        
        # slope m = ( y1 - y0 ) / ( x1 - x0 )
        # for 2nd pair m = (y2-y1) / (x2-x1)
        
        # then for m = m | ( y1 - y0 ) * (x2-x1) == ( x1 - x0 ) * (y2-y1) 
        
        x0,y0 = coordinates[0]
        x1,y1 = coordinates[1]
        
        if len(coordinates) == 2:
            return True
        
        # now will loop through it
        for i in range(2, len(coordinates)):
            
            x,y = coordinates[i]
            # will place x,y at the place of x2,y2
            if (y1-y0) * (x - x1) != ( x1 - x0 ) * (y - y1) :
                return False
        return True 



# ==============================================================
# ==============================================================
# ==============================================================


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n < 2:
            return False
        if n == 2:
            return True
        xs = [coordinates[i][0] for i in range(n)]
        
        if max(xs) == min(xs):
            return True
        
        i = 1
        while coordinates[i][0] == coordinates[1][0]:
            i += 1
                          
        k = (coordinates[i][1]-coordinates[0][1]) /(coordinates[i][0]-coordinates[0][0])
        b = coordinates[0][1] - k * coordinates[0][0]
        
        for i in range(2,n):
            if abs(coordinates[i][1] - k * coordinates[i][0] - b) > 0.0001:
                return False
        
        return True