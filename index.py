#Declarando os números por extenso em tuplas
um_digito = ('', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove') # 0 - 9
dois_digitos = ('Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove') # 10 - 19
dezenas = ('Vinte', 'Trinta', 'Quarenta', 'Cinquenta', 'Sessenta', 'setenta', 'Oitenta', 'Noventa')
centenas = ('Cento', 'Duzentos', 'Trezentos', 'Quatrocentos', 'Quinhentos', 'Seiscentos', 'Setecentos', 'Oitocentos', 'Novecentos')
sufixos = ('Mil', 'Milhão', 'Bilhão')

#Recebe o número e o índice
def conversao(numero):
	#Se o número digitado for 0
	if numero == '0':
		# Nesse ponto a função será executada até aqui e retornará o 'Zero'
		return um_digito[0]

	#Se de alguma forma o numero (str) tiver mais de 3 caracetere
	quantidade_de_caracteres = len(numero)
	if (quantidade_de_caracteres > 3):
		return False

	#Se o número passar pelas duas condições acima 
	#Agora será preciso separar o número em grupo de três caracteres
	numero = numero.zfill(3) # 001, 023, 345
	palavras = ''

	#Como serão usados também como index para pegar os elementos nas tuplas
	#Então é necessário converter de str() para int()
	primeiro_digito = int(numero[0])
	segundo_digito = int(numero[1])
	terceiro_digito = int(numero[2])
	
	#Se o segundo digito for maior que 1
	if (primeiro_digito == 1) and (segundo_digito == 1):
		palavras += centenas[primeiro_digito - 1] # Cento
		palavras += ' e '
		palavras += dois_digitos[terceiro_digito] # 17 - Dezessete

	elif (primeiro_digito == 1) and (segundo_digito > 1):
		palavras += centenas[primeiro_digito - 1] # Cento
		palavras += ' e '
		palavras += dezenas[segundo_digito - 2] # Vinte e
		palavras += ' e '
		#Exemplo se o terceiro dígito for 3
		palavras += um_digito[terceiro_digito] # Vinte e três

	elif (primeiro_digito > 1) and (segundo_digito == 1):
		palavras += centenas[primeiro_digito - 1] # Cento
		palavras += ' e '
		palavras += dois_digitos[terceiro_digito] # 17 - Dezessete

	elif (primeiro_digito > 1) and (segundo_digito > 1):
		palavras += centenas[primeiro_digito - 1] # Cento
		palavras += ' e '
		palavras += dezenas[segundo_digito - 2] # Vinte e
		palavras += ' e '
		#Exemplo se o terceiro dígito for 3
		palavras += um_digito[terceiro_digito] # Vinte e três

	elif (primeiro_digito > 1) and (segundo_digito == 0) and (terceiro_digito == 0):
		palavras += centenas[primeiro_digito - 1] # Cento

	elif (primeiro_digito == 1) and (segundo_digito == 0) and (terceiro_digito == 0):
		palavras += 'Cem'

	elif (segundo_digito > 1):
		#Como se trata do segundo dígito então vamos tratar sobre dezenas
		#Exemplo se o segundo dígito for 2
		palavras += dezenas[segundo_digito - 2] # Vinte e
		palavras += ' e '
		#Exemplo se o terceiro dígito for 3
		palavras += um_digito[terceiro_digito] # Vinte e três
	
	#Se for igual a 1
	elif(segundo_digito == 1):
		#retorna a palavra por extenso de index equivalente ao número terceiro número
		palavras += dois_digitos[terceiro_digito]# 17 - Dezessete

	#Se o terceiro dígito for igual a zero
	#Ou seja se o número for de 0 - 9
	elif(segundo_digito == 0):
		palavras += um_digito[terceiro_digito]

	return palavras

def pegar_numeros(numero):

	#Essa variável guardará os números que serão tratados
	numeroFinal = list()

	#====> Tratando os caracteres <====
	#Caso o número tenha uma vírgula separando os decimais
	#Exemplos: 25.000,00 ou 25000,00
	if (numero.find(',') != -1):
		#Separa em uma lista os caracteres antes da vírgula na posição 0 e os que estão após
		#A vírgula na posição 1 ex: 1500,00 ====> ['1500', '00']
		listaDeNumeros = numero.split(',')
		#Depois transforma esses valores em interios
		#Por precaução, se o numéro tiver um separador de milhar (.) deve ser retirado
		numeroFinal.append(int(listaDeNumeros[0].replace('.', '')))
		numeroFinal.append(int(listaDeNumeros[1]))

	#Caso o número não tenha uma vírgula separando os decimais e sim um (.)
	#Exemplos: 25.000.45 ou 25000.45
	elif (numero.find('.', -3) != -1):
		listaDeNumeros = list()
		#Coloca na lista os numeros antes na separação de decimais
		listaDeNumeros.append(numero[:-3]) #25.000 ou 25000
		#Depois adiciona a lista os números decimais excluindo o (.)
		listaDeNumeros.append(numero[-2:]) #Apenas o 45
		#Depois transforma esses valores em interios
		#Por precaução, se o numéro tiver um separador de milhar (.) deve ser retirado
		numeroFinal.append(int(listaDeNumeros[0].replace('.', '')))
		numeroFinal.append(int(listaDeNumeros[1]))

	#Se o número não tiver nenhum separador de decimal
	#Exemplos: 25.000 ou 25000
	else:
		#Por precaução, se o numéro tiver um separador de milhar (.) deve ser retirado
		listaDeNumeros = int(numero.replace('.', ''))
		numeroFinal.append(listaDeNumeros)

	if (len(numeroFinal) == 1):
		if (len(str(numeroFinal[0])) > 9):
			return 'Desculpe-me, mas só consigo converter números até 999.999.999,99'
		elif (len(str(numeroFinal[0])) == 9):
			numero_feito = f'{conversao(str(numeroFinal[0])[:3])} Milhões '
			numero_feito += f'{conversao(str(numeroFinal[0])[3:6])} Mil '
			numero_feito += f'{conversao(str(numeroFinal[0])[6:])} Reais '
			return numero_feito
		elif (len(str(numeroFinal[0])) == 8):
			numero_feito = f'{conversao(str(numeroFinal[0])[:2])} Milhões '
			numero_feito += f'{conversao(str(numeroFinal[0])[2:5])} Mil '
			numero_feito += f'{conversao(str(numeroFinal[0])[5:])} Reais '
			return numero_feito
		elif (len(str(numeroFinal[0])) == 7):
			numero_feito = f'{conversao(str(numeroFinal[0])[:1])} Milhões '
			numero_feito += f'{conversao(str(numeroFinal[0])[1:4])} Mil '
			numero_feito += f'{conversao(str(numeroFinal[0])[4:])} Reais '
			return numero_feito
		elif (len(str(numeroFinal[0])) == 6):
			numero_feito = f'{conversao(str(numeroFinal[0])[:3])} Mil '
			numero_feito += f'{conversao(str(numeroFinal[0])[3:])} Reais '
			return numero_feito
		elif (len(str(numeroFinal[0])) == 5):
			numero_feito = f'{conversao(str(numeroFinal[0])[:2])} Mil '
			numero_feito += f'{conversao(str(numeroFinal[0])[2:])} Reais '
			return numero_feito
		elif (len(str(numeroFinal[0])) == 4):
			numero_feito = f'{conversao(str(numeroFinal[0])[:1])} Mil '
			numero_feito += f'{conversao(str(numeroFinal[0])[1:])} Reais '
			return numero_feito
		elif (len(str(numeroFinal[0])) <= 3):
			if (str(numeroFinal[0]) == '1'):
				numero_feito = f'{conversao(str(numeroFinal[0]))} Real '
				return numero_feito
			else:
				numero_feito = f'{conversao(str(numeroFinal[0]))} Reais '
				return numero_feito
	else:
		if (len(str(numeroFinal[0])) > 9):
			return 'Desculpe-me, mas só consigo converter números até 999.999.999,99'
		elif (len(str(numeroFinal[0])) == 9):
			numero_feito = f'{conversao(str(numeroFinal[0])[:3])} Milhões '
			numero_feito += f'{conversao(str(numeroFinal[0])[3:6])} Mil '
			numero_feito += f'{conversao(str(numeroFinal[0])[6:])} Reais '
			numero_feito += f' e {conversao(str(numeroFinal[1]))} Centavos'
			return numero_feito
		elif (len(str(numeroFinal[0])) == 8):
			numero_feito = f'{conversao(str(numeroFinal[0])[:2])} Milhões '
			numero_feito += f'{conversao(str(numeroFinal[0])[2:5])} Mil '
			numero_feito += f'{conversao(str(numeroFinal[0])[5:])} Reais '
			numero_feito += f' e {conversao(str(numeroFinal[1]))} Centavos'
			return numero_feito
		elif (len(str(numeroFinal[0])) == 7):
			numero_feito = f'{conversao(str(numeroFinal[0])[:1])} Milhões '
			numero_feito += f'{conversao(str(numeroFinal[0])[1:4])} Mil '
			numero_feito += f'{conversao(str(numeroFinal[0])[4:])} Reais '
			numero_feito += f' e {conversao(str(numeroFinal[1]))} Centavos'
			return numero_feito
		elif (len(str(numeroFinal[0])) == 6):
			numero_feito = f'{conversao(str(numeroFinal[0])[:3])} Mil '
			numero_feito += f'{conversao(str(numeroFinal[0])[3:])} Reais '
			numero_feito += f' e {conversao(str(numeroFinal[1]))} Centavos'
			return numero_feito
		elif (len(str(numeroFinal[0])) == 5):
			numero_feito = f'{conversao(str(numeroFinal[0])[:2])} Mil '
			numero_feito += f'{conversao(str(numeroFinal[0])[2:])} Reais '
			numero_feito += f' e {conversao(str(numeroFinal[1]))} Centavos'
			return numero_feito
		elif (len(str(numeroFinal[0])) == 4):
			numero_feito = f'{conversao(str(numeroFinal[0])[:1])} Mil '
			numero_feito += f'{conversao(str(numeroFinal[0])[1:])} Reais '
			numero_feito += f' e {conversao(str(numeroFinal[1]))} Centavos'
			return numero_feito
		elif (len(str(numeroFinal[0])) <= 3):
			if (str(numeroFinal[0]) == '1'):
				numero_feito = f'{conversao(str(numeroFinal[0]))} Real '
				numero_feito += f' e {conversao(str(numeroFinal[1]))} Centavos'
				return numero_feito
			else:
				numero_feito = f'{conversao(str(numeroFinal[0]))} Reais '
				numero_feito += f' e {conversao(str(numeroFinal[1]))} Centavos'
				return numero_feito


if __name__ == '__main__':
	numero = input('Por favor, digite um valor que você deseja converter para valor em extenso:\n')
	print(pegar_numeros(numero))