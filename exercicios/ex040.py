#Ler duas notas de um aluno, calcular sua média e informar se ele está aprovado, reprovado ou em recuperação

#Meu método
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota2 + nota1)/2

if media >= 7:
    print(f'Sua média foi {media:.2f}, Você está aprovado!')
elif 5 <= media <= 6.9:
    print(f'Sua média foi {media:.2f}, Você está em recuperação!')
elif media < 5:
    print(f'Sua média foi {media:.2f}, Você está reprovado!')

#Método Guanabara
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {média:.1f}')
if 7 > média >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif média < 5:
    print('O aluno está REPROVADO.')
elif média >= 7:
    print('O aluno está APROVADO.')