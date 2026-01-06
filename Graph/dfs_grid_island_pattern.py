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
        
        visited.add((r, c))     # function come to this point if it is 1 and we marked it as visited 
        
        # from this point check all 4 directions if any connected land or 1 
        dfs(r+1, c)     # Down 
        dfs(r-1, c)     # Up 
        dfs(r, c+1)     # Right 
        dfs(r, c-1)     # Left 
        
        
    count = 0 
    for r in range(rows):
        for c in range(cols):   # started visiting from (0,0) and complete visiting row by row 
            # if any coordinate not 0 not starting dfs or previous visited 
            if grid[r][c] == '1' and (r, c) not in visited: 
                dfs(r, c)       # call dfs  
                count += 1      # if this coordinate has atleast a 1 then its must be an island so increase the count 
    return count                # finally return the count means number of islands 



"""
1 1 0
0 1 0
1 0 1
"""