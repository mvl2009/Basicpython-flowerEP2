import turtle
tao = turtle.Pen() #ดึงความสามารถการใช้ปากกา
tao.shape('turtle') #แปลงร่างเป็นเต่า

def Rectangle():
    for i in range(10): #ฟั่งชั้น วาดดอกไม้
        tao.circle(50)
        tao.left(36)

def BOX():
    for i in range(10): #ฟั่งชั้น วาด 4 เหลี่ยม
        tao.forward(470)
        tao.left(90)
        
Rectangle()
def GO(x,y): # ยกปากกาเดิน
    tao.penup()
    tao.goto(x,y)
    tao.pendown()


Rectangle()
GO(200,200)
Rectangle()
GO(-150,-150)
BOX()
