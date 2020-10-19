import sys
from collections import deque

Q = deque()
S, N = map(int, sys.stdin.readline().split())
if N == 0:
    quit()
rem = S
Ans = [-1] * N
if S > 0:
    rem -= 1
    Q.append(list(map(int, sys.stdin.readline().split())) + [0])
else:
    for i in range(N):
        print(-1)
    quit()

for i in range(N - 1):
    currpacket = list(map(int, sys.stdin.readline().split()))
    currpacket.append(i + 1)
    if len(Q) == 0:
        rem -= 1
        Q.append(currpacket)
    else:
        while len(Q) > 0 and currpacket[0] >= Q[0][1]:
            ans = Q.popleft()
            Ans[ans[2]] = ans[0]
            rem += 1
        if rem > 0:
            if len(Q) > 0:
                currpacket[0] = Q[-1][1]
            currpacket[1] += currpacket[0]
            Q.append(currpacket)
            rem -= 1


for q in Q:
    Ans[q[2]] = q[0]

print(*Ans, sep='\n')
