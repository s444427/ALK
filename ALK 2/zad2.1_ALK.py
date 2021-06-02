binarylist = []
sublist = []
n = 0
a = []

# Input manager
n = int(input("Podaj n: "))
a = input("Podaj zawartość podzbioru: [ ")
print("]")

sublist = a.split(", ")

# Create base binary
for j in range(0, n):
    binarylist.append(0)

if sublist != [""]:
    for i in sublist:
        binarylist[int(i) - 1] = 1


endbinary = ""
for z in binarylist:
    endbinary += str(z)

enddecimal = int(endbinary, 2)

print("Podzbiór znajduje się na pozycji " + str(enddecimal) + ".")
