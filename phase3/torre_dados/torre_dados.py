#
# Olimpíada Brasileira de Informática
# Fase 3
# Atividade: Torre de dados
# Autor: Gabriel Gazola Milan
#

other_side = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0,
}


def get_free_sides(bottom):
    return [x for x in range(6) if x != bottom and x != other_side[bottom]]


def get_best_side(dice, bottom):
    values = [dice[i] for i in get_free_sides(bottom)]
    return max(values)


def sum_greater_side(dice):
    bestSum = 0
    # Iterate over sides
    for dice_index in range(len(dice)):
        for side in range(6):
            mSum = 0
            top = dice[dice_index][other_side[side]]
            best_side = get_best_side(dice[dice_index], side)
            mSum += best_side
            for top_dice_index in range(len(dice)):
                if top_dice_index == dice_index:
                    continue
                bottom_side = dice[top_dice_index].index(top)
                top = dice[top_dice_index][other_side[bottom_side]]
                best_side = get_best_side(dice[top_dice_index], bottom_side)
                mSum += best_side
            if mSum > bestSum:
                bestSum = mSum
        return bestSum


def main():
    try:
        N = int(input())
        dice = []
        for i in range(N):
            dice.append([int(x) for x in input().split(" ")])
    except Exception as e:
        raise e
    try:
        best_sum = sum_greater_side(dice)
        print(best_sum)
    except Exception as e:
        raise e


if __name__ == "__main__":
    main()
