# -*- coding: utf-8 -*-
"""
@author: Dr Michael GUEDJ

Algorithmique --
TP1 --
Fonctions et appels de fonctions
"""


# 1
def f(x):
    return x+1

# 2
def g(x):
    return 2*x+3

# 3
def h(x):
    return x*x+1

# 4
def i(x):
    return 5*x**2+3*x+1

# 5
def j(x):
    return 3*x**3+5*x**2+3*x+4

# 6
def k(x):
    return x**10-x**3+3

# 7
def l(x):
    return 3*x**10+4*x**2+5

# 8
def m(x):
    return 10*x**15+3*x+1

# 9
def a(x):
    return x+3

def  b(x):
    return x**2-2

def n(x):
    return a(x)+b(x)

# 10
def c(x):
    return x+1

def d(x):
    return x**3

def p(x):
    return c(d(x))

# 11
def q(x):
    return (3*x**3+2)/(20*x**2+1)


if __name__ == "__main__":
    
    print("exo 1:", f(3))   # 4
    print("exo 2:", g(2))   # 7
    print("exo 3:", h(3))   # 10
    print("exo 4:", i(3))   # 55
    print("exo 5:", j(2))   # 54
    print("exo 6:", k(2))   # 1019
    print("exo 7:", l(2))   # 3093
    print("exo 8:", m(2))   # 327687
    print("exo 9:", n(2))   # 7
    print("exo 10:", p(2))   # 9
    print("exo 11:", q(2))   # 0.32098765432098764

