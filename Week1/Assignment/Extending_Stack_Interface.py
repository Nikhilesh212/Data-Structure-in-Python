import sys


class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return

    def empty(self):
        return len(self.stack) == 0

    def __len__(self):
        return len(self.stack)

    def __repr__(self):
        return 'Stack({})'.format(self.stack.__repr__())


S = Stack()
maxS = Stack()
Output = []

q = int(sys.stdin.readline())
for _ in range(q):
    Q = str(sys.stdin.readline())
    if Q.startswith('push'):
        n = int(Q[5:])
        S.push(n)
        if maxS.empty():
            maxS.push(n)
        elif (n >= maxS.peek()):
            maxS.push(n)
    elif Q.startswith('pop'):
        k = S.pop()
        if not maxS.empty() and (k == maxS.peek()):
            maxS.pop()
    elif Q.startswith('max'):
        Output.append(maxS.peek())

print(*Output, sep='\n')
