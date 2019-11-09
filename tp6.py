# -*- coding: utf-8 -*-
"""
@author: Dr Michael GUEDJ

Algorithmique --
TP6 --
Listes
"""


# 1	
def afficher(lst):
    n = len(lst)
    for i in range(n):
        print(lst[i])

# 2	
def afficher_a(lst, a):
    if 0<= a <= len(lst)-1:
        print(lst[a])

# 3	
def afficher_a_b(lst, a, b):
    if 0<= a <= len(lst)-1 \
    and 0<= b <= len(lst)-1 \
    and a<=b:
        i=a
        while i<=b:
            print(lst[i])
            i += 1

# 4	
def concatener(lst):
    n = len(lst)
    res = ""
    for i in range(n):
        res += lst[i]
    return res

# 5	
def appartient(lst, x):
    return x in lst

# 6	
def non_appartient(lst, x):
    return not(appartient(lst, x))

# 7	
def appartient2(lst1, lst2, x):
    return appartient(lst1, x) and appartient(lst2, x)

# 8	
def appartient3(lst1, lst2, x):
    return appartient(lst1, x) and non_appartient(lst2, x)

# 9	
def appartient4(lst1, lst2, lst3, x):
    return appartient(lst1, x) and \
           (appartient(lst2, x) or appartient(lst3, x))


if __name__ == "__main__":

    lst = ["aaa", "bb", "c"]
    lst2 = ["toto", "c", "tata"]
    lst3 = ["1", "bb", "3"]
    
    print("exo 1")
    afficher(lst)

    print("exo 2")
    afficher_a(lst, 1)
    
    print("exo 3")    
    afficher_a_b(lst, 1, 2)
    
    print("exo 4")
    print(concatener(lst))
    
    print("exo 5")
    print(appartient(lst, "c"))
    
    print("exo 6")
    print(non_appartient(lst, "c"))
    
    print("exo 7")
    print(appartient2(lst, lst2, "c"))
    
    print("exo 8")
    print(appartient3(lst, lst2, "bb"))

    print("exo 9")
    print(appartient4(lst, lst2, lst3,  "c"))
