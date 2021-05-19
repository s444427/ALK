if __name__ == "__main__":

    y = input("Podaj kod prufera rozdzielony przecinkami: ").split(',')
    L = [int(x) for x in y]
    n = len(L) + 2

    for i in range(0, n-2):
        L[i] -= 1

    power = int(len(L)-1)

    rank = 0
    for i in range(0, len(L)):
        rank += L[i] * (n ** (power - i))

    print(rank)
