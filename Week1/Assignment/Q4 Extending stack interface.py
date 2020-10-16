class Node:
    def __init__(self,data=None):
        self.data=data
        self.max=None
        self.next=None
        self.tail=None
class Stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        if(self.head is None):
            self.max=data
            self.head=Node(data)
            self.tail=self.head
        else:
            curr=self.head
            while(curr.next):
                curr=curr.next
            curr.next=Node(data)
            self.tail=curr
            if(self.max<data):
                self.max=data
    def pop(self):
        m=-99
        curr=self.head
        temp=self.tail.next.data
        if(self.tail.next.data is self.max):
            while(curr.next):
                if(int(curr.data)>m):
                    m=int(curr.data)
                curr=curr.next
            self.max=m
        self.tail.next=None
        return temp
S=Stack()
Output=[]
for i in range(int(input())):
    Q = str(input())
    if Q.startswith('push'):
        S.push(Q[5:])
    elif Q.startswith('pop'):
        S.pop()
    elif Q.startswith('max'):
        Output.append(S.max)

print(*Output, sep='\n')
