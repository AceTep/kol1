n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

max_ratio = 0
max_ratio_count = 0

for front_teeth in a:
    for rear_teeth in b:
        if rear_teeth % front_teeth == 0:
            ratio = rear_teeth // front_teeth 
            if ratio > max_ratio:
                max_ratio = ratio
                max_ratio_count = 1  
            elif ratio == max_ratio:
                max_ratio_count += 1 

print(max_ratio_count)
