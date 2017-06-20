# Uses python3

n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

x1 = 0
x2 = 0
x1 = max(a)
a.remove(x1)
x2 = max(a)
print(x1*x2)
