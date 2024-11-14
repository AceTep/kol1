bills = [1,5,10,20,100]
bills.reverse()

n = int(input())
count = 0
for i in bills:
    if n >= i:
        count += n // i
        n %= i

print(count)