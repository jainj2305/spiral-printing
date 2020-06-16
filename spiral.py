import turtle
import random
turtle.bgcolor('white')
point=turtle.Turtle()
point.pu()
point.speed(1)
col=['red','black','green','yellow','gray','blue','orange','violet','indigo']
point.setpos(-250,250)
def fun(n):
    num=1
    r=0
    c=0
    while(r<n and c<n):
        point.color(col[random.randint(0,8)])
        for j in range(c,n):
            point.forward(50)
            point.write(num)
            num+=1
        point.color(col[random.randint(0,8)])
        point.right(90)
        r+=1
        for j in range(r,n):
            point.forward(50)
            point.write(num)
            num+=1
        point.color(col[random.randint(0,8)])
        point.right(90)
        n-=1
        for j in range(n,c,-1):
            point.forward(50)
            point.write(num)
            num+=1
        point.color(col[random.randint(0,8)])
        point.right(90)
        c+=1
        for i in range(n,r,-1):
            point.forward(50)
            point.write(num)
            num+=1
        point.right(90)

fun(10)