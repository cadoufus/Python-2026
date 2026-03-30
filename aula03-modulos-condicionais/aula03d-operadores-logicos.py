# lógica E (and)
# email     senha     login(resultado)
# true      false       false
# false     true        false
# true      true        true
# false     false       false

verifica_email = True
verifica_senha = True

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("Entra no programa.. executa...")

#logia OU (or)
logica_ou = False or True
print(logica_ou)

#operador de NEGAÇÃO (not)
negacao= not False
print(negacao)

if not verifica_login:
    print("loga ai...")