# -*- coding: utf-8 -*-
"""
@author: Dr Michael GUEDJ

Algorithmique --
TP2 --
Conditions
"""


# 1
def f(x):
    if x < 0:
        return 0
    else:
        return 1

# 2
def g(x):
    if x <= 0:
        return "toto"
    else:
        return "tata"

# 3
def h(c):
    if c == 'a':
        return 0
    if c == 'b':
        return 1
    if c == 'c':
        return 2
    else:
        return 3

# 4
def i(x):
    if x <= 0:
        return 0
    elif 0 <= x <= 100:
        return 1
    return 2

# 5
def j(x):
    if -10 < x < 10:
        return x*x
    elif 50 < x < 60:
        return x**3
    return 1

# 6
def k(x):
    if x == 1:
        return 'a'
    if x == 2:
        return 'b'
    if x == 3:
        return 'c'
    return '_'

# 7
def l(w):
    if w == "toto":
        return 1
    if w == "toutou":
        return 2
    return 0

# 8
def m(c):
    if c == 'h':
        return "haut"
    if c == 'b':
        return "bas"
    if c == 'd':
        return "droite"
    if c == 'g':
        return "gauche"
    return "autre"

# 9
def n(x, y):
    if x == y:
        return 1
    return 0

# 10
def p(a, b):
    if a == b:
        return True
    return False

def p_bis(a, b):
    return a == b

# 11
def q(x, y, z):
    if x == y == z:
        return True
    return False

def q_bis(x, y, z):
    return x == y == z

# 12
def r(x, y, z):
    if x > y and  x > z:
        return 1
    if y > x and y > z:
        return 2
    if z > x and z > y:
        return 3
    return 0

# 13
def s(x, y, z):
    if x != 0:
        return (1+y+z)/x
    if y != 0:
        return (2+x+z)/y
    if z != 0:
        return (3+x+y)/z
    return 0

# 14
def t(x, y, z):
    if x != 0:
        return x**4+(1+y**3+z**5)/x
    if y != 0:
        return y**4+(2+x**3+z**5)/y
    if z != 0:
        return z**4+(3+x**3+y**5)/z
    return 0


if __name__ == "__main__":
    
    print("exo 1:", f(3))   # 1
    print("exo 2:", g(2))   # tata 
    print("exo 3:", h('b'))   # 1
    print("exo 4:", i(100))   # 1
    print("exo 5:", j(55))   # 166375
    print("exo 6:", k(2))   # b
    print("exo 7:", l("toto"))   # 1 
    print("exo 8:", m('b'))   # bas
    print("exo 9:", n(2, 3))   # 0
    print("exo 10:", p(2, 3))   # False
    print("exo 10:", p_bis(2, 2))   # True
    print("exo 11:", q(2, 2, 2))   # True
    print("exo 11:", q_bis(2, 1, 1))   # False
    print("exo 12:", r(2, 1, 1))   # 1
    print("exo 13:", s(0, 0, 3))   # 1.0
    print("exo 14:", t(0, 0, 2))   # 33.5
