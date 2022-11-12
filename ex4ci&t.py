def calcula_top_ocorrencias_de_queries(texto,queries,k):
    ocorrencias = {}
    resultado = []
    for i in queries:
      seila = texto.count(i)
      ocorrencias[i] = seila
    oco2 = list(sorted(ocorrencias, key = ocorrencias.get, reverse=True))
    return (oco2[0:k])
    



# Dada um texto qualquer e um lista de termos de pesquisa (sequencia de caracteres), retorne os primeiros K termos mais recorrentes na string, onde K é um parâmetro configurável.

# Exemplo:

# String: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"

# Lista de termos: ["a", "em", "i", "el"]

# K: 2

# Resultado: ["i", "a"]

# Explicação:

# Ocorrências de cada termo,"i": 11, "a": 7, "em": 2, "el": 1, com K = 2, retornamos "i" e "a" ordenados conforme a quantidade de ocorrências de cada termo.

# Obs: Quando houver termos com quantidades iguais, priorizar o retorno de acordo com a ordem de ocorrência do termo na string.