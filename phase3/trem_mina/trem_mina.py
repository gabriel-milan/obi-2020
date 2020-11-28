#
# Olimpíada Brasileira de Informática
# Fase 3
# Atividade: Trem da mina
# Autor: Gabriel Gazola Milan
#

import sys

sys.setrecursionlimit(100000)
from copy import deepcopy

from time import sleep


class Graph:
    def __init__(self, n_nodes):
        self.__nodes = {}
        for i in range(n_nodes):
            self.__nodes[i + 1] = {}

    def add_edge(self, start, end, length):
        self.__nodes[start][end] = length
        self.__nodes[end][start] = length

    @property
    def nodes(self):
        return self.__nodes

    @classmethod
    def _undesired_loops(cls, path):
        path = deepcopy(path)
        if len(path) < 4:
            return False
        path.reverse()
        subs = cls.getSubSequences(path)
        return len(subs) != len(set(subs))

    @classmethod
    def getSubSequences(cls, S):
        S = [str(x) for x in S]
        output = []
        for start in range(len(S)):
            for end in range(start + 2, len(S) + 1):
                output.append("".join(S[start:end]))
        return output

    def get_loop_length(
        self,
        end_node,
        train_length,
        last_node=None,
        remaining_tail=None,
        length=0,
        rem_train_length=None,
        path=None,
        level=0,
    ):
        # sleep(1)
        last_node = last_node or end_node
        remaining_tail = remaining_tail or {}
        path = path or [end_node]
        rem_train_length = rem_train_length or train_length
        # print(
        #     "====== getLoopLength (end_node={}, train_length={}, last_node={}, remaining_tail={}, length={}, path={})".format(
        #         end_node,
        #         train_length,
        #         last_node,
        #         remaining_tail,
        #         length,
        #         path,
        #     )
        # )
        available_neighbors = []
        for neighbor in self.__nodes[last_node]:
            if neighbor not in remaining_tail:
                available_neighbors.append(neighbor)
            elif last_node not in remaining_tail[neighbor]:
                available_neighbors.append(neighbor)
            elif remaining_tail[neighbor][last_node] == 0:
                available_neighbors.append(neighbor)
        # print("-> Available neighbors: {}".format(available_neighbors))
        if self._undesired_loops(path):
            return -1
        elif len(available_neighbors) == 0:
            # print("-> return -1")
            return -1
        elif end_node in available_neighbors:
            # print("-> return end={}".format(length + self.__nodes[end_node][last_node]))
            if (length + self.__nodes[end_node][last_node]) >= train_length:
                return length + self.__nodes[end_node][last_node]
            else:
                return -1
        shortest_path = float("inf")
        for neighbor in available_neighbors:
            # print("Starting with neighbor {}".format(neighbor))
            # Deepcopies
            path2 = deepcopy(path)
            length2 = deepcopy(length) + self.__nodes[neighbor][last_node]
            remaining_tail2 = deepcopy(remaining_tail)
            train_length2 = deepcopy(train_length)
            # Add next node to path
            path2.append(neighbor)
            # print("New path will look like this: {}".format(path2))
            # print(range(len(path2) - 1, 0, -1))
            # Update remaining train tail
            for i in range(len(path2) - 1, 0, -1):
                cur_node = path2[i]
                prev_node = path2[i - 1]
                # print("Updating path {}->{}".format(prev_node, cur_node))
                if cur_node not in remaining_tail2:
                    remaining_tail2[cur_node] = {}
                if prev_node not in remaining_tail2:
                    remaining_tail2[prev_node] = {}
                remaining_tail2[cur_node][prev_node] = min(
                    train_length2, self.__nodes[cur_node][prev_node]
                )
                remaining_tail2[prev_node][cur_node] = remaining_tail2[cur_node][
                    prev_node
                ]
                train_length2 = max(
                    [train_length2 - remaining_tail2[prev_node][cur_node], 0]
                )
                # print("Remaining tail: {}".format(remaining_tail2))
                # print("Remaining length: {}".format(train_length2))
            # Recurse
            path_size = self.get_loop_length(
                end_node,
                train_length,
                last_node=neighbor,
                remaining_tail=remaining_tail2,
                length=length2,
                path=path2,
                rem_train_length=train_length2,
            )
            # print("Path size is {}".format(path_size))
            if path_size == -1:
                # print("Nothing on this way")
                pass
            elif path_size < shortest_path:
                # print("It'lower than current shortest!")
                shortest_path = path_size
        # print("Returning shortest path {}".format(shortest_path))
        return shortest_path if shortest_path != float("inf") else -1


def main():
    try:
        E, R = [int(x) for x in input().split(" ")]
        branches = []
        for _ in range(R):
            branches.append([int(x) for x in input().split(" ")])
        K = int(input())
        trains = []
        for _ in range(K):
            trains.append([int(x) for x in input().split(" ")])
    except Exception as e:
        raise e
    try:
        g = Graph(E)
        for branch in branches:
            g.add_edge(branch[0], branch[1], branch[2])
        for k in trains:
            print(g.get_loop_length(k[0], k[1]))
    except Exception as e:
        raise e


if __name__ == "__main__":
    main()
