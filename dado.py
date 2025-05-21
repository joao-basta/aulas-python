import random
 
print("Qual o seu palpite para a soma dos dois dados?\n")
 
def dado_usuario():
    chance = int(input("Digite um número de 2 a 12: "))
    while chance < 2 or chance > 12:
        chance = int(input("Digite um número válido: "))
    return chance
 
chance1 = dado_usuario()
 
if chance1 == 2 or chance1 == 12:
    print("\nSua chance de acertar é 1 em 36, em porcentagem é 2,78%\n")
elif chance1 == 3 or chance1 == 11:
    print("\nSua chance de acertar é 2 em 36, em porcentagem é 5,55%\n")
elif chance1 == 4 or chance1 == 10:
    print("\nSua chance de acertar é 3 em 36, em porcentagem é 8,33%\n")
elif chance1 == 5 or chance1 == 9:
    print("\nSua chance de acertar é 4 em 36, em porcentagem é 11,11%\n")
elif chance1 == 6 or chance1 == 8:
    print("\nSua chance de acertar é 5 em 36, em porcentagem é 13,89%\n")
elif chance1 == 7:
    print("\nSua chance de acertar é 6 em 36, em porcentagem é 16,66%\n")
 
def soma_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    dado3 = dado1 + dado2
    return dado3
 
soma = soma_dados()
 
if soma == chance1:
    print(f"Você acertou! Seu palpite foi {chance1} e a soma foi {soma}.")
else:
    print(f"Você errou! Seu palpite foi {chance1} e a soma foi {soma}.")
 
resultados = []
for i in range (100000):
    numero = soma_dados()
    resultados.append(numero)
 
 
print(f"O número 2  apareceu: {resultados.count(2)}   vezes")
print(f"O número 3  apareceu: {resultados.count(3)}   vezes")
print(f"O número 4  apareceu: {resultados.count(4)}   vezes")
print(f"O número 5  apareceu: {resultados.count(5)}  vezes")
print(f"O número 6  apareceu: {resultados.count(6)}  vezes")
print(f"O número 7  apareceu: {resultados.count(7)}  vezes")
print(f"O número 8  apareceu: {resultados.count(8)}  vezes")
print(f"O número 9  apareceu: {resultados.count(9)}  vezes")
print(f"O número 10 apareceu: {resultados.count(10)}   vezes")
print(f"O número 11 apareceu: {resultados.count(11)}   vezes")
print(f"O número 12 apareceu: {resultados.count(12)}   vezes")
       