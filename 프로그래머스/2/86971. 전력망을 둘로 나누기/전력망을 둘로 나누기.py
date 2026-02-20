from collections import defaultdict
def solution(n, wires):
    
    graph = defaultdict(list)
    
    for u,v in wires:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n+1)
    cost = [1] * (n+1)
    parent = [0] * (n+1)
    visited[1] = True
    stack = [1]
    order =[]
    
    while stack:
        node = stack.pop()
        order.append(node)
        for v in graph[node]:
            if not visited[v]:
                parent[v] = node
                visited[v] = True
                stack.append(v)
    
    for node in reversed(order):
        if parent[node] != 0:
            cost[parent[node]] += cost[node]
    
    total = cost[1]
    target = total /2
    min_diff = float('inf')
    
    for i in range(1, n+1):
        diff = abs(target - cost[i])    
        min_diff = min(min_diff, diff)
    print(order)
    print(cost)
    return 2 * min_diff