#
# Olimpíada Brasileira de Informática
# Fase 2
# Atividade: Estrada
# Autor: Gabriel Gazola Milan
#

def main ():
  try:
    T = int(input())
    N = int(input())
    cities_loc = []
    for i in range(N):
      cities_loc.append(int(input()))
  except Exception as e:
    print ("Falhou ao pegar input")
    raise e
  try:
    cities_loc = sorted(cities_loc)
    borders = []
    for i in range(N):
      if (i == 0):
        borders.append(cities_loc[i] + (cities_loc[i+1] - cities_loc[i]) / 2)
      elif (i == N-1):
        borders.append((cities_loc[i] - cities_loc[i-1])/2 + T - cities_loc[i])
      else:
        borders.append((cities_loc[i] - cities_loc[i-1]) / 2 + (cities_loc[i+1] - cities_loc[i]) / 2)
    borders = sorted(borders)
    print ("{:.2f}".format(borders[0]))
  except Exception as e:
    raise e

if __name__ == '__main__':
  main()