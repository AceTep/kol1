# with open("ulaz.txt", "r") as file:
#     data = file.readlines()

# t = int(data[0])

# for i in range(1,t):
#     n, m, k = map(int, data[i].split())
#     total_cost = (n-1) + (m-1) * n

#     if total_cost == k:
#         print("YES")
#     else:
#         print("NO")


t = int(input())
    
for _ in range(t):
    n, m, k = map(int, input().split())
    
    total_cost = (n - 1) + (m - 1) * n
    
    if total_cost == k:
        print("YES")
    else:
        print("NO")