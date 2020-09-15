#
# Olimpíada Brasileira de Informática
# Fase 1
# Atividade: Irmãos
# Autor: Gabriel Gazola Milan
#

def get_input ():
  try:
    val = int(input())
    return val
  except Exception as e:
    print ("Falhou ao pegar input")
    raise e

def run ():
  n = get_input()
  m = get_input()
  if n < 1:
    raise ValueError ("N deve ser maior ou igual a 1")
  elif n > 40:
    raise ValueError ("N deve ser menor ou igual a 40")
  if m < n:
    raise ValueError ("M deve ser maior ou igual a N")
  elif m > 40:
    raise ValueError ("M deve ser menor ou igual a 40")
  diff = m - n
  print (m + diff)
  return

if __name__ == '__main__':
  run()
