from collections import defaultdict, deque
import heapq
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w+1))
            graph[v].append((u, w+1))
        
        pq = []
        dist = [float('inf')] * n
        dist[0] = 0
        heapq.heappush(pq, (0, 0)) # 0번 노드, 가중치 0 

        while pq:
            node, cur_move = heapq.heappop(pq)
            
            for next_node, cost in graph[node]:
                new_cost = cur_move + cost
                if new_cost < dist[next_node]:
                    dist[next_node] = new_cost
                    heapq.heappush(pq, (next_node, new_cost))

        print(dist)

        ans = sum(1 for d in dist if maxMoves >= d)

        for x, y, w in edges:
            wx, wy = maxMoves - dist[x], maxMoves - dist[y]
            if wx >= 0 and wy >= 0:
                ans +=  wx + wy - max(wx + wy -w, 0) 
            else:
                ans += max(wx,0) + max(wy, 0)


        return ans




        
            
        

            