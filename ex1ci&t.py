def ultima_parada(combustivel,consumo,postos_de_gasolina):
  posto_ideal = combustivel * consumo
  postos_de_gasolina_com_posto_ideal = postos_de_gasolina.copy() + [posto_ideal]
  postos_de_gasolina_com_posto_ideal.sort()
  posto_ideal_index = postos_de_gasolina_com_posto_ideal.index(posto_ideal)
  if posto_ideal_index == 0:
    return -1
  ultimo_posto_na_autonomia = postos_de_gasolina_com_posto_ideal[posto_ideal_index - 1]
  return ultimo_posto_na_autonomia

print(ultima_parada(2, 8, [2, 15, 22, 10.2]))

#Você e seu time estão desenvolvendo um sistema de indicações de postos de gasolina que ficam próximos da localização atual do veículo. No modo de direção “viagem”, a funcionalidade a ser desenvolvida é de indicar ao condutor o posto mais distante possível dentro do limite atual de combustível. E caso não exista posto de gasolina, retornar -1

# A pessoa responsável por fazer a especificação do sistema informou que você terá as seguintes informações: consumo médio de combustível, quantidade de combustível restante no veículo e um array contendo distâncias dos postos de gasolinas.

# Exemplo:
# Combustivel (em litros): 2
# Consumo médio (km/l): 8
# Postos de Gasolina (km): [2, 15, 22, 10.2]