def lista_separada(lista_aninhada):
    flat_list = []
    for sublist in lista_aninhada:
      for item in sublist:
          flat_list.append(item)
    return flat_list
def filtra_vendas(valores_gerais):
    menor_valor_considerado = 20
    maior_valor_considerado = 500
    filtrado = list(filter(lambda ticket: ticket >= menor_valor_considerado and ticket <= maior_valor_considerado, valores_gerais))
    return filtrado
def retorna_menor_e_maior_valor_de_vendas(tickets):
    valores_gerais = lista_separada(tickets)
    filtrado = filtra_vendas(valores_gerais)
    lista_menor_e_maior = [min(filtrado), max(filtrado)]      
    return lista_menor_e_maior




# Você está trabalhando para uma empresa que fornece materiais escolares e precisa da sua ajuda para entrar no mundo digital. Como primeira atividade, você identificou que não existe uma funcionalidade que é muito importante para a empresa ter mais controle sobre os valores dos produtos vendidos. Esta funcionalidade consiste em descobrir o maior e o menor valor dos produtos vendidos em um período de tempo, para cada vendedor.

# Os valores das vendas que devem ser consideradas podem variar entre 20 e 500 reais e estão agrupados por vendedores. Além disso, deve-se ignorar as devoluções, que estão indicadas com o valor 0.

# A sua função/método deverá receber uma lista vendas agrupadas por vendedores, (e.g. [[200, 100], [300]]) e retornar um array onde a primeira posição contém o menor valor e a segunda posição o maior valor (e.g. [100, 300]).

# Mas preste atenção! Algum vendedor pode não ter realizado vendas no período.