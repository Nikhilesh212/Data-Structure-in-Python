class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=None
        self.height=1
        self.size=1

class BST:
    def __init__(self):
        self.head=None

    def insert(self,data):
        if self.head is None:
            self.head=Node(data[0])
        else:

list=[tuple(map(int,input().split()))for i in range(int(input()))]
