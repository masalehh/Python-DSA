from collections import deque 

def bfs_grid(grid, sr, sc):
    rows, cols = len(grid), len(grid[0])
    visited = set() 
    directions = [(1,0), (-1,0), (0,1), (0,-1)]  # (1,0) → down (-1,0) → up (0,1) → right (0,-1) → left
    
    queue = deque([(sr, sc)]) 
    visited.add((sr, sc)) 
    
    while queue:
        r, c = queue.popleft() 
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc 
            if (0 <= nr < rows and 
                0 <= nc < cols and 
                (nr, nc) not in visited and 
                grid[nr][nc] == 1):
                
                visited.add((nr, nc))
                queue.append((nr, nc))
                
                

"""
1 1 0 1
0 1 1 0
1 0 1 0


🔵 1  ⬜ 1
⬜ 1  1  ⬜
1  ⬜ 1  ⬜


✅ 🔵 ⬜ 1
⬜ 1  1  ⬜
1  ⬜ 1  ⬜


✅ ✅ ⬜ 1
⬜ ✅ ✅ ⬜
1  ⬜ ✅ ⬜


"""