#
# Olimpíada Brasileira de Informática
# Fase 2
# Atividade: Fotografia
# Autor: Gabriel Gazola Milan
#

def match_sides (pic_x, pic_y, mold_x, mold_y):
  if (pic_x < pic_y):
    tmp = pic_y
    pic_y = pic_x
    pic_x = tmp
  if (mold_x < mold_y):
    tmp = mold_y
    mold_y = mold_x
    mold_x = tmp
  if ((pic_x <= mold_x) and (pic_y <= mold_y)):
    return True
  return False

def main ():
  try:
    A, L = [int(i) for i in input().split()]
    N = int(input())
    X = []
    Y = []
    for i in range(N):
      x, y = [int(inp) for inp in input().split()]
      X.append(x)
      Y.append(y)
  except Exception as e:
    print ("Falhou ao pegar input")
    raise e
  try:
    theres_one = False
    pic_area = A * L
    mold_areas = []
    for i in range(len(X)):
      area = X[i]*Y[i]
      if (area > pic_area):
        theres_one = True
      mold_areas.append(area)
    if (not theres_one):
      print ("-1")
      return
    best = -1
    best_remaining_area = float("inf")
    for i in range(len(X)):
      if ((mold_areas[i] >= pic_area) and (match_sides(A, L, X[i], Y[i]))):
        remaining_area = mold_areas[i] - pic_area
        if (remaining_area < best_remaining_area):
          best_remaining_area = remaining_area
          best = i + 1
    print (best)
    return
  except Exception as e:
    print ("Falhou!")

if __name__ == '__main__':
  main()