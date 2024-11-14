n = int(input())

num = list(map(int, input().split()))
count =  1
best = 1
for i in range(n-1):
    if num[i] < num[i+1]:
        count +=1
        best = max(best, count)
    else:
        count = 1

print(best)