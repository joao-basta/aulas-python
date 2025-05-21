#1 PEÇA 6 DEZENAS PARA O USUARIO(LISTA) (FUNÇÃO)
#2 SORTEIE 6 DEZENAS (RANDOM) MAX DE 1 A 60
#3 APRESENTE A QUANTIDADE DE NUMEROS ACERTADOS(FUNÇÃO)
import random
def jogo():
    dezenas= []
    print("Digite 6 numeros inteiros entre 1 e 60:") 
    while len(dezenas)< 6:
        numero = int(input(f"Dezena {len(dezenas)+1}: "))
        if 1<= numero <=60:
            if numero not in dezenas:
                dezenas.append(numero)
            else:
                print("numero repetido. Digite outro")
        else:
            print("numero invalido. Digite um numero entre 1 e 60")
    return sorted (dezenas)
def sort_dezenas():
    dezenas = []
    while len (dezenas)<6:
        num = random.randint(1,60)
        if num not in dezenas:
            dezenas.append(num)
    return sorted(dezenas)
def acertos(escolhidas, sorteadas):
    n_acertos=[]
    for num in escolhidas:
        if num in sorteadas and num not in n_acertos:
            n_acertos.append(num)
    return len (n_acertos), n_acertos
    
print("=== JOGO DE 6 DEZENAS ===")

palpites = jogo()

sorteio = sort_dezenas()

print("\nSuas dezenas:", palpites)
print("Dezenas sorteadas:", sorteio)

quantidade, numeros_acertados = acertos(palpites, sorteio)
print(f"\nVocê acertou {quantidade} número(s)!")
print("Palpites acertados:", numeros_acertados)