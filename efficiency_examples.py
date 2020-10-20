def g(n):
    t = 0
    j = n
    while j > 1:
        t = t+1
        j = j/2
    return t
print(g(64))
## returns ceiling( log(n) )

def f(n):
    t = 0
    for i in range(0,n):
        for j in range(0,2*i):
            t = t+1
    return t
print(f(5))
## returns n(n-1)
