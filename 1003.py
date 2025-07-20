T = int(input())
test_cases = [int(input()) for _ in range(T)]

dp = [[0, 0] for _ in range(41)]

dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, 41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]  # 0이 출력된 횟수
    dp[i][1] = dp[i-1][1] + dp[i-2][1]  # 1이 출력된 횟수

# 테스트케이스 출력
for n in test_cases:
    print(dp[n][0], dp[n][1])