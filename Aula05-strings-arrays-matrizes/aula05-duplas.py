nomes = ["Ana", "Lara", "Luiz", "Caio"]

#print(nomes[0])

for i in range(len(nomes)):
    for j in range(i + 1, len(nomes)):
        print("Dupla:", nomes[i],"e", nomes[j])