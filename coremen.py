n, k = map(int, input().split()) 
a = list(map(int, input().split())) 

b = a[:]

additional_walks = 0

for i in range(n - 1):
    if b[i] + b[i + 1] < k:
        needed_walks = k - (b[i] + b[i + 1])
        b[i + 1] += needed_walks
        additional_walks += needed_walks

print(additional_walks)
print(" ".join(map(str, b)))
