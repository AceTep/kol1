# with open("ulaz.txt", "r") as file:
#     data = file.readlines()

# n = int(data[0].strip())

# i = 1
# for _ in range(n):
#     t = int(data[i])
#     i += 1
#     candies = list(map(int, data[i].split()))
#     i += 1

#     c1 = candies.count(1)
#     c2 = candies.count(2)

#     if (c1 % 2 == 0 and c2 % 2 == 0) or(c1 % 2 == 0 and c1> 0):        print("YES")
#     else:
#         print("NO")

t = int(input()) 

for _ in range(t):
    n = int(input())  
    candies = list(map(int, input().split()))  

    count1 = candies.count(1)
    count2 = candies.count(2)


    if (count1 % 2 == 0 and count2 % 2 == 0) or(count1 % 2 == 0 and count1> 0):
        print("YES")
    else:
        print("NO")
