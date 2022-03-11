N, K = map(int, input().split())
n = max(N, K)
dp = [0] * (n+1)
if K > N :
    for i in range(N-1,-1, -1):
            dp[i] = dp[i+1] + 1
    for i in range(N+1,K+1):
        if i % 2 == 0:
            dp[i] = min(dp[i-1]+1, dp[i//2]+1)
        else:
            dp[i] = min(dp[i-1]+1, dp[(i+1)//2]+2)
    print(dp[K])
elif K == N:
    print(0)
else:
    for i in range(N-1, K-1, -1):
        dp[i] = dp[i+1] + 1
    print(dp[K])