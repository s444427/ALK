def GenerujRGF(n):
    f = []
    F = []
    for i in range(0, n+1):
        f.append(int(0))
    for i in range(0, n+1):
        F.append(int(0))

    for i in range(1, n + 1):
        f[i] = 1
        F[i] = 2
    print(f)
    print(F)


    koniec = False

    while not koniec:
        fin = ''
        for i in range(1, n+1):
            fin = fin + str(f[i]) + ', '
        print(fin)

        j = n

        while f[j] != F[j]:
            j -= 1

        if j > 1:
            f[j] = f[j] + 1
            for i in range(j + 1, n + 1):
                f[i] = 1
                if f[j] == F[j]:
                    F[i] = F[j] + 1
                else:
                    F[i] = F[j]
        else:
            koniec = True
    return 0


if __name__ == "__main__":
    n = int(input("n: "))
    GenerujRGF(n)
