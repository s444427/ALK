if __name__ == "__main__":
    n = int(input("n: "))
    r = int(input("r: "))
    r2 = r // 2
    x = []
    x2 = []

    while r > 0:
        x.append(r % 2)
        r //= 2
    x.reverse()

    while r2 > 0:
        x2.append(r2 % 2)
        r2 //= 2
    x2.reverse()

    while len(x2) < len(x):
        x2.insert(0, 0)

    for i in range(0, len(x)):
        x[i] = (x[i] + x2[i]) % 2

    for i in range(0, len(x)):
        x[i] = (x[i])*(i+1)

    x = [p for p in x if p != 0]
    print(x)

