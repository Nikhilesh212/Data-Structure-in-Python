class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else :
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node

    def pop(self):
        temp=self.head
        self.head=temp.next
        return temp.data

    def empty(self):
        if( self.head is None):
            return True
        else:
            return False

def check(st):
    Stack=stack()
    for s in st:
        if( s =='(' or s=='[' or s=='{'):
            Stack.push(s)
        elif(s ==')' or s==']' or s=='}'):
            if(Stack.empty()):
                return False
            else:
                temp=Stack.pop()
                if(temp=='(' and s==')' or temp=='[' and s==']' or temp=='{' and s=='}'):
                    continue
                else:
                    return False
    return Stack.empty()
print(check('{}[]'))
