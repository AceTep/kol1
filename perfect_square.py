import math

n = int(input())
numbers = list(map(int, input().split()))

max_non_square = -float('inf')

for num in numbers:
    if num < 0:
        is_sqare = False
    else:
        root = int(math.isqrt(num))
        is_sqare = (root * root == num)

    if not is_sqare:
        max_non_square = max(max_non_square, num)

print(max_non_square)
            