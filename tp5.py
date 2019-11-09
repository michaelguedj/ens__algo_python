# -*- coding: utf-8 -*-
"""
@author: Dr Michael GUEDJ

Algorithmique --
TP5 --
Boucles "Tant que"
"""


import random

# 1
def dix():
    i=0
    while i<10:
        print(i)
        i += 1
        
# 2
def n_premiers_entiers(n):
    i=0
    while i<n:
        print(i)
        i += 1
        
# 3
def n_premiers_entiers_carre(n):
    i=0
    while i<n:
        print(i*i)
        i += 1
        
# 4
def n_premiers_entiers_pairs(n):
    i=0
    while i<n:
        if i%2 == 0:
            print(i)
        i += 1
        
# 5
def n_premiers_entiers_impairs(n):
    i=0
    while i<n:
        if i%2==1:
            print(i)
        i += 1
          
# 6
def _10_fois_coucou():
    i=0
    while i<10:
        print("coucou")
        i += 1
        
# 7
def n_fois_coucou(n):
    i=0
    while i<n:
        print("coucou")
        i += 1
        
# 8
def somme_n_premiers_entiers(n):
    res=0
    i=0
    while i<n:
        res += i
        i += 1
    return res

# 9
def somme_n_premiers_carres(n):
    res=0
    i=0
    while i<n:
        res += i*i
        i += 1
    return res

# 10
def somme_n_premiers_pairs(n):
    res=0
    i=0
    while i<n:
        if i%2==0:
            res += i
        i += 1
    return res

# 11
def somme_n_premiers_impairs(n):
    res=0
    i=0
    while i<n:
        if i%2==1:
            res += i
        i += 1
    return res

# 12
def somme_n_premiers_pairs_carre(n):
    res=0
    i = 0
    while i<n:
        if i%2==0:
            res += i*i
        i += 1
    return res

# 13
def toto(n):
    res=0
    i=0
    while i<n:
        if i%3 == 0:
            res += i
        i += 1
    return res

# 14
def toto2(n, k):
    res=0
    i=0
    while i<n:
        if i%k == 0:
            res += i
        i += 1
    return res

# 15
def toto_bis(n):
    return toto2(n,3)

# 16
def toto3():
    res=0
    i=1
    while i <= 100:
        res += i
        i += 1
    return res

# 17
def toto4(a, b):
    res=0
    i=a
    while i <= b:
        res += i
        i += 1
    return res

# 18
def toto3_bis():
    return toto4(1, 100)

# 19
'''
entree = input("Entrée : ")
while entree != "q":
    print(entree)
    entree = input("Entrée : ")
print("Au revoir !")
'''

# 20
'''
nombre = random.randint(1,100)
# generate random integer numbers
# between 1 and 100 (inclusive)

essai = int(input("Entrez un nombre entre 1 et 100 : "))

while essai != nombre:
    if essai < 1 or essai > 100:
        print("Usage : le nombre doit être compris entre 1 et 100 !")
    elif essai < nombre:
        print("Trop petit !")
    elif essai > nombre:
        print("Trop grand !")
    essai = int(input("Entrez un nombre entre 1 et 100 : "))
print("Trouvé !")
'''


if __name__ == "__main__":
    
    print("exo 1:")
    dix()
    
    print("exo 2:")
    n_premiers_entiers(5)
    
    print("exo 3:")
    n_premiers_entiers_carre(5)
    
    print("exo 4:")
    n_premiers_entiers_pairs(10)
    
    print("exo 5:")
    n_premiers_entiers_impairs(10)
    
    print("exo 6:")
    _10_fois_coucou()
    
    print("exo 7:")
    n_fois_coucou(5)
    
    print("exo 8:", somme_n_premiers_entiers(5))    # 10
    
    print("exo 9:",  somme_n_premiers_carres(5))    # 30
    
    print("exo 10:",  somme_n_premiers_pairs(10))   # 20
    
    print("exo 11:",  somme_n_premiers_impairs(10)) # 25
    
    print("exo 12:",  somme_n_premiers_pairs_carre(5)) # 20
    
    print("exo 13:", toto(10))  # 18
    
    print("exo 14:", toto2(10, 3))  # 18
    
    print("exo 15:", toto_bis(10) == toto(10))  # True
    
    print("exo 16:", toto3())   # 5050
    
    print("exo 17:", toto4(2, 5))   # 14
    
    print("exo 18:", toto3_bis()  == toto3())   # True
