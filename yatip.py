# with open("ulaz.txt","r") as file:
#     data = file.readlines()

# n = int(data[0].strip())

# brojevi = [line.strip() for line in data[1:n+1]]

# print(brojevi)

# lista = []
# for i in range(n):
#     a,b = brojevi[i].split()

#     diff = abs(int(a)-int(b))
#     moves = int((diff+9)/10)
#     lista.append(moves)

# print(lista)

# import math

n = int(input())

brojevi = []
for _ in range(n):
    a,b = map(int, input().split())
    brojevi.append((a,b))


lista = []
for i in range(n):
    a,b = brojevi[i]

    diff = abs(int(a)-int(b))
    # moves = math.ceil(diff / 10)
    moves = int((diff+9)/10)
    lista.append(moves)

for i in lista:
    print(i)