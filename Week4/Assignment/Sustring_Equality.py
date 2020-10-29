from random import randint as r

def PH(S, p, x):
    lS = len(S)
    H = [0] * (lS + 1)
    for i in range(lS):
        H[i + 1] = (x * H[i] + ord(S[i])) % p
    return H


def compare(S, q, x, p):
    global H
    y = pow(x, q[2], p)

    h1 = (H[q[0] + q[2]] - y * H[q[0]]) % p
    h2 = (H[q[1] + q[2]] - y * H[q[1]]) % p

    if h1 == h2:
        return 'Yes'
    return 'No'


S = input()
p = 1000000007
x = r(1, p - 1)
H = PH(S, p, x)
Q = int(input())
q = [tuple(map(int, input().split())) for _ in range(Q)]
Ans = [compare(S, i, x, p) for i in q]
print(*Ans, sep='\n')
