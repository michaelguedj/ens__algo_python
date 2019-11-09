# -*- coding: utf-8 -*-
"""
@author: Dr Michael GUEDJ

Algorithmique --
TP3 --
Procédures
"""


# 1
def afficher_arguments(a, b, c):
    print(a, b, c)

# 2
def etes_vous_toto():
    nom = input("votre nom : ")
    if nom == "Toto":
        print("Vous êtes Toto")
    else:
        print("Vous n'êtes pas Toto")

# 3
def etes_vous_toto2():
    nom = input("votre nom : ")
    if nom == "Toto" or nom == "toto":
        print("Vous êtes Toto")
    else:
        print("Vous n'êtes pas Toto")

# 4
def etes_vous_untel(untel):
    nom = input("votre nom : ")
    if nom == untel:
        print("Vous êtes", untel)
    else:
        print("Vous n'êtes pas", untel)

# 5
def qui_etes_vous():
    nom = input("votre nom : ")
    prenom = input("votre prénom : ")
    age = input("votre âge : ")
    print("Vous êtes", prenom, nom, "et vous avez", age, "ans.")

# 6
def qui_est_plus_grand(x, y):
    if x < y:
        print(y, "est plus grand que", x)
    elif x > y:
        print(x, "est plus grand que", y)
    else:
        print(x, "et", y, "sont égaux")

# 7
def quelle_heure():
    h = int(input("Entrer une heure : "))
    if h < 0 or h >= 24:
        print("Je vous demande pardon ?")
    elif 0 <= h < 5:
        print("Il faut dormir !")
    elif 5 <= h < 12:
        print("Bon matin !")
    elif 12 <= h < 14:
        print("Bon appétit !")
    elif 14 <= h < 18:
        print("Bon après-midi !")
    elif 18 <= h < 21:
        print("Bon soir !")
    elif 21 <= h < 24:
        print("Bonne nuit !")

# 8
def calculette():
    n1 = int(input("Nombre :"))
    op = input("Opérateur :")
    n2 = int(input("Nombre :"))
    if op == "+":
        print("=", n1+n2)
    elif op == "-":
        print("=", n1-n2)
    elif op == "*":
        print("=", n1*n2)  
    elif op == "/":
        print("=", n1/n2)    
    else:
        print("Opérateur non pris en compte !")
        

if __name__ == "__main__":
    
    # exo 1
    afficher_arguments(1, "toto", 3.5)

    # exo 6
    qui_est_plus_grand(2, 100)

