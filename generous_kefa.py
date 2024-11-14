b,f = map(int, input().split())
arr = input().strip()
col_count = {}

for c in arr:
    if c in col_count:
         col_count[c] += 1
    else: 
         col_count[c] = 1

possible = True
for count in col_count.values():
    if count > f:
         possible = False
         break
    
if possible:
     print("YES")
else:
    print("NO")

