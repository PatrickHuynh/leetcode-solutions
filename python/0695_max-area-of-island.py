class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        verified_land = set()
        grid_row_max = len(grid)
        grid_col_max = len(grid[0])
        
        def get_island(row, col, island):
            if grid[row][col] == 1:
                island.add((row,col))
                verified_land.add((row, col))
                cells = zip([row, row, row-1, row+1], [col-1, col+1, col, col])
                for cell in cells:
                    if 0 <= cell[0] < grid_row_max and 0 <= cell[1] < grid_col_max and cell not in island:
                        island = get_island(cell[0], cell[1], island)
            return island
        
        max_island_size = 0
        for i in range(grid_row_max):
            for j in range(grid_col_max):
                if grid[i][j] == 1 and (i, j) not in verified_land:
                    max_island_size = max(max_island_size, len(get_island(i, j, set())))
                    
        return max_island_size