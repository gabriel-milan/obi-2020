#
# Olimpíada Brasileira de Informática
# Fase 1
# Atividade: Anagrama
# Autor: Gabriel Gazola Milan
#

acceptable_characters = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def get_input ():
  try:
    val = input()
    return val
  except Exception as e:
    print ("Falhou ao pegar input")
    raise e

def handle_inputs (P, A):
  p_dict = {}
  a_dict = {}
  for char in P:
    if char not in acceptable_characters:
      raise ValueError ("Caracter {} não permitido na palavra P!".format(char))
    else:
      if char not in p_dict.keys():
        p_dict[char] = 0
      p_dict[char] += 1
  for char in A:
    if ((char not in acceptable_characters) and (char != '*')):
      raise ValueError ("Caracter {} não permitido na palavra A!".format(char))
    else:
      if char not in a_dict.keys():
        a_dict[char] = 0
      a_dict[char] += 1
  return p_dict, a_dict

def sum_remaining_chars (p_dict):
  p_sum = 0
  for key in p_dict.keys():
    p_sum += p_dict[key]
  return p_sum

def main ():
  p = get_input()
  a = get_input()
  p_dict, a_dict = handle_inputs(p, a)
  for key in a_dict.keys():
    if (key != '*'):
      try:
        p_dict[key] -= a_dict[key]
        if p_dict[key] < 0:
          print ("N")
          return
      except KeyError:
        print ("N")
        return
  if '*' in a_dict.keys():
    if (a_dict['*'] == sum_remaining_chars(p_dict)):
      print ("S")
      return
    else:
      print ("N")
      return
  elif (sum_remaining_chars(p_dict) == 0):
    print ("S")
    return
  else:
    print ("N")
    return
  

if __name__ == '__main__':
  main()