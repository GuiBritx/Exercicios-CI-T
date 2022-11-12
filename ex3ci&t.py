def lista_separada(lista_aninhada):
    flat_list = []
    for sublist in lista_aninhada:
      for item in sublist:
          flat_list.append(int(item))
    return flat_list
def calcula_numero_da_senha(senha): 
    return converter_binario_decimal(somando_as_colunas(lista_separada(senha)))
def somando_as_colunas(flat_list):
    resultado = ""
    def converter_soma(soma):
      if soma >= 5:
          return "1"
      else: 
          return "0"     
    for i in range(0, 10):
      soma_coluna_i = flat_list[0 + i] + flat_list[10 + i] + flat_list[20 + i] + flat_list[30 + i] + flat_list[40 + i] + flat_list[50 + i] + flat_list[60 + i] + flat_list[70 + i] + flat_list[80 + i] + flat_list[90 + i]
      resultado += converter_soma(soma_coluna_i)   
    return resultado
def converter_binario_decimal(binario):
    resultado_inverso = binario[::-1]
    resultado_decimal = 0
    for index, char in enumerate(list(resultado_inverso)):
      if char == "0":
        continue
      resultado_decimal += 2**index
    return resultado_decimal
        
# for j in range(0, 100, 10):
#   soma_coluna_i = flat_list[j + i] ...
    
  


# Durante uma expedição tecnológica, sua equipe encontrou o que parece ser a senha que lhes dá acesso a um grande tesouro digital. Por sorte, sua equipe é formada pelas pessoas mais feras em programação e vocês rapidamente descobriram como decifrá-la.

# Com a possibilidade de que vocês encontrem mais códigos contendo outras senhas, você foi designado à tarefa de desenvolver um algoritmo que decifra os códigos para não precisarem fazer isso de forma manual.

# A senha é representada por um número binário de 10 dígitos formado pelo dígito predominante de cada coluna. Caso a coluna tenha a mesma quantidade de dígitos 0 e 1, deve se considerar o número 1.

# Exemplo: A primeira coluna da lista tem como dígito predominante o número 1, sendo assim, o primeiro dígito - dos 10 - da senha é 1.

# 0110100000
# 1001011111
# 1110001010
# 0111010101
# 0011100110
# 1010011001
# 1101100100
# 1011010100
# 1001100111
# 1000011000

# Desenvolva um algoritmo que receba um array de valores binários (como o exemplo acima) e retorne a representação decimal da senha.