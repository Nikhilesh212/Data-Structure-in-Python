import sys
from random import randint as r

sys.setrecursionlimit(10**8)


def PH(S, p, x):
    H1 = [0] * (len(S[0]) + 1)
    H2 = [0] * (len(S[1]) + 1)
    l = max(len(S[0]), len(S[1]))
    for i in range(l):
        if i < len(S[0]):
            H1[i + 1] = (x * H1[i] + ord(S[0][i])) % p
        if i < len(S[1]):
            H2[i + 1] = (x * H2[i] + ord(S[1][i])) % p
    return H1, H2


def compare(S, x, p, lb, ub):
    global H1, H2
    l = (lb + ub) // 2
    if lb > ub:
        l1, l2 = len(S[0]), len(S[1])
        y = pow(x, l, p)
        h1 = {(H1[i + l] - y * H1[i]) % p: i for i in range(l1 - l + 1)}
        for i in range(l2 - l + 1):
            h2 = (H2[i + l] - y * H2[i]) % p
            if h2 in h1 and S[0][h1[h2]:h1[h2] + l - 1] == S[1][i:i + l - 1]:
                return h1[h2], i, l

    l1, l2 = len(S[0]), len(S[1])
    y = pow(x, l, p)
    h1 = {(H1[i + l] - y * H1[i]) % p: i for i in range(l1 - l + 1)}
    for i in range(l2 - l + 1):
        h2 = (H2[i + l] - y * H2[i]) % p
        if h2 in h1 and S[0][h1[h2]:h1[h2] + l - 1] == S[1][i:i + l - 1]:
            return compare(S, x, p, l + 1, ub)
    return compare(S, x, p, lb, l - 1)


p = 1000000007
x = r(1, p - 1)
while True:
    q = tuple(map(str, input().split()))
    H1, H2 = PH(q, p, x)
    Ans = compare(q, x, p, 0, min(len(q[0]), len(q[1])))
    print(*Ans)
