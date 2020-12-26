import sys
import threading

sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(input())
        self.key = [0] * self.n
        self.left = [0] * self.n
        self.right = [0] * self.n

        for i in range(self.n):
            a, b, c = map(int, input().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self, node, l):
        if self.n and node != -1:
            self.inOrder(self.left[node], l)
            l.append(self.key[node])
            if len(l) > 1 and ((l[-1] < l[-2]) or
            (self.left[node] != -1 and self.key[node] == self.key[self.left[node]])):
                print('INCORRECT')
                quit()
            self.inOrder(self.right[node], l)


def main():
    tree = TreeOrders()
    tree.read()
    tree.inOrder(0, [])
    print('CORRECT')



threading.Thread(target=main).start()
