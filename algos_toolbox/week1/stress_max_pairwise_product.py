# Uses python3
# Uses python3
import random
import copy
def multip(a):
    x2 = 0
    x1 = 0
    for i in range(0, n):
        if a[i] > x1:
            x2 = copy.copy(x1)
            x1 = copy.copy(a[i])
    return x1*x2  

while True:
    n = random.randint(2,100)
    a = random.sample(range(1000),n)
    assert(len(a) == n)

    result = 0

    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > result:
                result = a[i]*a[j]
    if result == multip(a):
        print(result,multip(a),'ok')
    else:
        print(result,multip(a),'wrong')