# with open("ulaz.txt","r") as file:
#     data = file.readlines()

# t = int(data[0].strip())
# results = []
# index = 1

# for _ in range(t):
#     n = int(data[index])
#     index += 1
#     cream_layers = list(map(int, data[index].split()))
#     index += 1
#     drenched = [0] * n  
#     coverage = 0  
    
#     for i in range(n - 1, -1, -1):
#         coverage = max(coverage, cream_layers[i])
#         if coverage > 0:  
#             drenched[i] = 1
#             coverage -= 1  
    
#     results.append(' '.join(map(str, drenched)))  
# print( '\n'.join(results))

t = int(input())
results = []
index = 1

for _ in range(t):
    n = int(input())
    index += 1
    cream_layers = list(map(int, input().split()))
    index += 1
    drenched = [0] * n  
    coverage = 0  
    
    for i in range(n - 1, -1, -1):
        coverage = max(coverage, cream_layers[i])
        if coverage > 0:  
            drenched[i] = 1
            coverage -= 1  
    
    results.append(' '.join(map(str, drenched)))  
print( '\n'.join(results))




