def Silnia(x):
    wynik = int(1)
    for i in range(1, x + 1):
        wynik = wynik * i
    return wynik


n = int(input("n: "))
p = []
r = 0

# p podajemy rozdzielając liczby tylko przecinkiem
p = input("p: ").split(",")
p = [int(x) for x in p]
p.insert(0, -1)

print(p)

for j in range(1, n + 1):
    pj = p[j]
    r = r + (p[j] - 1) * Silnia(n - j)
    for i in range(j+1, n+1):
        if p[i] > pj:
            p[i] -= 1

print('rank = ', r)
