"""
Course Schedule
Solution
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
   Hide Hint #1  
This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
   Hide Hint #2  
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
   Hide Hint #3  
Topological sort could also be done via BFS.

"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0: unlearned, 1: learning, 2: learned
        courses = [0] * numCourses
        table_course = collections.defaultdict(list)
        
        # now will loop through the prerequisites and will add mapping / graph
        for p1,p2 in prerequisites:
            table_course[p1].append(p2)
        
        # now we will define the DFS function for the recursive calls
        def dfs(course):
            # if 2 this mean we already visited it successfully 
            if courses[course] == 2:
                return True
            # 1 this means it will form a cycle so return False
            if courses[course] == 1:
                return False
            
            courses[course] = 1
            for cor in table_course[course]:
                if not dfs(cor):
                    return False
                
            courses[course] = 2
            return True
            
        # Now we call the function recursively for each item of the coureses    
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True