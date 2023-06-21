import turtle
import random
screen=turtle.Screen()
screen.bgcolor('green')
kap=turtle.Turtle()
kap.shape('turtle')
kap.turtlesize(4)
kap.color('blue')
screen.title('change the turtle')
liste=[(100,20),(32,12),(120,100),(-102,-103),(-300,102),(22,-102),(-230,-12)]
colorList=['black','purple','yellow','pink','cyan','azure','DarkBlue','DarkViolet']

T1=turtle.Turtle()
T2=turtle.Turtle()
T1.hideturtle()
T1.penup()
T1.goto(0,240)
T2.hideturtle()
T2.penup()
T2.goto(0,220)
T3=turtle.Turtle()
T3.penup()
T3.hideturtle()
sayaç=1
def counter():
    T1.clear()
    global sayaç
    T1.write(f'SAYAÇ: {sayaç}', align='center', font=300)
    sayaç+=1
def f(x,y):
    kap.color(random.choice(colorList))
    counter()
def hareket():
    kap.penup()
    kap.speed(1)
    kap.goto(random.choice(liste))
süre=10
def time():
    T2.clear()
    global süre
    T2.write(f'ZAMAN: {süre}', align='center', font=300)
    süre-=1
mili=10000
for i in range(11):
    turtle.ontimer(time,mili)
    mili-=1000
while True:
    kap.onclick(f)
    hareket()
    if süre==0:
        kap.hideturtle()
        T3.write('SÜRE BİTTİ', align='center', font=400)
        break
turtle.mainloop()