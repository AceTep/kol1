n,v = map(int, input().split())

if v >= n-1:
    print(n-1)
else:
    cost = v
    for i in range(2,n-v+1):
        cost += i
    print(cost)