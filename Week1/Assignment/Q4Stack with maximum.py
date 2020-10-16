
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None
        self.max=None
        self.second=None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
            self.max=data
            self.second=None
        else :
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
            if(data>self.max):
                self.second=self.max
                self.max=data
            elif(data>self.second or self.second is None):
                self.second =data

    def pop(self):
        temp=self.head
        if(temp.data==self.max and self.second is not None):
            self.max=self.second
            self.second =None
        elif(self.second is None):

            curr=temp.next
            while(curr):
                if(curr.data<self.max and curr.data>self.second):
                    self.second=curr.data
                curr=curr.next
        self.head=temp.next
        return temp.data

S=stack()
Output=[]
for i in range(int(input())):
    Q = str(input())

    if Q.startswith('push'):
        S.push(int(Q[5:]))
    if Q[0:3]=='pop':
        S.pop()
    elif Q.startswith('max'):
        Output.append(S.max)

print(*Output, sep='\n')
