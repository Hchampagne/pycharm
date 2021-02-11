import random

nombre = random.randint(0, 100)
print(nombre)

while True:
    choix = input("choisit un nombre entre 0 et 100 :")
    try:
        choix = int(choix)
    except:
        print("Entre 0 et 100, faut lire un peu !")
        pass
    else:
        if 0 < choix < 100:

            if nombre == choix:
                print("GOOD JOB !")
                break
            if nombre < choix:
                print("Trop grand ! ")
            if nombre > choix :
                print("Top petit ! ")
        else:
            print("ENTRE 0 et 100 ! ")