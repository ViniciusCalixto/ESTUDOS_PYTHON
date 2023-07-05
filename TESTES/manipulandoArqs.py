#manipulando arquivos.
'''		
modo = função 
r 	 = somente leitura
w 	 = escrita - sobrescreve arquivo
a 	 = leitura e escrita - incrementa no fim do arquivo
r+ 	 = leitura e escrita
w+ 	 = escrita  sobrescreve arquivo
a+ 	 = leirtura e escrita - abre arquivo para atualização 

----------


'''

Arquivo = open("Arquivo.txt")

print(Arquivo.read())
Arquivo.close()


Arquivo = open("Arquivo.txt")
linhas = Arquivo.readlines()
for linha in linhas:
	print(linha)
Arquivo.close()


Arquivo = open("Arq2.txt","w")
Arquivo.write("escrever dentro do arquivo\n")
Arquivo.close()

Arquivo = open("Arq2.txt")
print(Arquivo.read())
Arquivo.close()