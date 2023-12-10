import random

def jogo_adivinhar(adivinhar, computador):
    return adivinhar == computador

armazenar_numero = random.randint(1, 5)
    
tentativas = 5

while tentativas > 0:
    
    adivinhar_numero = int(input('Tente adivinhar um número que estou pensando de 1 a 5: '))
    
    if adivinhar_numero > 5 or adivinhar_numero == 0:
        print('Somente numeros de 1 ate 5')
        continue
    
    if jogo_adivinhar(adivinhar_numero, armazenar_numero):
        print('Vc acertou\nFIM')
        break
    else:
        tentativas -= 1
        print(f'Vc errou\nTentativas restantes {tentativas}')

if tentativas == 0:
    print('Suas chances acabaram')