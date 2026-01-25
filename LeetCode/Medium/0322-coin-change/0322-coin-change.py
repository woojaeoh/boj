from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # answer = 0
        # coins.sort(reverse = True)
        # for coin in coins:
        #     if amount >= coin :
        #        answer +=  amount // coin 
        #        amount = amount % coin
            
        #     if amount == 0 :
        #         return answer
        
        # return -1
        #dfs도 아님.

        # coins.sort(reverse=True)
        # n = len(coins)
        # answer= []

        # def backtracking(curr, coins, amount):
        #     curr_sum = sum(curr)

        #     if curr_sum == amount:
        #         answer.append(len(curr))
        #         return
        #     elif curr_sum > amount:
        #         return

        #     for i in range(n):
        #         if amount >= coins[i]:
        #             curr.append(coins[i])
        #             backtracking(curr, coins, amount)
        #             curr.pop()
        #         else:
        #             return -1

        #     return 1
        
        # if backtracking([], coins, amount):
        #     return min(answer)

        # if amount == 0:
        #     return 0

        # BFS

        coins.sort(reverse=True)
        n =  len(coins)
        
        
           
        q = deque()
        q.append((0, amount))
        
        visited= set([amount])


        while q:

            #cur_index, cur_depth, cur_amount = q.popleft()
            cur_depth, cur_amount = q.popleft()

            #BASE CASE
            if cur_amount == 0:
               return cur_depth

            #  동전을 차례로 들어갈 수 있는지
            for coin in coins:
                next_amount = cur_amount - coin 
                
                if next_amount >= 0 and next_amount not in visited:
                    q.append((cur_depth + 1, next_amount))
                    visited.add(next_amount)

                # if cur_index < n and coins[cur_index] <= cur_amount:
                #     q.append((cur_index+ 1, cur_depth + 1, cur_amount - coins[cur_index]))
                # elif cur_index < n and coins[cur_index] > cur_amount:
                #     q.append((cur_index +1, cur_depth ,cur_amount))


        #return -1       







        #coin change ->동전을 최소한으로 사용하는 경우
        #조합을 이용해 amount를 0으로 만들기

        # 완전탐색 -> 12의 12승 -> 탐색 불가.
        # 주어진 amount에서 coin을 빼서 0을 만드는 방식 -> dfs 백트래킹?
        # 상태공간 트리
        # 반복문을 돌면서 amount를 0을 만드는 방식 -> 가장 작은 min을 반환하려면?
        # 


        n = len(coins)
        coins.sort(reverse =True)

        def dfs(cur_coins, cur_amount):
            

            if cur_amount == 0:
                return cur_coins

            for coin in coins:
                if cur_amount >= coin and cur_amount-coin not in visited:
                    
                    visited.add(cur_amount-coin)
                    cur_amount -= coin

                    dfs(cur_coins+1, cur_amount)

        
        visited=set()
        visited.add(amount)

        return -1


        




















    