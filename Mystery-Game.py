import sys
import random

mystery_number = random.randint(0, 100)
try_number = 5
user_try = ""
increment = 0
#print(f"Le nombre mystère est {mystery_number}")

print("⭐ Le jeu du nombre mystère ⭐")
#Boucle principale
while try_number > 0:
    #Définir le nombre d'essais qu'il reste à l'utilisateur
    if try_number == 1:
        print(f"Il te reste {try_number} essai")
    else:
        print(f"Il te reste {try_number} essais")

    #Demander à l'utilisateur de rentrer un nombre et par la même occasion vérifier si c'est bien un nombre
    user_try = input("Devines le nombre : ")
    if not user_try.isdigit():
        print("Veuillez rentrer un nombre valide.")
    else:
        try_number -= 1
        increment += 1
        user_try = int(user_try)
        if increment <= 5:
            #Le cas dans lequel le nombre mystère est trouvé
            if user_try == mystery_number:
                if increment == 1:
                    print(f"Bravo ! Le nombre mystère était bien {mystery_number} !\nTu as trouvé le nombre mystère en {increment} essai\nFin du jeu.")
                    sys.exit()
                else:
                    print(f"Bravo ! Le nombre mystère était bien {mystery_number} !\nTu as trouvé le nombre mystère en {increment} essais\nFin du jeu.")
                    sys.exit()
            #Le cas dans lequel le nombre mystère est plus petit que ce que l'utilisateur a noté
            elif mystery_number < user_try:
                print(f"Le nombre mystère est plus petit que {user_try}")
            #Le cas dans lequel le nombre mystère est plus grand que ce que l'utilisateur a noté
            else:
                print(f"Le nombre mystère est plus grand que {user_try}")
        else:
            print(f"Dommage ! Le nombre mystère était : {mystery_number}")

print("Fin du jeu.")