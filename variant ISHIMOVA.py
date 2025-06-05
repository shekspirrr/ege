'''from itertools import*
def f(w,x,y,z):
    return x and (z<=w) and not(y)

for a1,a2,a3,a4,a5,a6,a7 in product([0,1],repeat=7):
    table = [(a1,a2,1,a3),
             (a4,1,0,a5),
             (1,0,a6,a7)]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p,r))) for r in table]==[1,1,1]:
                print(*p)'''



#5
'''def f(n):
    s = ''
    while n!=0:
        s = str(n%3)+s
        n = n // 3
    return s
rez = []
for n in range(1,100):
    b = f(n)
    if n % 3==0:
       b = b + b[-2:]
    else:
        b = b + f((n%3) * 5)
    r = int(b,3)
    if r >= 290:
        rez.append(n)
print(min(rez))
'''

'''#8
from itertools import*
k = 0
for x in product('0123456',repeat=6):
    s = ''.join(x)
    if s[0]!='0' and s.count('3')==1:
        for i in '15':
            s=s.replace(i,'*')
        if '3*' not in s and '*3' not in s:
            k+=1
print(k)'''

'''#12
s = '8'*180

while '2222' in s or '888' in s:
    if '2222' in s:
        s = s.replace('2222','88',1)
    else:
        s = s.replace('888','2',1)
print(s)'''

'''
from ipaddress import*
net = ip_network('143.168.72.213/255.255.255.240',0)
for i in net:
    print(i)
'''
'''#14
def f(n):
    s=''
    while n:
        s = str(n%5)+s
        n //=5
    return s

for x in range(1,2025):
    a = 5**2024-5**1005+25**650+3*5**9-x
    s = f(a)
    if s.count('4')==300:
        print(x)
        break'''

'''#16
from sys import*
setrecursionlimit(100000)
def f(n):
    if n <= 1:
        return 1
    if n>1:
        return n + f(n-3)
print(f(16025)-f(16021))
'''

'''#19
def f(s,m):
    if s<=87:
        return m%2==0
    if m == 0: return 0
    h = [f(s-2,m-1),f(s//2,m-1)]
    return any(h) if (m-1) %2 ==0 else all(h)
print([s for s in range(88,500) if f(s,2)])
print([s for s in range(88,500) if f(s,3) and not f(s,1)])
print([s for s in range(88,500) if f(s,4) and not f(s,2)])'''

'''#23
from sys import*
setrecursionlimit(10000)
def f(x,y):
    if x > y or x == 16:
        return 0
    if x == y:
        return 1
    if x<y:
        return f(x+1,y) + f(x+3,y)+f(x*2,y)
print(f(3,9)*f(9,30))
'''


