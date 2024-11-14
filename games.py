# with open("ulaz.txt","r") as file:
#     data = file.readlines()

# count = 0
# n = int(data[0].strip())
# uniforms = [line.strip() for line in data[1:n+1]]

# for i in range(n):
#     home_color_i, guest_color_i = uniforms[i].split()
#     for j in range(n):
#         if i!=j:
#             home_color_j, guest_color_j  = uniforms[j].split()

#             if home_color_i == guest_color_j:
#                 count += 1 

# print(count)
# 

n = int(input())
uniforms = []
for _ in range(n):
    home, guest = map(int, input().split())
    uniforms.append((home,guest))

count = 0

for i in range(n):
    home_color_i, guest_color_i = uniforms[i]
    for j in range(n):
        if i!=j:
            home_color_j, guest_color_j  = uniforms[j]

            if home_color_i == guest_color_j:
                count += 1 

print(count)