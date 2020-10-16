from collections import deque

buff, n = map(int, input().split())
l = []
ans = [0] * n
size = 0
time = 0
a_prv = None
curr = 0
t = []
r = 0
for i in range(n):
    ai, pi = map(int, input().split())
    if(ai > curr and ai > time):
        time += min((ai - curr), (ai - time))
    if(ai > time):
        time += ai - curr
    t = [(t - i) for i in a]
    for j in range(len(t)):
        if(t[j] != None and t[j] <= ai):
            t[j] = None
            size -= 1
            break
    if(size >= buff):
        ans[i] = -1
    elif(ai == a_prv or a_prv == None):
        curr = ai + 1
        ans[i] = time
        size += 1
        time += pi
        t.append(time)
    elif(ai != a_prv):
        curr += ai + 1
        ans[i] = time
        time += pi
        size += 1
        t.append(time)
    a_prv = ai

print(*ans, sep='\n')
