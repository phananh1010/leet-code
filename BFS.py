import numpy as np
import time

#1730. Shortest Path to Get Food

class Solution(object):
    #In this version, visit only hold one level of node, and queue hold the next level. 
    def getNeighbors(self, grid, node):
        result = {}
        (hi, wi) = node #a state is the position
        H, W = np.array(grid).shape
        top = (hi - 1, wi) if hi - 1 >= 0 and grid[hi - 1][wi] != "X" else None
        left = (hi, wi - 1) if wi - 1 >= 0 and grid[hi][wi - 1] != "X" else None
        right = (hi, wi + 1) if wi + 1 < W and grid[hi][wi + 1] != "X" else None
        bottom = (hi + 1, wi) if hi + 1 < H and grid[hi + 1][wi] != "X" else None
        return [item for item in (top, left, right, bottom) if item != None]
    
    def expandLevel(self, grid, nblist, visit):
        result = set()
        for nb in nblist:
            result = result.union(set(self.getNeighbors(grid, nb)))
        result = [item for item in result if item not in nblist and item not in visit]# return item in the next level that is not in current level
        return result
        
    def checkGoal(self, grid, curnode):
        (hi, wi) = curnode
        if grid[hi][wi] == '#':
            return True
        else:
            return False
    
    def BFS(self, grid, root):
        visit     = set()
        queue     = []
        nextlevel = []
        result = 0
        queue.append(root)
        while queue != None and len(queue) > 0:
            nextLevel = self.expandLevel(grid, queue, visit)
            print (f"Step {result}, visit: {visit}, queue: {queue}, nextLevel: {nextLevel}, ")
            visit = set(queue)
            while len(queue) > 0:
                curnode = queue.pop(0)
                if self.checkGoal(grid, curnode) == True:
                    return result #result corresponding to all node in queue
            
            queue = list(nextLevel)
            result += 1
        return -1
                
    def findRoot(self, grid):
        H, W = np.array(grid).shape
        for i in range(H):
            for j in range(W):
                if grid[i][j] == '*':
                    return (i, j)
        return False
        
    
    
    def getFood(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        root = self.findRoot(grid)
        goal = self.BFS(grid, root)
        return goal
    
    

grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
print (sol.getFood(grid))

grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
print (sol.getFood(grid))

grid = [["O","O","*","O"],["#","O","O","O"],["O","O","X","O"],["O","O","O","O"]]
print (sol.getFood(grid))