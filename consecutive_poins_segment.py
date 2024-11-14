def process_case(n, x):
    if x[-1] - x[0] <= n - 1:
        return "YES"
    return "NO"

t = int(input())  
for _ in range(t):
    n = int(input())  
    x = list(map(int, input().split()))  
    print(process_case(n, x))
