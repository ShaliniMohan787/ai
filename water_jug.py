from collections import deque 
 
def water_jug(a,b,target): 
    queue=deque([((0,0),[])]) 
    visited={(0,0)} 
 
    while queue: 
        (x,y),path=queue.popleft() 
 
        if x==target or y==target: 
            return path 
 
 
        possible_moves=[ 
            ((a,y),"Fill A"), 
            ((x,b),"Fill B"), 
            ((0,y),"Empty A"), 
            ((x,0),"Empty B"), 
            ((x-min(x,b-y),y+min(x,b-y)),"Pour A to B"), 
            ((x+min(y,a-x),y-min(y,a-x)),"Pour B to A")] 
 
        for state,action in possible_moves: 
            if state not in visited: 
                visited.add(state) 
                queue.append((state,path+[action])) 
 
steps=water_jug(4,3,2) 
if steps: 
    print("solution found") 
    for i,s in enumerate(steps,1): 
        print(i,s) 
else: 
        print("No solution")
