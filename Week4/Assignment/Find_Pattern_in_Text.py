def hash(S, p, x):
    h = 0
    for i in reversed(S):
        h = (h * x + ord(i)) % p
    return h


def PH(S, P, p, x):
    lP, lS = len(P), len(S)
    s = hash(S[-lP:], p, x)
    i = lS - lP - 1
    H = [0] * (i + 2)
    H[lS - lP] = s
    y = pow(x, lP, p)
    while i >= 0:
        H[i] = (x * H[i + 1] + ord(S[i]) - y * ord(S[i + lP])) % p
        i -= 1
    return H


x = 2
p = 1000000007
P = input()
S = input()
lP, lS = len(P), len(S)
h = hash(P, p, x)
H = PH(S, P, p, x)
Ans = [str(i) for i in range(len(H)) if H[i] == h]
print(' '.join(Ans))
