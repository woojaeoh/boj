import heapq
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((succProb[i], v))
            graph[v].append((succProb[i], u))

        costs={}
        pq =[]
        heapq.heappush(pq, (-1, start_node, end_node)) #시작노드        

        while pq:
            weight , cur_node, end = heapq.heappop(pq)
            if cur_node not in costs:
                costs[cur_node] = -1 * weight

            if cur_node == end:
                return -1 * weight
            
            for cur_weight, next_node in graph[cur_node]:
                if next_node not in costs:
                    next_weight = weight * cur_weight
                    heapq.heappush(pq, (next_weight, next_node, end))
                    
        for i in range(end_node+1):
            if i not in costs:
                return 0
        
        return -1