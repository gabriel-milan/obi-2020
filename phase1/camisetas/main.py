#
# Olimpíada Brasileira de Informática
# Fase 1
# Atividade: Camisetas da olimpíada
# Autor: Gabriel Gazola Milan
#

def get_inputs ():
  try:
    n = int(input())
  except Exception as e:
    print ("Falhou ao pegar input N")
    raise e
  try:
    Xi = input()
  except Exception as e:
    print ("Falhou ao pegar o tamanho solicitado!")
    raise e
  try:
    P = int(input())
  except Exception as e:
    print ("Falhou ao pegar input P")
    raise e
  try:
    M = int(input())
  except Exception as e:
    print ("Falhou ao pegar input M")
    raise e
  return n, Xi, P, M

def check_inputs (inputs):
  n, xi, p, m = inputs
  if n < 1:
    raise ValueError ("N deve ser maior ou igual a 1")
  elif n > 1000:
    raise ValueError ("N deve ser menor ou igual a 1000")
  if p < 0:
    raise ValueError ("P deve ser maior ou igual a 0")
  elif p > 1000:
    raise ValueError ("P deve ser menor ou igual a 1000")
  if m < 0:
    raise ValueError ("M deve ser maior ou igual a 0")
  elif m > 1000:
    raise ValueError ("M deve ser menor ou igual a 1000")
  if n > (p + m):
    raise ValueError ("N deve ser menor ou igual à soma de P e M")
  try:
    xi = [int(x) for x in xi.split()]
  except Exception as e:
    print ("Falhou ao converter os valores de Xi para inteiro")
    raise e
  for x in xi:
    if x not in [1, 2]:
      raise ValueError("Os tamanhos solicitados devem ser 1 ou 2")
  return n, xi, p, m

def handle_xi (xi):
  size_dict = {
    1: 0,
    2: 0,
  }
  for x in xi:
    size_dict[x] += 1
  return size_dict

def main ():
  n, xi, p, m = check_inputs(get_inputs())
  xi = handle_xi(xi)
  if ((xi[1] <= p) and (xi[2] <= m)):
    print ("S")
    return
  else:
    print ("N")
    return

if __name__ == '__main__':
  main()