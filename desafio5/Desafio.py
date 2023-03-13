palavra = input("digite oq deseja: ")

conversao = ""

for x in range(len(palavra)-1,-1,-1):
    conversao += palavra[x]

print (conversao)