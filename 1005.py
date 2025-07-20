from collections import deque

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    build_time = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(N + 1)]            # 건물 의존 그래프 graph[[이것의 이름은 graph[0]],[],[],[],[]]
    indegree = [0] * (N + 1)                      # 진입 차수
    dp = [0] * (N + 1)                

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y) # graph = [[0],[2,3],[],[],[]]
        indegree[Y] += 1 # indegree = [0],[0],[1],[0],[0]

    W = int(input())

    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = build_time[i]

    while q:
        cur = q.popleft()
        for next in graph[cur]:
            # 다음 건물까지 누적 시간 계산
            dp[next] = max(dp[next], dp[cur] + build_time[next])
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)

    print(dp[W])