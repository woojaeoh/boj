def solution(land):
    N = len(land)
    
    dp =[[0]*4 for _ in range(N)] #dp테이블 생성.
    dp[0] = [land[0][0], land[0][1], land[0][2], land[0][3]]
    
    for i in range(1,N):
        dp[i][0] = land[i][0] + max(dp[i-1][1], dp[i-1][2], dp[i-1][3])
        dp[i][1] = land[i][1] + max(dp[i-1][0], dp[i-1][2], dp[i-1][3])
        dp[i][2] = land[i][2] + max(dp[i-1][0], dp[i-1][1], dp[i-1][3])
        dp[i][3] = land[i][3] + max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
        
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    
    return max(dp[-1])