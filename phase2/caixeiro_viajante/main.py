#
# Olimpíada Brasileira de Informática
# Fase 2
# Atividade: Caixeiro Viajante
# Autor: Gabriel Gazola Milan
#
# This one didn't work

from itertools import permutations

def filter_routes (routes):
  filtered = set()
  for route in routes:
    include = True
    for i in range(1, len(route)):
      # All before must be greater
      if (route [i-1] > route[i]):
        for j in range(i):
          if (route[j] < route[i]):
            include = False
            break
      else:
        for j in range(i):
          if (route[j] > route[i]):
            include = False
            break
    if (include):
      filtered.add(route)
  return list(filtered)

def compute_route_cost (route, cost_dict):
  try:
    cost = 0
    for i in range(1, len(route)):
      cost += cost_dict[route[i-1]][route[i]]
    return cost
  except KeyError:
    return float('inf')

def main ():
  N = int(input())
  travel_dict = {}
  for i in range(N):
    travel_dict[i+1] = {}
  for _ in range(int(N*(N-1)/2)):
    A, B, T = [int(i) for i in input().split()]
    travel_dict[A][B] = T
    travel_dict[B][A] = T
  cities = [i + 1 for i in range(N)]
  perm = [subset for subset in permutations(cities, N)]
  print (perm)
  print (filter_routes(perm))
  best_cost = float("inf")
  for route in perm:
    cost = compute_route_cost(route, travel_dict)
    if (cost < best_cost):
      best_cost = cost
  print (best_cost)

if __name__ == '__main__':
  main()

