#Ler uma frase e informas quantos 'A' aparece, qual a posição 1° e do último.

#Meu método
fras = str(input('Digite uma frase: ')).strip().lower()
quantidade = fras.count('a')
print(f'Na frase {fras}, a letra "A" aparece {quantidade} vezes.')
print(f'O primeiro "A" aparece na {fras.find("a") + 1}ª posição')
print(f'O ultimo "A" está na posição {fras.find("a") - fras.count("a")}') #←erro, não cheguei ao resultado esperado.

#Método Guanabara
frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count("A")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.find("A")+1}')
print(f'A ultima letra A apareceu na posição {frase.rfind("A")+1}')