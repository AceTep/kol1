# with open("ulaz.txt","r") as file:
#     data = file.readlines()

# brojevi = list(map(int, data[0].split('+')))


# brojevi.sort()
# nova_lista = '+'.join(map(str,brojevi))

# print(nova_lista)

n = input()
brojevi = list(map(int, n.split('+')))


brojevi.sort()
nova_lista = '+'.join(map(str,brojevi))

print(nova_lista)

