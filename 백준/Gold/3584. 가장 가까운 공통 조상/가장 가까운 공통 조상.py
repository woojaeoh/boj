import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    graph =[[] for _ in range(N+1)]
    parent = [0] *(N+1)
    depth =[0] *(N+1) 
    
    nodes = set(range(1, N+1))
    child = set()
    
    for _ in range(N-1):
        p , c = map(int, input().split())       
        graph[p].append(c)
        graph[c].append(p)
        child.add(c)
    
    root = (nodes - child).pop()
  
    def dfs(cur, p, d):
        parent[cur] = p
        depth[cur] = d
        for v in graph[cur]:
            if v == p:
                continue
            dfs(v, cur, d+1)
              
    def LCA(p, q):
        while depth[p] != depth[q] :
            if depth[p] > depth[q] :
                p = parent[p]
            else:
                q = parent[q]
        while p != q:
            p = parent[p]
            q = parent[q]
            
        return p or q      
            
    
    dfs(root, 0, 0)    
    p, q = map(int, input().split())  
    print(LCA(p,q))