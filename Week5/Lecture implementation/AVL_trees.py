
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=None
        self.height=1

class AVL:
    def __init__(self):
        self.head=None

    def height(self,i):
        if(i is None):return 0
        else:return 1+max(self.height(i.left),self.height(i.right))

    def find(self,data):
        curr=self.head
        while(True):
            if(curr.data==data or curr.data is None):
                return curr
            elif(curr.data>data):
                curr=curr.left
            elif(curr.data<data):
                curr=curr.right

    def insert(self,data):
        if self.head is None:
            self.head=Node(data)

        else:
            curr=self.head
            while(True):
                if(curr.data>=data):
                    if(curr.left):
                        curr=curr.left
                    else:
                        curr.left=Node(data)
                        curr.left.parent=curr
                        self.rebalance(curr.left)
                        break
                elif(curr.data<data):
                    if(curr.right):
                        curr=curr.right
                    else:
                        curr.right=Node(data)
                        curr.right.parent=curr
                        self.rebalance(curr.right)
                        break

    def adjustheight(self,head):
        if(head):
            head.height=self.height(head)
            self.adjustheight(head.left)
            self.adjustheight(head.right)

    def rotate_right(self,X):
        # p=node.parent
        # y=node.left
        # b=node.left.right
        # y.parent=p
        # if(y.data>p.data):
        #     p.right=y
        # else:
        #     p.left=y
        # node.parent=y
        # y.right=node
        # b.parent=node
        # node.left=b
        B = X.left.right
        X.left.parent = X.parent
        if X.parent and X == X.parent.left:
            X.parent.left = X.left
        elif X.parent and X == X.parent.right:
            X.parent.right = X.left
        else:
            self.head = X.left
        X.parent = X.left
        X.left.right = X
        X.left = B
        if X.left:
            X.left.parent = X

    def rotate_left(self, X):
        B = X.right.left
        X.right.parent = X.parent
        if X.parent and X == X.parent.left:
            X.parent.left = X.right
        elif X.parent and X == X.parent.right:
            X.parent.right = X.right
        else:
            self.head=X.right
        X.parent = X.right
        X.right.left = X
        X.right = B
        if X.right:
            X.right.parent = X

    def p(self,head):
        if(head):
            if(head.left):
                print(head.data,"->",head.left.data)
            self.p(head.left)
            if(head.right):
                print(head.data,"->",head.right.data)
            self.p(head.right)

    def rebalance(self,node):
        p=node.parent
        if(node.left):
            lh=node.left.height
        else:
            lh=0
        if node.right:
            rh=node.right.height
        else:
            rh=0
        if(lh>rh+1):
            self.rebalance_right(node)
        if(rh>lh+1):
            self.rebalance_left(node)
        self.adjustheight(node)
        if(p):
            self.rebalance(p)

    def rebalance_right(self,node):
        m=node.left
        if(m.left):
            lh=m.left.height
        else:
            lh=0
        rh=0
        if m.right:
            rh=m.right.height
        if(rh>lh):
            self.rotate_left(m)
        self.rotate_right(node)

    def rebalance_left(self,node):
        m=node.right
        if(m.left):
            lh=m.left.height
        else:
            lh=0
        rh=0
        if m.right:
            rh=m.right.height
        if(lh>rh):
            self.rotate_right(m)
        self.rotate_left(node)

a=AVL()
while(True):
    i=int(input())
    if(i==1):
        l=list(map(int,input().split()))
        for i in l:
            a.insert(i)
    elif(i==2):
        a.p(a.head)
        print("________________________________________")
    else:
        exit()
