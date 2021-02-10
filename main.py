import sys
nb1 = input("Saisissez un premier nombre: ")
try:
    nb1 = int(nb1)
except:
    print("La conversion de ce nombre s’est mal passée", file=sys.stderr)
    sys.exit()
try:
    nb2 = int(input("Saisissez un deuxième nombre: "))
except:
    print("La conversion de ce nombre s’est mal passée", file=sys.stderr)
    sys.exit()

if nb1 < nb2:
    print("<")
elif nb1 > nb2:
    print(">")
else:
    print("=")
