from collections import deque
n = int(input())
l = list(map(int, input().split()))
m = int(input())
q = deque()
for i in range(m):
    while q and l[i] >= l[q[-1]]:
        q.pop()
    q.append(i)

for i in range(m, n):
    print(l[q[0]], end=' ')
    while q and q[0] <= i - m:
        q.popleft()
    while q and l[i] >= l[q[-1]]:
        q.pop()
    q.append(i)
print(l[q[0]],end=' ')
