# with open("ulaz.txt", "r") as file:
#     data = file.readlines()

# t = int(data[0])

# index = 1
# for _ in range(t):
#     a = int(data[index])
#     index +=1
#     lista = list(map(int, data[index].split()))
#     index +=1


#     while len(lista) > 0 and lista[0] == 0:
#         lista.pop(0)
#     while len(lista) > 0 and lista[-1] == 0:
#         lista.pop()
 
#     ans = 0
#     for i in range(len(lista)):
#         if lista[i] == 0:
#             ans += 1
 
#     if len(lista) == 0:
#         print(0)
#     elif ans != 0:
#         print(2)
#     else:
#         print(1)


t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    
    while len(v) > 0 and v[0] == 0:
        v.pop(0)
    while len(v) > 0 and v[-1] == 0:
        v.pop()
    
    ans = 0
    for i in range(len(v)):
        if v[i] == 0:
            ans += 1
    
    if len(v) == 0:
        print(0)
    elif ans != 0:
        print(2)
    else:
        print(1)