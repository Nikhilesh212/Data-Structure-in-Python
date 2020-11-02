class Node:
    def __init__(self,data=None):
        self.data=data
        self.height=0
        self.left=None
        self.right=None

class AVL:
    def __init__(self):
        self.head=None

    def height(self,i):
        print(i)
        if(self.tree[i] is None):return 0
        else:return 1+max(self.height(leftchild(i)),self.height(rightchild(i)))

    def find(self,data):
        curr=self.head
        while(True):
            if(curr.data==data or curr.data is None):
                return curr
            elif(curr.data>data):
                curr=curr.left
            elif(curr.data<data):
                curr=curr.right

    def insert(self,root,data):
        if root is None:
            root=Node(data)
        else:
            if root.data <= key:
                return self.insert(self,root.right,data)
            else:
                return self.insert(self,root.left,data)
        return root
    def p(self,head):
        if(head):
            print(head.data)
            self.p(head.left)
            self.p(head.right)
a=AVL()
while(True):
    i=int(input())
    if(i==1):
        l=list(map(int,input().split()))
        for i in l:
            a.insert(a.head,23i)
    elif(i==2):
        a.p(a.head)
    else:
        exit()
