#
# Olimpíada Brasileira de Informática
# Fase 2
# Atividade: Dona Formiga
# Autor: Gabriel Gazola Milan
#

class Node ():

  def __init__ (self, height: int, id: int):
    self.__height = height
    self.__nodes = []
    self.__id = id

  def __str__ (self):
    return self.__repr__()

  def __repr__ (self):
    return "<Node (id={}, n_nodes={}, ids={})>".format(self.id, self.n_nodes, self.ids)

  @property
  def height (self):
    return self.__height

  @property
  def nodes (self):
    return self.__nodes

  @property
  def id (self):
    return self.__id
  
  @property
  def n_nodes (self):
    return len(self.__nodes)

  @property
  def ids (self):
    ids = [self.id]
    for node in self.nodes:
      ids.append(node.id)
    return ids

  def addNode (self, node):
    if node.height > self.height:
      node.addNode(self)
    elif node.height < self.height:
      self.__nodes.append(node)
    else:
      pass

  def getLargestNumberOfLeaves (self):
    ids = []
    for node in self.nodes:
      ids.extend([node_id for node_id in node.ids if node_id not in ids])
    return len(ids)

def main ():
  try:
    nodes = []
    # Getting S, T and P
    inputs = [i for i in input().split()]
    if len(inputs) != 3:
      raise ValueError("Wrong input")
    S, T, P = [int(i) for i in inputs]
    if ((S < 1) or (S > 200)):
      raise ValueError("1 <= S <= 200")
    if ((T < 1) or (T > (S*(S-1)/2))):
      raise ValueError("T <= S <= S*(S-1)/2")
    if ((P < 1) or (P > S)):
      raise ValueError("1 <= P <= S")
    # Getting Ai
    A = [int(i) for i in input().split()]
    if (len(A) != S):
      raise ValueError("len(A) must match S")
    for a in A:
      if ((a < -1000) or (a > 1000)):
        raise ValueError("-1000 <= Ai <= 1000")
    # Generating S nodes with Ai heights
    for i in range(S):
      nodes.append(Node(A[i], i+1))
    # Getting relationships
    for i in range(T):
      rel = [int(n_id) for n_id in input().split()]
      if (len(rel) != 2):
        raise ValueError("Relationships must be between two rooms only")
      for n_id in rel:
        if ((n_id < 1) or (n_id > S)):
          raise ValueError("Room {} doesn't exist".format(n_id))
      nodes[rel[0]-1].addNode(nodes[rel[1]-1])
    # Return
    print (nodes[P-1].getLargestNumberOfLeaves())
  except Exception as e:
    print ("Falhou!")
    raise e

if __name__ == '__main__':
  main()