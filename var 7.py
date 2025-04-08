'''from turtle import*
screensize(2000,2000)
speed(0)
tracer(0)
k=15
left(90)
rt(180)
for _ in range(3):
    rt(45)
    fd(11*k)
    rt(45)
rt(315)
fd(11*k)
rt(90)
fd(22*k)
for _ in range(2):
    rt(90)
    fd(11*k)
up()
home()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*k,y*k)
        dot()
update()
dot()'''

#23
def f(x,y,s):
    if x>y or 'BBB' in s: return 0
    if x == y: return 1
    if x<y: return f(x+1,y,s+'A')+f(x+3,y,s+'B')+f(x*2,y,s+'C')
print(f(2,20,''))