'''from itertools import*
k = 0
for x in product(sorted('АВЛОС'),repeat=4):
    s = ''.join(x)
    k+=1
    #print(k,s)
    if s[0]=='Л':
        print(k,s)
        break'''

'''from itertools import*
k = 0
b = 0
for x in product(sorted('ВЕСНА'),repeat=5):
    s = ''.join(x)
    k+=1
    if s[0]=='Н' and s.count('В')==2 and s.count('Е')<=1 and s.count('С')<=1 and s.count('А')<=1 and s.count('Н')<=1:
        b += 1
print(b)'''

'''from itertools import*
k = 0
for x in product(sorted('МАРИЯ'),repeat=4):
    s = ''.join(x)
    k+=1
    if k==211:
        print(k,s)'''

'''from itertools import*
k = 0
b = 0
for x in product(sorted('ВЕЧНОСТЬ'),repeat=6):
    s = ''.join(x)
    k+=1
    if k%2==0 and s.count('О')>=2 and s[0] not in 'ВЧНСТ':
        b += 1
        print(k,b,s)'''
'''from itertools import*
k = 0

for x in product(sorted('ИЮНЬ'),repeat=5):
    s = ''.join(x)
    k+=1
    if  s.count('И') + s.count('Ю')==2:
        print(k,s)
'''
'''from itertools import*
k = 0
b = 0
for x in product(sorted('МКЦЖЧФ'),repeat=6):
    s = ''.join(x)
    k+=1
    if s.count('Ч')>=2:
        b += 1
print(b)
'''

'''from itertools import*
k = 0
b = 0
for x in product(sorted('ВОСТРГ'),repeat=6):
    s = ''.join(x)
    k+=1
    if s=='СГОВОР':
        b = 1
    if b==1: 
        for i in 'ВСТРГ':
            s=s.replace(i,'*')
        if '**' not in s:
            print(k)
            break'''
'''from itertools import*
k = 0
b = 0
for x in product(sorted('БАТЫР'),repeat=5):
    s = ''.join(x)
    k+=1
    if s.count('Ы')==0 and 'АА' not in s:
        print(k,s)
        break'''
        
'''from itertools import*
k = 0
for x in product('0123456789abc',repeat=7):
    s = ''.join(x)
    if s[0]!='0' and s.count('5')>=2:
        for i in '02468ac':
            s=s.replace(i,'*')
        for i in '13579b':
            s=s.replace(i,'#')
        if '**' not in s and '##' not in s:
            k+=1
print(k)'''

'''from itertools import*
k = 0
for x in permutations('АРТЁМ',r=5):
    s = ''.join(x)
    if not(s[0] in 'АЁ' and s[-1] in 'АЁ'):
        k += 1
print(k)
'''
'''from itertools import*
k = 0
for x in product('ЭТАН',repeat=5):
    s = ''.join(x)
    if s.count('Э') + s.count('А')==1:
        k+=1
print(k)'''


'''from itertools import*
k = 0
for x in permutations('0123456789',r=4):
    s = ''.join(x)
    if s[0]!='0':
           for i in '02468':
                s=s.replace(i,'*')
           for i in '13579':
                s=s.replace(i,'#')
           if '**' not in s and '##' not in s:
                k+=1
print(k)'''

'''from itertools import*
k = 0
for x in product('БАНДЕРОЛЬ',repeat=7):
    s = ''.join(x)
    if s.count('Ь')<=1 and '''