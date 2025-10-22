from collections import deque 
 
# Start and Goal states 
start = [1, 3, 0, 6, 8, 4, 7, 5, 2] 
goal  = [1, 2, 3, 4, 5, 6, 7, 8, 0] 
 
q = deque([(start, [])]) 
visited = {tuple(start)} 
 
while q: 
    s, path = q.popleft() 
 
    # If goal is reached 
    if s == goal: 
        for step in path + [s]: 
            for i in range(0, 9, 3): 
                print(step[i:i+3]) 
            print("---") 
        print("Solved in", len(path), "moves") 
        break 
 
    # Position of blank (0) 
    z = s.index(0) 
    row, col = divmod(z, 3) 
 
    # Possible moves: up, down, left, right 
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]: 
        nr, nc = row + dr, col + dc 
 
        if 0 <= nr < 3 and 0 <= nc < 3: 
            new = s[:] 
            nz = nr * 3 + nc 
            new[z], new[nz] = new[nz], new[z] 
 
            if tuple(new) not in visited: 
                visited.add(tuple(new)) 
                q.append((new, path + [s]))
