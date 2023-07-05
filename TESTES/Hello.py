# Para usar o acentos precisa do comando abaixo:
# -*- coding: utf-8 -*-
print("Hello World!")
print('Acentuaç        ão(áé"ç"ã)')

# operadores 
#  + - * /  ** %
# ** = Modulo, retorna o resto da divisão
print(2 ** 2)


# Tipo de variaveis.
variavel_string 	= "Olá mundo"
variavel_numeric 	= 123
variavel_float 		= 123.05
variavel_bool 		= True

"""Operadores logicos e Relacionais 
==
!=
>
<
>=
<=
AND 
OR
NOT
"""
x = 3
y = 4
print(x == y)

soma = x + y
print("soma > x? - ") 
print(soma == x)

# comandos condicionais 
# if 
x = 1
y = 2
if x > y:
	print("X é maior")
else:
	if y == x:
		print("Y é igual a X")
	else:
		print("Y é maior")


# varias condição elif
print ("elif======================")
x = 1
y = 2

if y == x:
		print("Y é igual a X")
elif y > x:
	print("y é maior")		
elif y < x:
	print("x é maior")		
else:
	print("Diferentes")


#repetição
x = 1
while x < 10:
	print(x)
	x += 1

print ("======================")
listaNum	= [1, 2, 3, 4, 5]
listaChar	= ['oi','teste']
listaMix	= [1, 'oi', True, 1.2]
x = 1
for x in listaChar:
	print(x)

print ("======================")
for x in range(10, 20, 2):
	print(x)

	
print ("======================")
# input

numero = input("Digite um numero: ")
print("o numero digitado é: ", numero)

nome = input("Digite um nome:")
print("Bem vindo, ", nome)
print("Bem vindo, " + nome)


#concatenação

nome 		= 'Vinicius'
sobrenome 	= 'Calixto'

print (nome + sobrenome)
