#Dissecando uma váriavel 

var = "ola"

print(f'O tipo primitivo desse valor é: {type(var)}') #Vai fazer a verificação do tipo primitivo da variavél
print(f'Só tem espaços: {var.isspace()}') #Vai verificar se só tem espaços na variavél
print(f'É um número: {var.isnumeric()}') #Vai verificar se a variavél é número
print(f'É alfabético: {var.isalpha()}') #Vai verificar se a variavél tem letra
print(f'É alfanumérico: {var.isalnum()}') #Vai verificar se tem letras e números
print(f'Está em maúscula: {var.isupper()}') #Verificar se a variavél está toda em maiúscula 
print(f'Está em minúscula: {var.islower()}') #Verificar se a variavél está toda em minúscula
print(f'Está capitalizada: {var.istitle()}') #Verificar se a primeira letra da variavél está em maiúscula
