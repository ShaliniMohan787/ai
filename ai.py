from collections import deque

# Initial and goal states
start = (3, 3, 'L')  # 3 missionaries, 3 cannibals, boat on left
goal = (0, 0, 'R')

# Possible boat moves
moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

def is_valid(state):
    M_left, C_left, side = state
    M_right, C_right = 3 - M_left, 3 - C_left
    
    # Invalid if out of range
    if not (0 <= M_left <= 3 and 0 <= C_left <= 3):
        return False
    
    # Missionaries eaten if outnumbered (on either bank)
    if (M_left > 0 and C_left > M_left):
        return False
    if (M_right > 0 and C_right > M_right):
        return False
    
    return True

def successors(state):
    M_left, C_left, side = state
    next_states = []
    
    for m, c in moves:
        if side == 'L':  # boat moves left → right
            new_state = (M_left - m, C_left - c, 'R')
        else:            # boat moves right → left
            new_state = (M_left + m, C_left + c, 'L')
        
        if is_valid(new_state):
            next_states.append(new_state)
    
    return next_states

def bfs(start, goal):
    queue = deque([(start, [start])])  # (state, path)
    visited = set([start])
    
    while queue:
        state, path = queue.popleft()
        
        if state == goal:
            return path
        
        for next_state in successors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
    
    return None

# Run BFS
solution = bfs(start, goal)

if solution:
    print("Solution found in", len(solution)-1, "steps:")
    for step, s in enumerate(solution):
        print(f"Step {step}: {s}")
else:
    print("No solution found.")
