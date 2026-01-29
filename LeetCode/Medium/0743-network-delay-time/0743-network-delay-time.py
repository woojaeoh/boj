from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    
        def dijkstra( graph, start):
            costs ={}
            pq = []
            heapq.heappush(pq , (0, start))

            while pq:
                cur_cost, cur_node = heapq.heappop(pq)
                if cur_node not in costs:
                    costs[cur_node] = cur_cost
                for next_node, cost in graph[cur_node]:
                    next_cost = cost + cur_cost    
                    heapq.heappush(pq, (next_cost, next_node))
            
            for i in range(n):
                if (i+1) not in costs:
                    return 0     
            
            return max(costs.values())

        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        result = dijkstra(graph, k)

        return -1 if result == 0 else result 