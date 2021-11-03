#你的python代码
import turtle as t
def tcyuan(x,y,r):
    t.fillcolor("black")
    t.begin_fill()
    t.seth(0)
    y = y - r
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(r)
    t.end_fill()
def yuan(x,y,r):
    t.seth(0)
    y=y-r
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(r)
def yueliang():
    R = 110 -1

    r = R - 22 -1

    # 月亮填充
    t.penup()
    t.goto(-350+2*R,0)
    t.seth(90)
    t.fillcolor("black")
    t.begin_fill()
    t.circle(R,359)
    t.left(90)
    t.fd(2)
    t.left(90)
    t.circle(-r,359)
    t.left(90)
    t.fd(2)
    t.pendown()
    t.end_fill()
    #轮廓
    yuan(-350 + R, 0, R)
    yuan(-350 + 44 + r - 2, 0, r - 2)
def zhixian(R,r,count,jiaodu):
    t.seth(90+jiaodu)
#    t.goto(0, 0)
    for i in range(count):
        t.penup()
        t.goto(0, 0)
        t.fd(r)
        t.pendown()
        t.fd(R-r)
        t.left(360/count)
def zfx(R,r):
    jiange = 10
#    t.pensize(jiange)
    t.seth(90)
    big = pow((R**2)*2,0.5)
    small = big-2*jiange
    for i in range(13):
        #大线
        t.penup()
        t.goto(0,0)
        t.fd(R)
        t.pendown()
        t.right(135)
        t.fd(big)
        #小线
        t.left(135)
        t.penup()
        t.goto(0, 0)
        t.fd(pow((small**2)/2,0.5))
        t.pendown()
        t.right(135)
        t.fd(small)
        #粗线
        t.pensize(8)
        t.pencolor("black")
        t.left(135)
        t.penup()
        t.goto(0, 0)
        t.fd((R+pow((small ** 2) / 2, 0.5))/2)
        t.pendown()
        t.right(135)
        t.fd((big+small)/2)
        t.pensize(2)
        t.pencolor("yellow")
        t.seth(90+i*30)
    else:
        # 大线
        t.penup()
        t.goto(0, 0)
        t.fd(R)
        t.right(135)
        t.fd(big / 2)
        t.pendown()
        t.fd(big / 2)
        # 小线
        t.left(135)
        t.penup()
        t.goto(0, 0)
        t.fd(pow((small ** 2) / 2, 0.5))
        t.right(135)
        t.fd(small/2)
        t.pendown()
        t.fd(small/2)
        # 粗线
        t.pensize(8)
        t.pencolor("black")
        t.left(135)
        t.penup()
        t.goto(0, 0)
        t.fd((R + pow((small ** 2) / 2, 0.5)) / 2)
        t.right(135)
        t.fd((big + small) / 2/2)
        t.pendown()
        t.fd((big + small) / 2/2)
        t.pensize(2)
        t.pencolor("yellow")
        t.seth(90 + i * 30)
def wjx(r,jiaodu):
    t.fillcolor("black")
    t.penup()
    t.goto(0,0)
    t.seth(90+jiaodu)
    t.fd(r)
    t.pendown()
    t.right(18)
    t.begin_fill()
    for i in range(5):
        t.right(144)
        t.forward(144)
        t.left(72)
        t.forward(144)
    t.end_fill()
    if jiaodu!=0:
        t.seth(90 + jiaodu)
        for i in range(1,6):
            t.penup()
            t.goto(0, 0)
            t.left(72)
            t.pendown()
            t.fd(r)
def xingzuo():
    r = 250
    t.penup()
    t.goto(20,-35)
    t.seth(-45)
    t.fd(r)
    t.pendown()
    xz=['','','','','','','','']
    for i in range(4):
        t.write(xz[i],font=("", 20, ""))
        t.penup()
        t.right(90)
        t.circle(-300, 30)
        t.left(90)
        t.pendown()
    t.penup()
    t.goto(-r/4+10, 5)
    t.seth(135)
    t.fd(r)
    for i in range(4,8):
        t.write(xz[i],font=("", 20, ""))
        t.penup()
        t.right(90)
        t.circle(-300, 30)
        t.left(90)
        t.pendown()
def dxnb(s):
    t.penup()
    t.fd(-19)
    t.left(90)
    t.fd(2)
    t.pendown()
    t.write(s, font=["KaiTi", 30, "bold"])
def taiyang():

    def haicao(r,i):
        # 海藻
        t.fillcolor("black")

        t.penup()
        if i==0:
            t.goto(256, r)
        elif i==1:
            t.goto(256-r, 0)
        else:
            t.goto(256, -r)
        t.pendown()
        t.begin_fill()
        t.seth(2+i*90)
        t.circle(r / 2, 105)
        t.left(10)
        t.circle(-r / 3, 90)
        t.circle(r / 3, 60)
        t.left(20)
        t.circle(r / 3, -80)
        t.left(50)
        t.circle(-r + 10, -40)
        t.right(30)
        t.circle(r / 2 + 10, -50)
        t.penup()
        if i == 0:
            t.goto(256, r)
        elif i == 1:
            t.goto(256 - r, 0)
        else:
            t.goto(256, -r)
        t.pendown()
        t.end_fill()


        t.seth(2 + i * 90)
        t.circle(r / 2, 105)
        t.left(10)
        t.circle(-r / 3, 90)
        t.begin_fill()
        t.circle(r / 3, 60)
        t.left(20)
        t.circle(r / 3, -80)
        t.left(50)
        t.circle(-r + 1
