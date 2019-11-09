# -*- coding: utf-8 -*-
"""
@author: Dr Michael GUEDJ

Algorithmique --
TP9 --
Matrices
"""


from numpy import *

#- 2
def afficher(m, l, c):
    for i in range(l):
        for j in range(c):
            print(m[i][j], end="  ")
        print("\n")

print("\n\n  Exo 2")
afficher(ones((4,10)), 4, 10)


#- 3
def exo3(m, l, c):
    for i in range(l):
        for j in range(c):
            if m[i][j] != 1:
                return False
    return True

print("\n\n  Exo 3")
print(exo3(ones((4,10)), 4, 10))
print(exo3(zeros((4,10)), 4, 10))


#- 4
def mult_scal(m, k, l, c):
    res = zeros((l, c))
    for i in range(l):
        for j in range(c):
            res[i][j] = k*m[i][j]
    return res

print("\n\n  Exo 4")
res = mult_scal(ones((4,10)), 3, 4, 10)
afficher(res, 4, 10)


#- 5
def addition(m1, m2, l, c):
    res = zeros((l, c))
    for i in range(l):
        for j in range(c):
            res[i][j] = m1[i][j] + m2[i][j]
    return res

print("\n\n  Exo 5")
res = addition(ones((4,10)), ones((4,10)), 4, 10)
afficher(res, 4, 10)
