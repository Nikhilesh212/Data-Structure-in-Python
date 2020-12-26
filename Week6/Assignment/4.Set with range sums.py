# import sys, threading
# sys.setrecursionlimit(10**9)
# threading.stack_size(2**27)
f = open("20.txt","r")

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=None
        self.height=1
        self.size=1

    def __repr__(self):
        return str(node.data)

class AVL:
    def __init__(self):
        self.head=None

    def node_size(self,node):
        if node:
            return 1+self.node_size(node.left)+self.node_size(node.right)
        else:
            return 0

    def height(self,node):
        if not node:
            return 0
        else:
            # rH = 0
            # lH = 0
            # if node.left:
                # if node.right:
            #     rH = node.right.height
            # return 1 + max(lH, rH)
            return 1+max(self.height(node.left),self.height(node.right))

    def delete(self, val):
        node = self.find(val)
        if not node:
            return
        x = self.next(node.data)
        if not x:
            if node.parent and not node.left:
                node.parent.right = None
            elif node.parent:
                node.parent.right = node.left
                node.left.parent = node.parent
            else:
                self.head = node.left
                if node.left:
                    node.left.parent = None

        elif not node.right:
            if node.parent.left == node:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
            if node.left:
                node.left.parent = node.parent
        else:
            node.data = x.data
            if x.parent.left == x:
                x.parent.left = x.right
            else:
                x.parent.right = x.right
            if x.right:
                x.right.parent = x.parent
        del node
        self.adjustheight(self.head)

    def next(self, val):
        node = self.find(val)
        if node.right:
            node = node.right
            while node.left:
                node = node.left
        else:
            while node.parent and node.parent.left != node:
                node = node.parent
            node = node.parent
        return node
    def find(self,data):
        curr=self.head
        prv=None
        while(curr):
            if(curr.data==data):
                return curr
            elif curr.data>data:
                prv=curr
                if curr.left:
                    curr=curr.left
                else:
                    return prv
            elif curr.data<data:
                prv=curr
                if curr.right:
                    curr=curr.right
                else:
                    return prv
        return prv

    def rc_size(self,node):
        if(node):
            node.size=self.node_size(node)
            self.rc_size(node.left)
            self.rc_size(node.right)

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
        self.rc_size(self.head)

    def adjustheight(self,head):
        if(head):
            head.height=self.height(head)
            self.adjustheight(head.left)
            self.adjustheight(head.right)


    def os(self,node,k):
        s=node.left.size
        if k== s+1:
            return node.data
        elif k<s+1:
            return self.os(node.left,k)
        else:
            return self.os(node.right,k-s-1)

    def rotate_right(self,X):
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

    # def del_node(self,data):
    #     s=self.find(data)
    #     if s.right is None :
    #         if s.left is None:
    #             s.parent = None
    #             del s
    #         else:
    #             s.parent = s.left
    #             del s
    #     else:
    #         curr=s.right
    #         while curr:
    #             curr=curr.left
    #         s.parent=curr
    #         curr.left=s.left
    #         curr.right=s.right
    #     elif()
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
        self.rc_size(self.head)

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

    def range_sum(self,curr,l,h):
        # if curr:
        #     if (curr.data>=l and curr.data<=h):
        #         return curr.data+self.range_sum(curr.left,l,h)+self.range_sum(curr.right,l,h)
        #     else:
        #         return self.range_sum(curr.left,l,h)+self.range_sum(curr.right,l,h)
        # else:
        #     return 0

a=AVL()
M=1000000001
x=0
for i in f:
    q=list(map(str,i.split()))
    if q[0]=="+":
        a.insert((int(q[1])+x)%M)
    elif q[0]=="?":
        ans=a.find((int(q[1])+x)%M)
        if(ans and ans.data==(int(q[1])+x)%M):
            print("Found")
        else:
            print("Not found")

    elif q[0]=="s":
        s=a.find((int(q[2])+x)%M)
        q1=(int(q[1])+x)%M
        q2=(int(q[2])+x)%M
        if s is None:
            s=a.find((int(q[1])+x)%M)
        while(s):
            if (not s.parent) or (s.parent.data<s.data):
                if s.parent:
                    s=s.parent
                break
            s=s.parent

        x= a.range_sum(s,q1,q2)
        print(x)

    elif q[0]=='-':
        q=(int(q[1])+x)%M
        while(True):
            e = a.find(q)
            if(e and e.data == q):
                a.delete(q)
            else:
                break
    elif q[0]=="t":
        a.p(a.head)
