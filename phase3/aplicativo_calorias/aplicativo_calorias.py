#
# Olimpíada Brasileira de Informática
# Fase 3
# Atividade: Aplicativo de calorias
# Autor: Gabriel Gazola Milan
#


def main():
    try:
        E_1 = int(input())
        E_2 = int(input())
        E_3 = int(input())
        X = int(input())
    except Exception as e:
        raise e
    try:
        if (E_2 - E_1) <= X:
            print(E_2)
        else:
            print(E_3)
    except Exception as e:
        raise e


if __name__ == "__main__":
    main()
