with open("ulaz.txt", "r") as file:
    data = file.readlines()

n = int(data[0].strip())

lines = [line.strip() for line in data[1:n+1]]
problem_solved = 0

for i in lines:
    temp = 0
    for j in i:
        if j=='1':
            temp += 1
    if temp >= 2:
        problem_solved += 1

print(problem_solved)


# n = int(input())

# problem_solved = 0

# for _ in range(n):
#     p,v,t = map(int, input().split())

#     count = p + v + t

#     if count >= 2:
#         problem_solved += 1

# print(problem_solved)