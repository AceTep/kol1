t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    
    min_val = min(x, y)
    max_val = max(x, y)
    
    if b < 2 * a:
        cost = min_val * b + (max_val - min_val) * a
    else:
        cost = (x + y) * a
    
    print(cost)
