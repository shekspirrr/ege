'''from itertools import*
def f(x ,y , w , z):
    return (w or ((not(x)) and (not(y))) or (y == z))

for a1, a2, a3, a4  in product([1 , 0] , repeat=4):
    table = [(a1,0,0,1),(1,a2,1,a3),(1,0,a4,1)]
    if len(set(table)) == len(table):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p , r))) for r in table] == [0,0,0]:
                print(*p)'''
'''#№11
from math import *
k = 1387
c = ceil(log2(k))#SIMVOL
p = ceil(63*c/8)#PAROL # выделено целое число байт
pl = 268464/329
print(pl - p)'''



'''from turtle import*
screensize(2000,2000)
speed(0)
tracer(0)
k=(50)
lt(90)
rt(270)
for _ in range(2):
    fd(10*k)
    rt(90)
    fd(18*k)
    rt(90)
up()
fd(5*k)
rt(90)
fd(7*k)
lt(90)
down()
for _ in range(2):
    fd(10*k)
    rt(90)
    fd(7*k)
    rt(90)
up()
home()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*k,y*k)
        dot()
update()
dot()'''
'''from itertools import*
k = 0
c = "ВИШНЯ"
for a in product(c, repeat=5):
    s = ''.join(a)
    if s[0] != 'Ш' and s[-1]!='И' and s[-1]!='Я' and s.count('В') <= 1:
        k += 1
print(k)'''
    
    

'''def f(n):
    s = ''
    while n > 0:
        s = str(n % 4) + s
        n = n//4
    return s

for n in range(1 , 100):
    b = f(n)
    if n %4 ==0:
        b = b[:-1]
    if n % 4 !=0:
        b = str(n%4) + b + str(n%4)
    r = int(b , 4)
    if r > 313:
        print(n)
        break'''

'''for a in range(1,50000):
    flag = 1
    for x in range(1,500):
        if (((x % 3 == 0) <= (x % 11 != 0)) or (not(a < 80 - x))) == 0:
            flag = 0
            break
    if flag == 1:
        print(a)
        break'''

'''from sys import*
setrecursionlimit(10000)
def f(n):
    if n <= 2740: return n + 7
    if n > 2740: return f(n - 7) + 3*n
print(f(2803)+f(2789))'''

'''def f(s, m):
    if s >= 307:
        return m % 2 ==0
    if m == 0: return 0
    h = [f(s + 2,m - 1), f(s + 5 ,m - 1), f(s * 7 ,m - 1)]
    return any(h) if (m - 1) % 2 == 0 else any(h)
    #return any(h) if (m - 1) % 2 == 0 else any(h)
print([s for s in range(1, 306) if f(s, 2)])
print([s for s in range(1, 306) if f(s, 3) and not f(s, 1)])
print([s for s in range(1, 306) if f(s, 4) and not f(s, 2)])'''

'''from sys import*
setrecursionlimit(100000)
def f(x , y):
    if x < y or x == 29:
        return 0
    if x == y:
        return 1
    if x > y:
        return f(x-5, y) + f(x // 2, y) + (x - 3, y)
print(f(38 , 3)*f(3 , 29))'''

'''#№7
print(9184*1024*8/(16*620*477))
print(2**15)'''

'''#13
from ipaddress import*
for a in (128,192,240,248,252,254,255):
    net = ip_network(f'192.68.120.0/255.255.{a}.0', 0)
    if all(bin(int(ip))[2:].zfill(32)[:16].count('1') <= bin(int(ip))[2:].zfill(32)[16:].count('1') for ip in net):
        print(a)'''
        
#14
'''def p(x):
    while t > 0:
        if t % 9 > 0:
         k += 1
    t //= 9
for n in range(11, 36):
    t = 2 * 229 ** 1333 - 2 * 243 ** n + 81 ** 2335 + 2 * 27 ** 2336 - 2 * 9 ** 2337 - 2024
    k = 0 
    while t > 0:
        if t % 9 > 0:
            k += 1
        t //= 9
    if k % 2 != 0:
        print(n)'''
        
'''s = [int(x) for x in open('6_17.txt')]
maxx = max(s)
k = []
for i in range(len(s)-2):
    if (s[i] % 2 != 0) + (s[i+1] % 2 != 0) + (s[i+2] % 2 != 0) == 1 and\
        (s[i]**2 + s[i+1]**2 + s[i+2]**2) % maxx == 0 :
            k.append(abs(s[i]+s[i+1]+s[i+2]))
print(len(k), min(k))'''
    
s = open('6_24.txt').readline()
print(s[:100])