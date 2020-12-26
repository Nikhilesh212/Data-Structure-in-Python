# python3

import sys
import threading

sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self, node):
        if(node == -1):
            return
        self.inOrder(self.left[node])
        print(self.key[node],end=" ")
        self.inOrder(self.right[node])

    def preOrder(self, node):
        if(node != -1):
            print(self.key[node],end=" ")
            self.preOrder(self.left[node])
            self.preOrder(self.right[node])

    def postOrder(self,node):
        if(node != -1):
            self.postOrder(self.left[node])
            self.postOrder(self.right[node])
            print(self.key[node],end=" ")


def main():
    tree = TreeOrders()
    tree.read()
    tree.inOrder(0)
    print()
    tree.preOrder(0)
    print()
    tree.postOrder(0)
threading.Thread(target=main).start()
