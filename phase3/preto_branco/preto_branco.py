#
# Olimpíada Brasileira de Informática
# Fase 3
# Atividade: Jogo do Preto e Branco
# Autor: Gabriel Gazola Milan
#

EMPTY = 0
BLACK = 1
WHITE = 2


class Board:
    def __init__(self, rows, cols):
        self.__rows = rows - 1
        self.__cols = cols - 1
        self.__board = []
        for i in range(rows):
            self.__board.append([])
            for _ in range(cols):
                self.__board[i].append(EMPTY)

    def __repr__(self):
        ret = ""
        for row in self.__board:
            ret += row.__repr__() + "\n"
        return ret

    def __str__(self):
        return self.__repr__()

    def fillBlacks(self, blacks):
        for black in blacks:
            i, j = black[0] - 1, black[1] - 1
            self.__board[i][j] = BLACK

    def getNeighborsCoordinates(self, x, y, raw=True):
        output = []
        if raw:
            x -= 1
            y -= 1
        neighbors = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        for neighbor in neighbors:
            new_x = x + neighbor[0]
            new_y = y + neighbor[1]
            if (
                (new_x >= 0)
                and (new_x <= self.__rows)
                and (new_y >= 0)
                and (new_y <= self.__cols)
            ):
                output.append([new_x, new_y])
        return output

    def hasBlackNeighbor(self, x, y, raw=True):
        if raw:
            x -= 1
            y -= 1
        for neighbor_coordinate in self.getNeighborsCoordinates(x, y, False):
            if self.__board[neighbor_coordinate[0]][neighbor_coordinate[1]] == BLACK:
                return True
        return False

    def hasWhiteNeighbor(self, x, y, raw=True):
        if raw:
            x -= 1
            y -= 1
        for neighbor_coordinate in self.getNeighborsCoordinates(x, y, False):
            if self.__board[neighbor_coordinate[0]][neighbor_coordinate[1]] == WHITE:
                return True
        return False

    def coordinateEmpty(self, x, y, raw=True):
        if raw:
            x -= 1
            y -= 1
        return self.__board[x][y] == EMPTY

    def setWhite(self, x, y, raw=True):
        if raw:
            x -= 1
            y -= 1
        self.__board[x][y] = WHITE


def rotate_list(mList):
    mList.insert(0, mList.pop())


def main():
    try:
        L, C = [int(x) for x in input().split(" ")]
        P = int(input())
        blacks = []
        for _ in range(P):
            blacks.append([int(x) for x in input().split(" ")])
    except Exception as e:
        raise e
    try:
        best_count = 0
        try_these = list(range(L * C))
        for _ in range(len(try_these)):
            rotate_list(try_these)
            count = 0
            board = Board(L, C)
            board.fillBlacks(blacks)
            for cell in try_these:
                i = cell // C
                j = cell % C
                if (
                    board.coordinateEmpty(i, j, raw=False)
                    and board.hasBlackNeighbor(i, j, raw=False)
                    and not board.hasWhiteNeighbor(i, j, raw=False)
                ):
                    board.setWhite(i, j, raw=False)
                    count += 1
            if count > best_count:
                best_count = count
        print(best_count)
    except Exception as e:
        raise e


if __name__ == "__main__":
    main()
