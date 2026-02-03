from collections import defaultdict
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        

        #그래프 완성  -> 0: (1, 0.5) 
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        costs = {}
        pq =[]
        heapq.heappush(pq, (-1, start_node))
        costs[start_node] = 0

        while pq:
            cost, cur_node = heapq.heappop(pq)

            if cur_node not in costs:
                costs[cur_node] = -1 * cost

            if cur_node == end_node:
                return -1 * cost

            for next_node, weight in graph[cur_node]:
                if next_node not in costs:
                    next_cost  = weight * cost
                    heapq.heappush( pq, (next_cost, next_node))

                
        return 0
                 