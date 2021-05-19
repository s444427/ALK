def Silnia(x):
    wynik = int(1)
    for i in range(1, x + 1):
        wynik = wynik * i
    return wynik


def countD(r, j):
    d = 0
    d = (r % Silnia(j + 1)) / Silnia(j)
    return d


n = int(input("n: "))
r = int(input('r: '))
p = []
for i in range(0, n + 1):
    p.append(int(0))
p[n] = 1
print('start p: ', p)

p[n] = 1
for j in range(1, n):
    d = countD(r, j)
    r = r - d * Silnia(j)
    p[n - j] = int(d + 1)

    for i in range(n - j + 1, n + 1):
        if p[i] >= d + 1:
            p[i] += 1
    print('p: ', p, 'd: ', d, 'r: ', r)

print('final p: ', p)
