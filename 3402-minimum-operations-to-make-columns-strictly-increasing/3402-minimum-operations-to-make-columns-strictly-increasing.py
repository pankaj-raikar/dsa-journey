class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        
        rows=len(grid)
        cols=len(grid[0])

        operation=0

        for col in range(cols):
            for row in range(1,rows):
                if grid[row][col]<=grid[row-1][col]:
                    req=grid[row-1][col]+1
                    operation+=req-grid[row][col]

                    grid[row][col]=req
                
        return operation
        
