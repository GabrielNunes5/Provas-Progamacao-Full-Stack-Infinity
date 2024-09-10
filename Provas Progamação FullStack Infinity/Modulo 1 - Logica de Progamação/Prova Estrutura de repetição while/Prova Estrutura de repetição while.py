numSecreto = 7
tentativasMax = 3
tentativa = int (input('Adivinhe o numero: '))
while tentativa != numSecreto and tentativasMax > 0:
    tentativasMax -= 1
    tentativa = int (input(f'Numero incorreto.Tente novamente, você possui {tentativasMax} tentativas: '))
if tentativa == numSecreto:
    print('Parabens! Você acertou o numero Secreto')
else:
    print(f'Suas tentativas acabaram, o numero secreto era: {numSecreto}')