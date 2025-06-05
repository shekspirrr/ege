'''a = set(range(10000))
def f(x):
    B = x in {-42, -10, -8, 2,16}
    C = x in {-10, -4, 2, 15, 23}
    A = x in a
    return (A<=B) or C
for x in range(10000):
    if f(x) == 0:
        a.remove(x)
print(sum(a))'''
'''
a = set()
def f(x):
    P = x in {18,20,22,26,27,30}
    Q = x in {20,21,27,30}
    A = x in a
    return (P<=Q) or A
for x in range(10000):
    if f(x)==0:
        a.add(x)
print(len(a))
print(sum(a))'''

from itertools import*
def f(x):
    P=23<=x<45
    Q=34<=x<=56
    A=a1<=x<=a2
    return (not A) or (not P) and Q
#Ox = [i/4 for i in range(20*4,60*4)]
Ox = [i for i in range(20,60)]
n = []
for a1,a2 in combinations (Ox,2):
    if all(f(x)==1 for x in Ox):
        n.append(a2-a1)
print(max(n))