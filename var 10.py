'''from itertools import*
def f(w,x,y,z):
    return (((y <= (not(x))) and y) == w) and z

for a1,a2,a3,a4,a5 in product([1,0], repeat=5):
    table = [(1,a1,0,a2),(a3,1,0,0),(a4,0,0,a5)]
    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, r))) for r in table] == [1,1,1]:
                print(*p)'''

#5
'''def tr(x):
    s = ''
    while x>0:
        s = str(x%3)+s
        x = x // 3
    return s
rez = []
for n in range(1,1000):
    b = tr(n)
    if n % 3 == 0:
        b = b[-2:]+b
    else:
        sm = b.count('1')*1+b.count('2')*2
        b = tr(sm)+b
    r = int(b,3)
    if r>418 and r%2!=0:
        rez.append(r)
print(min(rez))'''
      
#8
'''from itertools import*
k = 0
a = 0
b = 0
for i in product(sorted('ЧМСЕИАК'), repeat=5):
    s = ''.join(i)
    k += 1
    if 'МАСИК' in s:
        a = k
    if 'ЧЕЧИК' in s:
        b = k
print(b -a - 1)'''


'''#12
s = '4' * 222
k = 0
while '4444' in s or '222' in s:
    if '4444' in s:
        s = s.replace('4444','2',1)
    else:
        s = s.replace('222','44',1)
    k+=1
print(k)'''

#11
'''from math import*
sim = ceil(log2(26+10))'''

#13
'''
В терминологии сетей TCP/IP маска сети – это двоичное число, меньше
2**32в маске сначала (в старших разрядах) стоят единицы, а затем с некоторого мест
нули. Маска определяет, какая часть IP-адреса узла сети относится к адресу сети, 
какая – к адресу самого узла в этой сети. Обычно маска записывается по тем ж
правилам, что и IP-адрес – в виде четырёх байт, причём каждый байт записывается
виде десятичного числа. Адрес сети получается в результате применения поразрядно
конъюнкции к заданному IP-адресу узла и маске.
Для узла c IP-адресом 221.142.14.0 адрес подсети равен 221.142.0.0. Скольк
существует различных возможных значений маски сети, если известно, что в этой сет
не менее 8000 узлов? Ответ запишите в виде десятичного числа.
from ipaddress import*

for mask in range(33):
    net = ip_network(f'221.142.14.0/{mask}',0)
    if net.num_addresses >= 8000:
        print(net)'''
 
#14
#16
from functools import*
@lru_cache(None)
def f(n):
    if n<222: return 111
    if n>= 222: return 2*(n+4)+f(n-3)
for n in range(0,55556):
    f(n)
print(f(55555)-f(55543))

 
 
 
 
 
 
    
    