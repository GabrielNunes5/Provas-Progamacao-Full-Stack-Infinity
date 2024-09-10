qnt_alunos = int(input('Quantos alunos deseja inserir as notas: '))
media_geral = 0
for alunos in range(qnt_alunos):
    aluno = input('Insira o nome do aluno: ')
    nota1 = int(input(f'Insira a primeira nota do aluno {aluno}: '))
    nota2 = int(input(f'Insira a segunda nota do aluno {aluno}: '))
    nota3 = int(input(f'Insira a terceira nota do aluno {aluno}: '))
    media_aluno = (nota1 + nota2 + nota3) / 3  
    if media_aluno < 7:
        print(f'O aluno {aluno} foi reprovado! Sua media foi: {media_aluno:.2f} e suas notas foram: {nota1},{nota2},{nota3}')
    else:
        print(f'O aluno {aluno} foi aprovado! Sua media foi: {media_aluno:.2f} e suas notas foram: {nota1},{nota2},{nota3}')

    media_geral += media_aluno

media_geral = media_geral/qnt_alunos
print(f'A media geral dos alunos foi de: {media_geral:.2f}')