n, m, k = map(int, input().split())
dp = [[0 for _ in range(m)] for _ in range(n)]
if k == 0:
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                dp[i][j]=1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[n-1][m-1])
else:
    a = (k-1)//m
    b = (k-1)%m
    for i in range(n):
        for j in range(m):
            if i==a and j==b:
                p = dp[i-1][j]+dp[i][j-1]
            if (i==a and j>=b) or (j==b and i>=a):
                dp[i][j] = 1
            elif i==0 or j==0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
    print(p*dp[n-1][m-1])