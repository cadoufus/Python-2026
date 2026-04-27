# cp = 0
# while cp < 10:
#     cp += 1
#
#     if cp == 3 or cp == 5:
#         continue
#
#     if cp == 7:
#         break
#
#     print(f"Produto {cp}")
#
# i = 4
# while i > 0:
#     print(i)
#     i -= 1
def validar_nota(nota):
    while nota < 0 or nota > 10:
        print("A nota deve ser entre 0 e 10")
        nota = float(input("Digite novamente a nota: "))
    return nota

notaA = float(input("Digite a primeira nota: "))
notaA = validar_nota(notaA)

notaB = float(input("Digite a segunda nota: "))
notaB = validar_nota(notaB)

media = (notaA + notaB) / 2
print(media)