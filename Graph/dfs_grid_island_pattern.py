from typing import List, TypeVar, Dict, Any 

T = TypeVar('T')

def num_islands(grid: list[list[int]]):
    rows, cols = len(grid), len(grid[0])
    visited = set() 
    
    def dfs(r: int, c: int):
        if (
            r < 0 or r >= rows or 
            c < 0 or c >= cols or 
            (r, c) in visited or 
            grid[r][c] == '0'
        ):
            return 
        
        visited.add((r, c)) 
        
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
        
    count = 0 
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)
                count += 1 
    return count 



"""
1 1 0
0 1 0
1 0 1
"""