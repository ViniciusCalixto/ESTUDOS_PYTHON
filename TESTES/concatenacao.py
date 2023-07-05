#concatenação

nome 		= 'Vinicius'
sobrenome 	= 'Calixto'
concatenacao = nome + " " + sobrenome
print (concatenacao)

tamanho = len(concatenacao)
print(tamanho)

#colocando entre colchetes ele percorre a string e retorna o caractere da possição
print(concatenacao[3])
# imprimir parte de uma string tipo SUBSTRING
print(concatenacao[9:12])


# lower

print("original: " + concatenacao + "\nlower: " + concatenacao.lower() + "\nUPPER: "+ concatenacao.lower())


#remover caracteres de enter ou espaçonas estremidades
x = ' oloco \n asd \n'
print(x.strip())

#quebra string em lista
x = ' oloco asd asdasdad asda sd asd a'
print(x.split(' '))

#qual possição aparece tal palavra, traz a primeira que achar
print(x.find("sa"))

#subistituir palavras
print(x.replace("d","K"))
