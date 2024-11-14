# with open("ulaz.txt", "r") as file:
#     data = file.readlines()

# n = int(data[0])
# index = 1

# for _ in range(n):
#     t = int(data[index])
#     index +=1
#     candies = list(map(int, data[index].split()))
#     index +=1

#     total_candies = sum(candies)
#     avg_candies = total_candies // t

#     count = sum(1 for candy in candies if candy > avg_candies)

#     if total_candies % t == 0:
#         print(count)
#     else: 
#         print(-1)


t = int(input())
    
for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    
    print()
    total_candies = sum(candies)
    avg_candies = total_candies // n  
    
    count = sum(1 for candy in candies if candy > avg_candies) 
    
    if total_candies % n == 0: 
        print(count)
    else:
        print(-1)