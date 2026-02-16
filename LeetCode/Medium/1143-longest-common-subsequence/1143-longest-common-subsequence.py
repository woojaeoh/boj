class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp =[0] * 1001
        n = len(text1)
        m = len(text2)

        cur_index = -1
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j] and j > cur_index:
                    dp[i] = max(dp) + 1
                    cur_index = j

                   
        print(dp[:n])
        return max(dp)