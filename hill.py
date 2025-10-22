import random 
 
d=[ 
    [0,10,15,20], 
    [10,0,35,25], 
    [15,35,0,25], 
    [20,25,35,15]] 
 
def dist(p): 
    return sum(d[p[i]] [p[(i+1)%len(p)]] for i in range(len(p))) 
 
def solve(): 
    p=list(range(len(d))) 
    random.shuffle(p) 
    for _ in range(1000): 
        i,j=random.sample(range(len(p)),2) 
        new=p[:] 
        new[i], new[j]= new[j], new[i] 
        if dist(new)<dist(p): 
            p=new 
 
        return p 
 
path=solve() 
print("Path",path) 
print("Distance",dist(path))
