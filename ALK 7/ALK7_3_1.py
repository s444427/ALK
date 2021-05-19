def PermNast(n, pi):
    pi[0] = 0
    i = n-1
    while pi[i+1] < pi[i]:
        i -= 1
    if i == 0:
        return "nieokreślony"
    j=n
    while pi[j] < pi[i]:
        j -= 1
    pi[i], pi[j] = pi[j], pi[i]
    for h in range(i+1, n+1):
        ro[h] = pi[h]
        for h in range(i+1, n+1):
            pi[h] = ro[n+i+1-h]
    return pi