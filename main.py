import random

def demander_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f" quel est le nombre magique (entre {nb_min} et {nb_max}) ? ")
        try:
            nombre_int = int(nombre_str)
        except:
            print("ERREUR: vous devez rentre un nombre.réessayez.")
        else:
            if nombre_int < nb_min or nombre_int > nb_max :
                print(f"ERREUR: le nombre doit etre entre {nb_min} et {nb_max}. réessayer.")
                nombre_int = 0
    return nombre_int


NOMBRE_MIN = 1
NOMBRE_MAX = 20
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN,NOMBRE_MAX)
NB_VIES = 5

nombre = 0
vies = NB_VIES

while not nombre == NOMBRE_MAGIQUE and vies > 0:
    print(f" il vous reste {vies} vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE: 
        print("bravo, vous avez gagner")
    elif nombre > NOMBRE_MAGIQUE:
        print(" le nombre est plus petit ")
        vies -= 1
    else:
        print("le nombre magique est plus grand")
        vies -= 1

if vies == 0:
    print(f"vous avez perdu! le nombre magique était : {NOMBRE_MAGIQUE} ")