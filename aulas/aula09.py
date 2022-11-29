frase = '    Curso em Vídeo Python    '
#print(frase) #mostra todo o conteúdo da string

#print(frase[3]) #mostra o conteúdo da string na posição 3

#print(frase[3:13]) #mostra o conteúdo da string da posição 3 até a posição 13

#print(frase[:13]) #mostra a string da posição 0 até a posição 13

#print(frase[13:]) #mostra o conteudo da string da posição 13 até o final

#print(frase[1:15:2]) #mostra o que há na string, da posição 1 até a posição 15, pulando de 2 em 2

#print('oi') #mostra um oi na tela

#print('''Cedo ou tarde, você vai aprender, assim como eu aprendi, que existe uma diferença entre CONHECER o caminho e TRILHAR o caminho.(filme Matrix)''') #mostra a frase mesmo se ela tiver mais de uma linha. Bom para cabeçalho.

#print(frase.count('o')) #mostra quantas vezes aparece a letra o

#print(frase.upper().count('O')) #transforma todas as letras para maiusculas e mostra quantas vezes aparece a letra O maniuscula

#print(len(frase)) #mostra quanto digitos tem a frase

#print(len(frase.strip())) #mostra quantos digitados tem a frase desconsiderando os espaços vazios antes e depois da frase.

#print(frase.replace('Python', 'Android'))  #mostra a string na tela substituindo a palavra python por android

#print('Curso' in frase) #consulta se a palavra entre aspas esta na string e retorna True ou False

#print(frase.find('Curso')) #retorna o número da posição na qual aparece a palavra entre aspas.

#print(frase.lower().find('vídeo')) #alterar toda a string para minuscula e procura pela palavra entre aspas e retorna sua posição

#print(frase.split()) #mostra a string transformada em lista

dividido = frase.split() #criou uma variavel que recebeu a string transformada em lista
#print(dividido[0]) #mostra na tela o item da posição
#print(dividido[2] [3]) #pega o segundo item da lista e mostra a letra que aparece na posição 3
