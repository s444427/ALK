nktab = [[0, 0]]
resulttab = [1]


def Stirling2(n, k):
    print(n, k)
    # print(nktab)
    # print(resulttab)

    if [n, k] in nktab:
        print("used nktab")
        return resulttab[nktab.index([n, k])]

    elif n >= 0 and k == n + 1:
        nktab.append([n, k])
        resulttab.append(0)
        print("used n > 0 & k = n+1")
        return int(0)

    elif n >= 1 and k == 0:
        nktab.append([n, k])
        resulttab.append(0)
        print("used n >= 1 & k = 0")
        return int(0)
    else:
        sup2 = int(Stirling2(n - 1, k - 1))
        sup1 = int(Stirling2(n - 1, k))
        result = k * int(sup1) + int(sup2)
        nktab.append([n, k])
        resulttab.append(result)
        return result


if __name__ == '__main__':
    N = int(input('n: '))
    K = int(input('k: '))

    print(Stirling2(N, K))
