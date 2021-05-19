def Sprzężenie(n, tab):
    sub = []
    for i in range(0, tab[0]):
        sub.append(1)

    for i in range(1, len(tab)):
        print(i, tab[i], tab, sub)
        for j in range(0, tab[i]):
            sub[j] += 1

    print("podział sprzężony: ", sub)


if __name__ == "__main__":
    n = int(input("n: "))
    tab = input("podział: ").split(',')
    tab = [int(x) for x in tab]
    Sprzężenie(n, tab)
