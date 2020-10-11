class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, entry):
        self.stack.append(entry)

    def pop(self):
        return self.stack.pop()

    def __len__(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1]

    def empty(self):
        return len(self.stack) == 0

    def __repr__(self):
        return self.stack.__repr__()


def brackets(s):
    c = 0
    Brackets = Stack()
    for i in s:
        c += 1
        if i in ('(', '[', '{'):
            Brackets.push((i,c))
        elif i in (')', ']', '}'):
            if Brackets.empty():
                return c
            Top = Brackets.pop()[0]
            if (i == ')' and Top != '(') or (i == ']' and Top != '[') or (i == '}' and Top != '{'):
                return c
    if Brackets.empty():
        return 'Success'
    else:
        while not Brackets.empty():
            last = Brackets.pop()
        return last[1]


print(brackets(str(input())))
