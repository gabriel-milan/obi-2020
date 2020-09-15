#
# Olimpíada Brasileira de Informática
# Fase 1
# Atividade: Música para todos
# Autor: Gabriel Gazola Milan
#

def get_checked_inputs ():
  try:
    n, m, c = [int(x) for x in input().split()]
  except Exception as e:
    print ("Erro ao pegar N, M e C")
    raise e
  if n < 1:
    raise ValueError ("N deve ser inteiro maior ou igual a 1")
  elif n > 10e5:
    raise ValueError ("N deve ser inteiro menor ou igual a 10^5")
  if m < 1:
    raise ValueError ("M deve ser inteiro maior ou igual a 1")
  elif m > 10e5:
    raise ValueError ("M deve ser inteiro menor ou igual a 10^5")
  if c < 1:
    raise ValueError ("C deve ser inteiro maior ou igual a 1")
  if c > m:
    raise ValueError ("C deve ser inteiro menor ou igual a M={}".format(m))
  love_hate = []
  for i in range(n):
    try:
      a, d = [int(x) for x in input().split()]
    except Exception as e:
      print ("Erro ao pegar A e D #{}".format(i+1))
      raise e
    if (a == d):
      raise ValueError ("A deve ser diferente de D")
    love_hate.append((a, d))
  return n, m, c, love_hate

def generate_graph (love_hate):
  graph = {}
  for a, d in love_hate:
    if d not in graph.keys():
      graph[d] = a
  return graph

def main():
  n, m, c, love_hate = get_checked_inputs()
  graph = generate_graph(love_hate)
  keep_track = []
  iterate = True
  changes = 0
  while (iterate):
    if c in graph.keys():
      if c in keep_track:
        print ("-1")
        return
      keep_track.append(c)
      c = graph[c]
      changes += 1
    else:
      iterate = False
  print (changes)
  return

if __name__ == '__main__':
  main()