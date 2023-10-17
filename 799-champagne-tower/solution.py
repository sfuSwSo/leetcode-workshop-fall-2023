class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        grid = [[0 for i in range(query_glass+1)] for j in range(query_row+1)]
        grid[0][0] = poured

        for i in range(1, query_row+1):
            for j in range(query_glass+1):
                left = 0
                if i-1 >= 0 and j-1 >= 0 and grid[i-1][j-1] > 1:
                    left = (grid[i-1][j-1]-1) / 2
                top = 0
                if i-1 >= 0 and grid[i-1][j] > 1:
                    top = (grid[i-1][j]-1) / 2

                grid[i][j] = left+top

        return grid[query_row][query_glass] if grid[query_row][query_glass] < 1 else 1