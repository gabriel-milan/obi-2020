#
# Olimpíada Brasileira de Informática
# Fase 3
# Atividade: Candidatas
# Autor: Gabriel Gazola Milan
#


def mdc(a, b):
    while b:
        a, b = b, a % b
    return a


def multiMdc(vals):
    if len(vals) == 1:
        return vals[0]
    if len(vals) == 2:
        return mdc(vals[0], vals[1])
    else:
        mMdc = mdc(vals[0], vals[1])
        new_vals = [mMdc]
        new_vals.extend(vals[2:])
        return multiMdc(new_vals)


def typeOneOperation(S, I, V):
    S[I - 1] = V
    return S


def getSubSequences(S):
    output = []
    for start in range(len(S)):
        for end in range(start + 1, len(S) + 1):
            output.append(S[start:end])
    return output


def typeTwoOperation(S, E, D):
    subs = getSubSequences(S[E - 1 : D])
    count = 0
    for sub in subs:
        if multiMdc(sub) > 1:
            count += 1
    return count


def parseOperations(S, ops):
    for op in ops:
        if op[0] == 1:
            S = typeOneOperation(S, op[1], op[2])
        else:
            print(typeTwoOperation(S, op[1], op[2]))


def main():
    try:
        _, M = [int(x) for x in input().split(" ")]
        S = [int(x) for x in input().split(" ")]
        ops = []
        for _ in range(M):
            ops.append([int(x) for x in input().split(" ")])
    except Exception as e:
        raise e
    try:
        parseOperations(S, ops)
    except Exception as e:
        raise e


if __name__ == "__main__":
    main()
