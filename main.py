'''for n in range(1,1000):
  b = bin(n)[2:]
  b=b+str(b.count('1') % 2)
  b=b+str(b.count('1') % 2)
  r = int(b,2)
  if r<253:
      print(n,r)'''
'''rez=[]
for n in range(1,100):
    b = bin(n)[2:]
    if n%2!=0:
        b = '1' + b[:-2]+'10'
    else:
        b = '10' +b[2:] + '1'
    r = int(b,2)
    if n>=33:
        rez.append(r)
print(min(rez))'''

'''rez=[]
for n in range(1,100):
    b = bin(n)[2:]
    if n%2==0:
        b = '10'+b
    else:
        b = '1' + b+'01'
    r = int(b,2)
    if n<=12:
        rez.append(r)
print(max(rez))'''

'''rez=[]
for n in range(1,100):
    b = bin(n)[2:]
    if n % 3==0:
        b = b+b[-2:]
    else:
        b=b+bin(n%3*3)[2:]
    r = int(b,2)
    if r>=195:
        rez.append(r)
print(min(rez))'''


'''for n in range(3,100):
    b = bin(n)[2:]
    if b[-2]!=b[-1]:
       b=b[:-2]+b[-2:][::-1]
       b=b+b[-1]
    else:
        if b[-2:]=='11':
            b=b[:-2]+'101'
        else:
            b=b[:-2]+'010'
    if b[-2]!=b[-1]:
       b=b[:-2]+b[-2:][::-1]
       b=b+b[-1]
    else:
        if b[-2:]=='11':
            b=b[:-2]+'101'
        else:
            b=b[:-2]+'010'
    r = int(b,2)
    if r>168:
        print(n,r)
        break'''


'''for n in range(1,100):
    b = bin(n)[2:]
    if n%3==0:
        b=b+b[-3:]
    else:
        b=b+bin(n%3*3)[2:]
    r=int(b,2)
    if r<76:
        print(n,r)'''

'''def ss(n):
    s=''
    while n!=0:
        s=str(n%3)+s
        n=n//3
    return s
rez=[]
for n in range(1,10000):
    t=ss(n)
    t=sorted(t)[::-1]
    t=''.join(t)
    t=t+t[0]
    r=int(t,3)
    if r<1200:
        rez.append(r)
print(max(rez))'''


'''def ss(n):
    s = ''
    while n!=0:
        if n%12<10:
            s=str(n%12)+s
        if n%12==10:
            s='a'+s
        if n%12==11:
            s='b'+s
        n=n//12
    return s
rez=[]
for n in range(1,1000):
    t=ss(n)
    if n%4==0:
        t='2'+t+'64'
    else:
        t = t+max(t)
    r=int(t,12)
    if r>1799:
        rez.append(r)
print(min(rez))'''


'''def ss(n):
    s = ''
    while n!=0:
        s=str(n%3)+s
        n=n//3
    return s
rez=[]
for n in range(1,100):
    t=ss(n)
    t=t+ss(t.count('2'))
    t=t+ss(t.count('1'))
    t=t+ss(t.count('0'))
    r = int(t,3)
    if r<1000:
        print(n,r)'''

'''def ss(n):
    s = ''
    while n!=0:
        s=str(n%3)+s
        n=n//3
    return s
def d(n):
    s = ''
    for i in n:
        s = s+i*2
    return s
for n in range(1,100):
    t=ss(n)
    if n % 3 == 0:
        t = d(t)
    else:
        t=t.replace('0','*').replace('1','#').replace('2','0').replace('*','1').replace('#','2')
        t = d(t)
    r = int(t,3)
    if r>120:
        print(n,r)
        break'''

'''rez=[]
for n in range(1000,10000):
    b = str(n)
    a = int(b[0])*int(b[1])
    c = int(b[1])*int(b[2])
    d = int(b[2])*int(b[3])
    b = sorted(str(a)+str(d)+str(c))
    b = ''.join(b)
    r = int(b)
    if 1000<r<10000:
        rez.append(r)
print(max(rez))'''
'''    
a = [5 , 2, 3]
b = ''.join(map(str , a))
print(b)

def f(n):
    digits = [int(d) for d in str(n)]
    p1 = digits[0] * digits[1]
    p2 = digits[1] * digits[2]
    p3 = digits[2] * digits[3]
    products = sorted([p1, p2, p3])
    f = ''.join(products)
    result = int(f)
    return result
print(f(10))
rez = []
for n in range(1000 , 10000):
    r = f(n)
    if 999<r<10000:
        rez.append(r)
print(max(rez))'''
    

    