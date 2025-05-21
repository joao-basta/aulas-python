import random

def jogo():
    dezenas = []
    print("Digite 6 números inteiros entre 1 e 60:")
    while len(dezenas) < 6:
        numero = int(input(f"Dezena {len(dezenas)+1}: "))
        if 1 <= numero <= 60:
            if numero not in dezenas:
                dezenas.append(numero)
            else:
                print("Número repetido. Digite outro.")
        else:
            print("Número inválido. Digite um número entre 1 e 60.")
    return sorted(dezenas)

def sort_dezenas():
    return sorted(random.sample(range(1, 61), 6))

def acertos(escolhidas, sorteadas):
    n_acertos = [num for num in escolhidas if num in sorteadas]
    return len(n_acertos), n_acertos

print("=== JOGO DE 6 DEZENAS ===")

palpites = jogo()
sorteio = sort_dezenas()

print("\nSuas dezenas:", palpites)
print("Dezenas sorteadas:", sorteio)

quantidade, numeros_acertados = acertos(palpites, sorteio)
print(f"\nVocê acertou {quantidade} número(s)!")
print("Palpites acertados:", numeros_acertados)
