class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0 
        visited = set()
        directions=[(-1,0),(0,1),(1,0),(0,-1)]

        def islands(x,y):
             for dx, dy in directions:
                nx,ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n and grid[nx][ny]=='1' and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    islands(nx,ny)


        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1' and (x,y) not in visited:
                    count +=1
                    visited.add((x,y))
                    islands(x,y)        

        return count












   