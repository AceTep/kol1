# with open("ulaz.txt", "r") as file:
#     data = file.readlines()

# t = int(data[0])
# for i in range(1,t):
#     a,b,c,x,y = map(int, data[i].split())

#     x -= min(a,x)
#     y -= min(b,y)

#     enough = (x+y <= c)

#     if(enough):
#         print("YES")
#     else:
#         print("NO")


t = int(input())
    
for _ in range(t):
    a, b, c, x, y = map(int, input().split())
    
    x -= min(a, x)
    y -= min(b, y)
    
    enough_food = (x + y <= c)
    
    if enough_food:
        print("YES")
    else:
        print("NO")