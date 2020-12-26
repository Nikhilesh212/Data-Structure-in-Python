
# Solution video - https://www.youtube.com/watch?v=lsQTYlCiU6c


def rect(h):
    stack = []
    area = i = 0
    h.append(0)
    while i < len(h):
        if not len(stack) or h[stack[-1]] < h[i]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            area = max(area, h[top] * (i - stack[-1] - 1 if stack else i))
    return area

n = int(input())
h = list(map(int, input().split()))
print(rect(h))
