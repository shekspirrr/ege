'''s = open('k8-31.txt').readline()
print(s[:100])
m=[0]*len(s)
#print(m)
for i in range(len(s)):
    if s[i] in 'ABEF':
        m[i] = m[i-1]+1
print(max(m))'''

'''s = open('k7a-3.txt').readline()
c = 0
m = 0
for i in range(len(s)):
    if s[i] in 'ABEF':
        c += 1 
        m = max(m, c)
    else:
        c = 0
print(m)'''

'''s = open('k8-4.txt').readline()
m = [1]*len(s)
for i in range(len(s)):
    if s[i]!= s[i-1]:
        m[i] = m[i-1]+1
print(max(m))'''

'''s = open('k8-31.txt').readline()
m = [1]*len(s)
for i in range(len(s)):
    if s[i] == s[i-1]:
        m [i] == m [i-1]+1
        if m [i] == 9:
            print(s[i],m[i])
print(max(m))'''


'''s = open('24-157.txt').readline()
m = [2]*len(s)
for i in range(len(s)):
    if s[i-2] + s[i-1] + s[i] != 'PPP':
        m[i] = m[i-1]+1
print(max(m))'''

'''s = open('24-196.txt').readline()
m = [0]*len(s)
for i in range(len(s)):
    if s [i-1] + s [i] == 'ZX' or s[i-1] + s[i] == 'ZY':
        m [i] = m[i-2] + 1
print(max(m))'''

'''s = open('24-204.txt').readline()
m  = [0] *len(s)
for i in range(len(s)):
    if s[i-1] + s[i] == 'AA' or s[i-1]   + s[i] == 'CC':
        m[i] = m[i-2] + 1
print(max(m))'''


'''s = open('24-181.txt').readline()
l = 0
m = 0
k = 0
for r in range(len(s)):
    if s[r] == '.':
        k += 1
    while k > 1:
        if s[l] == '.':
            k -= 1
        l += 1
    m = max(m, r-l+1)
print(m)'''

'''s = open('24-280.txt').readline()
l = 0
m = 0
kx = ky =0
for r in range(len(s)):
    if s[r] == 'X':
        kx += 1
    if s[r] == 'Y':
        ky += 1
    while kx > 1 or ky > 1:
        if s[l] == 'X':
            kx -= 1
        if s[l] == 'Y':
            ky -= 1
        l += 1
    if kx == 1 and ky == 1:
        m = max(m, r-l + 1)
print(m)'''

'''s = open('24-263.txt').readline()
l = 0
m = 0
ky = 0
for r in range(len(s)):
    if s[r] == 'Y':
        ky +=1
    while ky > 150:
        if s[l] == 'Y':
            ky -= 1
        l += 1
    m = max(m, r-l+1)
print(m)'''

'''s = open('24-263.txt').readline()
print(s)'''



#21
#регулярное выражение
'''from re import*
s = open('k7a-1.txt').readline()
finditer
r = r'[ABC]+'
#print(s[:100])
print(max([len(x.group()) for x in finditer(r, s)]))'''


'''from re import*
s = open('24-196.txt').readline()
r = r'(ZX|ZY)+'
print(max([len(x.group())//2 for x in finditer(r,s)]))'''

#212
'''from re import*
s = open('24-212.txt').readline()
r = r'([BCD][AO])+'
print(max([len(x.group())//2 for x in finditer(r,s)]))'''

#204
from re import*
s = open('24-204.txt').readline()
reg = r'(AA|CC)+'
rk = rf'(?=({reg}))'
print([(x.group()) for x in finditer(reg,s)])






