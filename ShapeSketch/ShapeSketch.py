import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.listen()
t.speed(0)
t.width(5)

first_canvas = []
second_canvas = []
tempo_canvas = []
canvas = []

def up():
    t.setheading(90)
    tempo_canvas.append(11)

def down():
    t.setheading(270)
    tempo_canvas.append(12)

def right():
    t.setheading(0)
    tempo_canvas.append(13)

def left():
    t.setheading(180)
    tempo_canvas.append(14)

def right_angle():
    t.rt(15)
    tempo_canvas.append(15)

def left_angle():
    t.lt(15)
    tempo_canvas.append(16)

def square():
    t.begin_fill()
    for i in range(4):
        t.fd(100)
        t.rt(90)
    t.end_fill()
    tempo_canvas.append(17)
        
def triangle():
    t.rt(60)
    t.begin_fill()
    for j in range(3):
        t.fd(100)
        t.rt(120)
    t.end_fill()
    t.lt(60)
    tempo_canvas.append(18)

def circle():
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    tempo_canvas.append(19)

def penup():
    t.penup()
    tempo_canvas.append(20)

def pendown():
    t.pendown()
    tempo_canvas.append(21)

def move():
    t.fd(10)
    tempo_canvas.append(22)

def undo():
    t.undo()
    tempo_canvas.append(23)

def white():
    t.color("black", "white")
    tempo_canvas.append(24)

def red():
    t.color("black", "red")
    tempo_canvas.append(25)

def orange():
    t.color("black", "orange")
    tempo_canvas.append(26)
    
def yellow():
    t.color("black", "yellow")
    tempo_canvas.append(27)

def green():
    t.color("black", "green")
    tempo_canvas.append(28)

def blue():
    t.color("black", "blue")
    tempo_canvas.append(29)

def indigo():
    t.color("black", "indigo")
    tempo_canvas.append(30)

def violet():
    t.color("black", "violet")
    tempo_canvas.append(31)


### Start ###
    
def start():
    t.clear()
    t.hideturtle()
    t.penup()
    t.goto(-1000, 1000)
    t.pendown()

    t.color("light blue")
    t.begin_fill()
    for i in range(4):
        t.fd(10000)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-670, 350)
    t.pendown()

    t.color("black", "white")
    t.begin_fill()
    for i in range(2):
        t.fd(1340)
        t.rt(90)
        t.fd(650)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-330, 180)
    t.write("ShapeSketch", font=("arial", 80, "bold"))


    t.goto(-100, 0)
    t.write("[D] Draw", font=("arial", 30, "bold"))

    t.goto(-100, -80)
    t.write("[A] Album", font=("arial", 30, "bold"))

    t.goto(-100, -160)
    t.write("[I] Instructions", font=("arial", 30, "bold"))

### Draw ###

def draw():
    t.clear()
    t.hideturtle()
    t.penup()
    t.goto(-1000, 1000)
    t.pendown()

    t.color("light blue")
    t.begin_fill()
    for i in range(4):
        t.fd(10000)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-670, 350)
    t.pendown()

    t.color("black", "white")
    t.begin_fill()
    for i in range(2):
        t.fd(1340)
        t.rt(90)
        t.fd(650)
        t.rt(90)
    t.end_fill()
    t.penup()

    t.goto(-290, 180)
    t.write("Choose a Canvas:", font=("Arial", 50, "bold"))

    t.goto(-140, 20)
    t.write("[J] First Canvas", font=("arial", 30, "bold"))

    t.goto(-140, -80)
    t.write("[K] Second Canvas", font=("arial", 30, "bold"))

    t.goto(550, -370)
    t.color("red")
    t.write("[B] Back", font=("arial", 20, "normal"))
    t.color("black", "white")

### First Canvas ###

def canvas1():

    canvas.clear()
    canvas.append(1)
    tempo_canvas.clear()

    t.showturtle()
    t.clear()
    t.penup()
    t.goto(-1000, 1000)
    t.pendown()

    t.color("light blue")
    t.begin_fill()
    for i in range(4):
        t.fd(10000)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-670, 350)
    t.pendown()

    t.color("black", "white")
    t.begin_fill()
    for i in range(2):
        t.fd(1340)
        t.rt(90)
        t.fd(650)
        t.rt(90)
    t.end_fill()

    t.penup()

    t.goto(550, -370)
    t.color("red")
    t.write("[B] Back", font=("arial", 20, "normal"))
    t.color("black", "white")

    t.goto(-640, -370)
    t.write("[0] Save", font=("arial", 20, "normal"))

    t.home()
    t.pendown()
    

### Second Canvas ###

def canvas2():

    canvas.clear()
    canvas.append(2)
    tempo_canvas.clear()

    t.showturtle()
    t.clear()
    t.penup()
    t.goto(-1000, 1000)
    t.pendown()

    t.color("light blue")
    t.begin_fill()
    for i in range(4):
        t.fd(10000)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-670, 350)
    t.pendown()

    t.color("black", "white")
    t.begin_fill()
    for i in range(2):
        t.fd(1340)
        t.rt(90)
        t.fd(650)
        t.rt(90)
    t.end_fill()

    t.penup()

    t.goto(550, -370)
    t.color("red")
    t.write("[B] Back", font=("arial", 20, "normal"))
    t.color("black", "white")

    t.goto(-640, -370)
    t.write("[0] Save", font=("arial", 20, "normal"))
    
    t.home()
    t.pendown()
    
### Album ###
    
def pic():
    t.hideturtle()
    t.clear()
    t.penup()
    t.goto(-1000, 1000)
    t.pendown()

    t.color("light blue")
    t.begin_fill()
    for i in range(4):
        t.fd(10000)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-670, 350)
    t.pendown()

    t.color("black", "white")
    t.begin_fill()
    for i in range(2):
        t.fd(1340)
        t.rt(90)
        t.fd(650)
        t.rt(90)
    t.end_fill()

    t.penup()

    t.goto(550, -370)
    t.color("red")
    t.write("[B] Back", font=("arial", 20, "normal"))
    t.color("black", "white")

    t.color("red")    
    t.goto(-640, -380)
    t.write("[ 1 ]", font=("arial", 40, "bold"))
    t.color("black", "white")
    
    t.goto(-490, -370)
    t.write("[ 2 ]", font=("arial", 30, "normal"))

    t.goto(-340, -370)
    t.write("[ 3 ]", font=("arial", 30, "normal"))

    t.goto(-190, -370)
    t.write("[ 4 ]", font=("arial", 30, "normal"))

    t.goto(-40, -370)
    t.write("[ 5 ]", font=("arial", 30, "normal"))

    t.home()

    t.color('brown')
    t.begin_fill()
    t.circle(103)

    t.lt(90)
    t.penup()
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.rt(180)
    t.pendown()
    t.end_fill()

    t.color('brown')
    t.begin_fill()
    for i in range(4):
      t.fd(200)
      t.rt(90) 
    t.end_fill()

    t.fd(60)

    for j in range(2):
      t.color('black')
      t.begin_fill()
      t.circle(20)
      t.end_fill()

      t.penup()
      t.lt(90)
      t.fd(15)
      t.pendown()

      t.rt(90)
      t.color('white')
      t.begin_fill()
      t.circle(5)
      t.end_fill()

      t.penup()
      t.rt(90)
      t.fd(15)
      t.lt(90)
      t.pendown()

      t.penup()
      t.fd(80)
      t.pendown()

    t.penup()
    t.home()
    t.fd(25)
    t.pendown()
    for k in range(2):
      t.color('orange')
      t.begin_fill()
      t.circle(25)
      t.end_fill()
            
      t.penup()
      t.rt(180)
      t.fd(50)
      t.rt(180)
      t.pendown()

    t.penup()
    t.fd(50)
    t.pendown()

    t.begin_fill()
    for l in range(4):
      t.fd(50)
      t.lt(90)
    t.end_fill()

    t.penup()
    t.home()
    t.rt(90)
    t.fd(100)
    t.lt(90)
    t.pendown()

    t.color('black')
    t.fd(150)
    t.bk(300)

    t.penup()
    t.color("black", "white")



### Picture 1 ###
    
def pic1():
    t.hideturtle()
    t.clear()
    t.penup()
    t.goto(-1000, 1000)
    t.pendown()

    t.color("light blue")
    t.begin_fill()
    for i in range(4):
        t.fd(10000)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-670, 350)
    t.pendown()

    t.color("black", "white")
    t.begin_fill()
    for i in range(2):
        t.fd(1340)
        t.rt(90)
        t.fd(650)
        t.rt(90)
    t.end_fill()

    t.penup()

    t.goto(550, -370)
    t.color("red")
    t.write("[B] Back", font=("arial", 20, "normal"))
    t.color("black", "white")

    t.color("red")    
    t.goto(-640, -380)
    t.write("[ 1 ]", font=("arial", 40, "bold"))
    t.color("black", "white")
    
    t.goto(-490, -370)
    t.write("[ 2 ]", font=("arial", 30, "normal"))

    t.goto(-340, -370)
    t.write("[ 3 ]", font=("arial", 30, "normal"))

    t.goto(-190, -370)
    t.write("[ 4 ]", font=("arial", 30, "normal"))

    t.goto(-40, -370)
    t.write("[ 5 ]", font=("arial", 30, "normal"))

    t.home()

    t.color('brown')
    t.begin_fill()
    t.circle(103)

    t.lt(90)
    t.penup()
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.rt(180)
    t.pendown()
    t.end_fill()

    t.color('brown')
    t.begin_fill()
    for i in range(4):
      t.fd(200)
      t.rt(90) 
    t.end_fill()

    t.fd(60)

    for j in range(2):
      t.color('black')
      t.begin_fill()
      t.circle(20)
      t.end_fill()

      t.penup()
      t.lt(90)
      t.fd(15)
      t.pendown()

      t.rt(90)
      t.color('white')
      t.begin_fill()
      t.circle(5)
      t.end_fill()

      t.penup()
      t.rt(90)
      t.fd(15)
      t.lt(90)
      t.pendown()

      t.penup()
      t.fd(80)
      t.pendown()

    t.penup()
    t.home()
    t.fd(25)
    t.pendown()
    for k in range(2):
      t.color('orange')
      t.begin_fill()
      t.circle(25)
      t.end_fill()
            
      t.penup()
      t.rt(180)
      t.fd(50)
      t.rt(180)
      t.pendown()

    t.penup()
    t.fd(50)
    t.pendown()

    t.begin_fill()
    for l in range(4):
      t.fd(50)
      t.lt(90)
    t.end_fill()

    t.penup()
    t.home()
    t.rt(90)
    t.fd(100)
    t.lt(90)
    t.pendown()

    t.color('black')
    t.fd(150)
    t.bk(300)

    t.penup()
    t.color("black", "white")



### Picture 2 ###
    
def pic2():
    t.hideturtle()
    t.clear()
    t.penup()
    t.goto(-1000, 1000)
    t.pendown()

    t.color("light blue")
    t.begin_fill()
    for i in range(4):
        t.fd(10000)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-670, 350)
    t.pendown()

    t.color("black", "white")
    t.begin_fill()
    for i in range(2):
        t.fd(1340)
        t.rt(90)
        t.fd(650)
        t.rt(90)
    t.end_fill()

    t.penup()

    t.goto(550, -370)
    t.color("red")
    t.write("[B] Back", font=("arial", 20, "normal"))
    t.color("black", "white")

    t.goto(-640, -370)
    t.write("[ 1 ]", font=("arial", 30, "normal"))

    t.color("red")
    t.goto(-505, -380)
    t.write("[ 2 ]", font=("arial", 40, "bold"))
    t.color("black", "white")

    t.goto(-340, -370)
    t.write("[ 3 ]", font=("arial", 30, "normal"))

    t.goto(-190, -370)
    t.write("[ 4 ]", font=("arial", 30, "normal"))

    t.goto(-40, -370)
    t.write("[ 5 ]", font=("arial", 30, "normal"))

    t.home()

    #First layer#
    t.penup()
    t.goto(-250, 300)
    t.pendown()

    for tri in range(5):
      t.rt(10)
      for triangle in range(2):
        t.fd(100)
        t.right(160)
      
      t.lt(60)
      t.fd(35)
            
      t.penup()
      t.rt(90)
      t.fd(100)
      t.pendown()

    #Second layer#
    t.penup()
    t.goto(-250, 230)
    t.pendown()

    for tri2 in range(20):
      if (tri2 == 2) or (tri2 == 5) or (tri2 == 8) or (tri2 == 11) or (tri2 == 14) or (tri2 == 17):
        t.penup()
      
      t.rt(50)
      for tri1 in range(3):
        if tri1 == 2:
          t.penup()
          t.rt(50)
          t.fd(45)
          t.pendown()
        else:
          t.fd(30)
          t.rt(85)    
        
      t.penup()
      t.rt(90)
      t.fd(25)
      t.pendown()

    #Third layer#
    t.penup()
    t.goto(-250, 150)
    t.pendown()

    for s1 in range(13):
      for s2 in range(2):
        t.fd(20)
        t.rt(90)
        t.fd(30)
        t.rt(90)

      t.penup()
      t.fd(40)
      t.pendown()

    #Fourth layer#
    t.penup()
    t.goto(-250, 80)
    t.pendown()

    for tri in range(17):
      if (tri == 5) or (tri == 11) or (tri == 17):
        t.penup()
        
      t.rt(10)
      for triangle in range(2):
        t.fd(30)
        t.right(160)
      
      t.lt(60)
      t.fd(10)
            
      t.penup()
      t.rt(90)
      t.fd(30)
      t.pendown()

    #Fifth layer#
    t.penup()
    t.goto(-250, 30)
    t.pendown()

    for squ in range(15):
      t.color("Black")
      t.begin_fill()
      
      for sque in range(4):    
        t.fd(20)
        t.rt(90)
        
      t.end_fill()
      t.penup()
      t.fd(35)
      t.pendown()

    #Sixth layer#
    t.penup()
    t.goto(-250, -30)
    t.pendown()

    for w in range(4):
      t.color("Black")
      t.begin_fill()
      
      for q in range(3):
        t.fd(100)
        t.rt(120)
            
      t.end_fill()
      t.penup()
      t.fd(130)
      t.pendown()

    t.penup()
    t.goto(-250, -120)
    t.fd(64)
    t.pendown()

    for a in range(4):
      t.color("Black")
      t.begin_fill()
      
      for e in range(3):
        t.fd(100)
        t.lt(120)

      t.end_fill()
      t.penup()
      t.fd(130)
      t.pendown()  

    #Seventh layer#
    t.penup()
    t.goto(-250, -150)
    t.pendown()
        
    for qt in range(17):
      if (qt == 2) or (qt == 3) or (qt == 4) or (qt == 5) or (qt == 8) or (qt == 9) or (qt == 10) or (qt == 11) or (qt == 14) or (qt == 15) or (qt == 16):
         t.penup()
      
      if (qt == 1) or (qt == 7)or (qt == 13):
        t.color("black" , "white")
        t.begin_fill()
      t.rt(10)
      for l in range(2):
        t.fd(50)
        t.right(160)
      
      t.end_fill()
      t.lt(60)
      t.fd(17.4)
            
      t.penup()
      t.rt(90)
      t.fd(30)
      t.pendown()

    t.rt(180)

    for qt1 in range(17):
      if (qt1 == 2) or (qt1 == 3) or (qt1 == 4) or (qt1 == 5) or (qt1 == 8) or (qt1 == 9) or (qt1 == 10) or (qt1 == 11) or (qt1 == 14) or (qt1 == 15) or (qt1 == 16):
         t.penup()
      
      if (qt1 == 1) or (qt1 == 7)or (qt1 == 13):
        t.color("black" , "white")
        t.begin_fill()
      t.lt(10)
      for v in range(2):
        t.fd(50)
        t.lt(160)   
            
      t.end_fill()
      t.rt(60)
      t.fd(17.3)

      t.penup()
      t.lt(90)
      t.fd(30)
      t.pendown()

    #Eighth layer#
    t.penup()
    t.goto(-250, -200)
    t.rt(180)
    t.pendown()    

    for v in range(18):
      if (v == 2) or (v == 5) or (v == 8) or (v == 11) or (v == 14) or (v == 17):
        t.penup()
      else:
        t.color("black")
        t.begin_fill()
        
      t.rt(10)
      for l in range(2):
          t.fd(50)
          t.right(160)    

      t.end_fill()
      t.lt(60)
      t.fd(17.3)

      t.penup()
      t.rt(90)
      t.fd(30)
      t.pendown()
      
    #Ninth layer#
    t.penup()
    t.goto(-250, -250)
    t.pendown()  
     
    for p in range(15):
      t.lt(45)
      for o in range(4):
        t.fd(20)
        t.rt(90)

      t.rt(45)
      t.penup()
      t.fd(35)
      t.pendown()

    t.penup()
    t.color("black", "white")

### Picture 3 ###
      
def pic3():
    t.hideturtle()
    t.clear()
    t.penup()
    t.goto(-1000, 1000)
    t.pendown()

    t.color("light blue")
    t.begin_fill()
    for i in range(4):
        t.fd(10000)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-670, 350)
    t.pendown()

    t.color("black", "white")
    t.begin_fill()
    for i in range(2):
        t.fd(1340)
        t.rt(90)
        t.fd(650)
        t.rt(90)
    t.end_fill()

    t.penup()

    t.goto(550, -370)
    t.color("red")
    t.write("[B] Back", font=("arial", 20, "normal"))
    t.color("black", "white")

    t.goto(-640, -370)
    t.write("[ 1 ]", font=("arial", 30, "normal"))

    t.goto(-490, -370)
    t.write("[ 2 ]", font=("arial", 30, "normal"))

    t.color("red")
    t.goto(-355, -380)
    t.write("[ 3 ]", font=("arial", 40, "bold"))
    t.color("black", "white")

    t.goto(-190, -370)
    t.write("[ 4 ]", font=("arial", 30, "normal"))

    t.goto(-40, -370)
    t.write("[ 5 ]", font=("arial", 30, "normal"))

    t.home()


    #SKY BACKGROUND#

    t.width(3)

    t.penup()
    t.goto(-620, 300)
    t.pendown()

    t.color("black", "light blue")
    t.begin_fill()
    for n in range(2):
        t.fd(1240)
        t.rt(90)
        t.fd(560)
        t.rt(90)
    t.end_fill()


    #CLOUDS#

    t.penup()
    t.goto(620,-200)
    t.pendown()

    t.color("black", "light gray")
    t.begin_fill()

    for i in range(13):
        t.setheading(90)
        t.circle(47.7,180)
        
    t.setheading(270)
    t.fd(60)
    t.lt(90)
    t.fd(1240)
    t.lt(90)
    t.fd(60)

    t.end_fill()


    #SUN#

    t.penup()
    t.goto(400,250)
    t.lt(90)
    t.pendown()

    t.color("black", "yellow")
    t.begin_fill()
    t.circle(75)
    t.end_fill()

    t.penup()
    t.goto(370,250)
    t.rt(45)
    t.pendown()
    t.fd(30)

    t.penup()
    t.goto(330,220)
    t.pendown()
    t.fd(30)

    t.penup()
    t.goto(320,190)
    t.setheading(180)
    t.pendown()
    t.fd(30)

    t.penup()
    t.goto(320,150)
    t.lt(35)
    t.pendown()
    t.fd(30)

    t.penup()
    t.goto(340,110)
    t.lt(20)
    t.pendown()
    t.fd(30)

    t.penup()
    t.goto(380,100)
    t.lt(20)
    t.pendown()
    t.fd(30)

    t.penup()
    t.goto(430,110)
    t.lt(30)
    t.pendown()
    t.fd(30)

    t.penup()
    t.goto(465,110)
    t.lt(20)
    t.pendown()
    t.fd(30)

    t.penup()
    t.goto(485,150)
    t.lt(20)
    t.pendown()
    t.fd(30)

    t.penup()
    t.goto(485,190)
    t.lt(45)
    t.pendown()
    t.fd(30)

    t.penup()
    t.goto(470,230)
    t.lt(45)
    t.pendown()
    t.fd(30)

    t.penup()
    t.goto(435,250)
    t.lt(15)
    t.pendown()
    t.fd(25)


    #PIPES UP#

    t.penup()
    t.goto(-500, 300)
    t.setheading(270)
    t.pendown()

    t.color("black", "light green")
    t.begin_fill()
    for i in range(2):
        t.fd(250)
        t.lt(90)
        t.fd(120)
        t.lt(90)
    t.end_fill()

    t.fd(250)

    t.color("black", "light green")
    t.begin_fill()
    t.rt(90)
    t.fd(30)

    t.lt(90)
    t.fd(40)

    t.lt(90)
    t.fd(180)

    t.lt(90)
    t.fd(40)

    t.lt(90)
    t.fd(30)
    t.end_fill()

    t.rt(90)
    t.fd(250)
    t.setheading(0)

    t.fd(180)
    t.rt(90)

    t.color("black", "light green")
    t.begin_fill()
    for i in range(2):
        t.fd(60)
        t.lt(90)
        t.fd(120)
        t.lt(90)
    t.end_fill()

    t.fd(60)

    t.color("black", "light green")
    t.begin_fill()
    t.rt(90)
    t.fd(30)

    t.lt(90)
    t.fd(40)

    t.lt(90)
    t.fd(180)

    t.lt(90)
    t.fd(40)

    t.lt(90)
    t.fd(30)
    t.end_fill()

    t.rt(90)
    t.fd(60)
    t.setheading(0)

    t.fd(180)
    t.rt(90)

    t.color("black", "light green")
    t.begin_fill()
    for i in range(2):
        t.fd(320)
        t.lt(90)
        t.fd(120)
        t.lt(90)
    t.end_fill()

    t.fd(320)

    t.color("black", "light green")
    t.begin_fill()
    t.rt(90)
    t.fd(30)

    t.lt(90)
    t.fd(40)

    t.lt(90)
    t.fd(180)

    t.lt(90)
    t.fd(40)

    t.lt(90)
    t.fd(30)
    t.end_fill()

    t.rt(90)
    t.fd(320)
    t.setheading(0)

    t.fd(180)
    t.rt(90)

    t.color("black", "light green")
    t.begin_fill()
    for i in range(2):
        t.fd(260)
        t.lt(90)
        t.fd(120)
        t.lt(90)
    t.end_fill()

    t.fd(260)

    t.color("black", "light green")
    t.begin_fill()
    t.rt(90)
    t.fd(30)

    t.lt(90)
    t.fd(40)

    t.lt(90)
    t.fd(180)

    t.lt(90)
    t.fd(40)

    t.lt(90)
    t.fd(30)
    t.end_fill()

    t.rt(90)
    t.fd(260)


    #PIPES DOWN#

    t.penup()
    t.setheading(270)
    t.fd(560)
    t.setheading(90)
    t.pendown()

    t.color("black", "light green")
    t.begin_fill()
    for i in range(2):
        t.fd(140)
        t.lt(90)
        t.fd(120)
        t.lt(90)
    t.end_fill()

    t.fd(140)

    t.color("black", "light green")
    t.begin_fill()
    t.rt(90)
    t.fd(30)

    t.lt(90)
    t.fd(40)

    t.lt(90)
    t.fd(180)

    t.lt(90)
    t.fd(40)

    t.lt(90)
    t.fd(30)
    t.end_fill()

    t.rt(90)
    t.fd(140)

    t.rt(90)
    t.fd(180)
    t.setheading(90)

    t.color("black", "light green")
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.lt(90)
        t.fd(120)
        t.lt(90)
    t.end_fill()

    t.fd(80)

    t.color("black", "light green")
    t.begin_fill()
    t.rt(90)
    t.fd(30)

    t.lt(90)
    t.fd(40)

    t.lt(90)
    t.fd(180)

    t.lt(90)
    t.fd(40)

    t.lt(90)
    t.fd(30)
    t.end_fill()

    t.rt(90)
    t.fd(80)

    t.rt(90)
    t.fd(180)
    t.setheading(90)

    t.color("black", "light green")
    t.begin_fill()
    for i in range(2):
        t.fd(340)
        t.lt(90)
        t.fd(120)
        t.lt(90)
    t.end_fill()

    t.fd(340)

    t.color("black", "light green")
    t.begin_fill()
    t.rt(90)
    t.fd(30)

    t.lt(90)
    t.fd(40)

    t.lt(90)
    t.fd(180)

    t.lt(90)
    t.fd(40)

    t.lt(90)
    t.fd(30)
    t.end_fill()

    t.rt(90)
    t.fd(340)

    t.rt(90)
    t.fd(180)
    t.setheading(90)

    t.color("black", "light green")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.lt(90)
        t.fd(120)
        t.lt(90)
    t.end_fill()

    t.fd(150)

    t.color("black", "light green")
    t.begin_fill()
    t.rt(90)
    t.fd(30)

    t.lt(90)
    t.fd(40)

    t.lt(90)
    t.fd(180)

    t.lt(90)
    t.fd(40)

    t.lt(90)
    t.fd(30)
    t.end_fill()

    t.rt(90)
    t.fd(150)

    t.penup()
    t.home()
    t.width(5)
    t.color("black", "white")
    

### Picture 4 ###

def pic4():
    t.hideturtle()
    t.clear()
    t.penup()
    t.goto(-1000, 1000)
    t.pendown()

    t.color("light blue")
    t.begin_fill()
    for i in range(4):
        t.fd(10000)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-670, 350)
    t.pendown()

    t.color("black", "white")
    t.begin_fill()
    for i in range(2):
        t.fd(1340)
        t.rt(90)
        t.fd(650)
        t.rt(90)
    t.end_fill()

    t.penup()

    t.goto(550, -370)
    t.color("red")
    t.write("[B] Back", font=("arial", 20, "normal"))
    t.color("black", "white")

    t.goto(-640, -370)
    t.write("[ 1 ]", font=("arial", 30, "normal"))

    t.goto(-490, -370)
    t.write("[ 2 ]", font=("arial", 30, "normal"))

    t.goto(-340, -370)
    t.write("[ 3 ]", font=("arial", 30, "normal"))

    t.color("red")
    t.goto(-205, -380)
    t.write("[ 4 ]", font=("arial", 40, "bold"))
    t.color("black", "white")
    
    t.goto(-40, -370)
    t.write("[ 5 ]", font=("arial", 30, "normal"))

    t.home()
    t.pendown()
    
    if first_canvas:
        for element in first_canvas:
            if element == 11:
                up()
            elif element == 12:
                down()
            elif element == 13:
                right()
            elif element == 14:
                left()
            elif element == 15:
                right_angle()
            elif element == 16:
                left_angle()
            elif element == 17:
                square()
            elif element == 18:
                triangle()
            elif element == 19:
                circle()
            elif element == 20:
                penup()
            elif element == 21:
                pendown()
            elif element == 22:
                move()
            elif element == 23:
                undo()
            elif element == 24:
                white()
            elif element == 25:
                red()
            elif element == 26:
                orange()
            elif element == 27:
                yellow()
            elif element == 28:
                green()
            elif element == 29:
                blue()
            elif element == 30:
                indigo()
            elif element == 31:
                violet()
    t.penup()
    t.home()
    t.color("black", "white")
        
### Picture 5 ###
    
def pic5():
    t.hideturtle()
    t.clear()
    t.penup()
    t.goto(-1000, 1000)
    t.pendown()

    t.color("light blue")
    t.begin_fill()
    for i in range(4):
        t.fd(10000)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-670, 350)
    t.pendown()

    t.color("black", "white")
    t.begin_fill()
    for i in range(2):
        t.fd(1340)
        t.rt(90)
        t.fd(650)
        t.rt(90)
    t.end_fill()

    t.penup()

    t.goto(550, -370)
    t.color("red")
    t.write("[B] Back", font=("arial", 20, "normal"))
    t.color("black", "white")

    t.goto(-640, -370)
    t.write("[ 1 ]", font=("arial", 30, "normal"))

    t.goto(-490, -370)
    t.write("[ 2 ]", font=("arial", 30, "normal"))

    t.goto(-340, -370)
    t.write("[ 3 ]", font=("arial", 30, "normal"))

    t.goto(-190, -370)
    t.write("[ 4 ]", font=("arial", 30, "normal"))

    t.color("red")
    t.goto(-55, -380)
    t.write("[ 5 ]", font=("arial", 40, "bold"))
    t.color("black", "white")
    
    t.home()
    t.pendown()

    
    if second_canvas:
        for element in second_canvas:
            if element == 11:
                up()
            elif element == 12:
                down()
            elif element == 13:
                right()
            elif element == 14:
                left()
            elif element == 15:
                right_angle()
            elif element == 16:
                left_angle()
            elif element == 17:
                square()
            elif element == 18:
                triangle()
            elif element == 19:
                circle()
            elif element == 20:
                penup()
            elif element == 21:
                pendown()
            elif element == 22:
                move()
            elif element == 23:
                undo()
            elif element == 24:
                white()
            elif element == 25:
                red()
            elif element == 26:
                orange()
            elif element == 27:
                yellow()
            elif element == 28:
                green()
            elif element == 29:
                blue()
            elif element == 30:
                indigo()
            elif element == 31:
                violet()

    t.penup()
    t.home()
    t.color("black", "white")

### Instruction ###

def instruction():
    t.clear()
    t.hideturtle()
    t.penup()
    t.goto(-1000, 1000)
    t.pendown()

    t.color("light blue")
    t.begin_fill()
    for i in range(4):
        t.fd(10000)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-670, 350)
    t.pendown()

    t.color("black", "white")
    t.begin_fill()
    for i in range(2):
        t.fd(1340)
        t.rt(90)
        t.fd(650)
        t.rt(90)
    t.end_fill()

    t.penup()

    t.goto(-640, 250)
    t.write("Instructions:", font=("Arial", 40, "bold"))

    t.goto(-630, 220)
    t.write("Use the arrow keys and other command keys to draw anything.", font=("Arial", 20, "normal"))


    t.goto(-640, 120)
    t.write("Commands:", font=("arial", 40, "bold"))

    t.goto(-610, 80)
    t.write("'S' = Square", font=("arial", 20, "normal"))

    t.goto(-610, 40)
    t.write("'T' = Triangle", font=("arial", 20, "normal"))

    t.goto(-610, 0)
    t.write("'C' = Circle", font=("arial", 20, "normal"))

    t.goto(-610, -40)
    t.write("'U' = Pen up", font=("arial", 20, "normal"))

    t.goto(-610, -80)
    t.write("'P' = Pendown", font=("arial", 20, "normal"))

    t.goto(-610, -120)
    t.write("'M' = Move", font=("arial", 20, "normal"))

    t.goto(-610, -160)
    t.write("'Z' = Undo", font=("arial", 20, "normal"))

    t.goto(-310, 80)
    t.write("'Arrow key up' = Face up", font=("arial", 20, "normal"))

    t.goto(-310, 40)
    t.write("'Arrow key down' = Face down", font=("arial", 20, "normal"))

    t.goto(-310, 0)
    t.write("'Arrow key right' = Face right", font=("arial", 20, "normal"))

    t.goto(-310, -40)
    t.write("'Arrow key left' = Face left", font=("arial", 20, "normal"))

    t.goto(-310, -80)
    t.write("'<' = Rotate left 15°", font=("arial", 20, "normal"))

    t.goto(-310, -120)
    t.write("'>' = Rotate right 15°", font=("arial", 20, "normal"))

    t.goto(-310, -160)
    t.write("'F1' = Change color to White", font=("arial", 20, "normal"))

    t.goto(200, 80)
    t.write("'F2' = Change color to Red", font=("arial", 20, "normal"))

    t.goto(200, 40)
    t.write("'F3' = Change color to Orange", font=("arial", 20, "normal"))

    t.goto(200, 0)
    t.write("'F4' = Change color to Yellow", font=("arial", 20, "normal"))

    t.goto(200, -40)
    t.write("'F5' = Change color to Green", font=("arial", 20, "normal"))

    t.goto(200, -80)
    t.write("'F6' = Change color to Blue", font=("arial", 20, "normal"))

    t.goto(200, -120)
    t.write("'F7' = Change color to Indigo", font=("arial", 20, "normal"))

    t.goto(200, -160)
    t.write("'F8' = Change color to Violet", font=("arial", 20, "normal"))

    t.goto(550, -370)
    t.color("red")
    t.write("[B] Back", font=("arial", 20, "normal"))
    t.color("black", "white")

def save():

    t.penup()
    t.goto(-100, -385)
    t.color("red")
    t.write("SAVED!", font=("arial", 40, "bold"))
    t.color("black", "white")
    t.home()
    t.pendown()
    
    if canvas[0] == 1:
        first_canvas.clear()
        first_canvas.extend(tempo_canvas)

    elif canvas[0] == 2:
        second_canvas.clear()
        second_canvas.extend(tempo_canvas)


screen.onkey(up, 'Up')
screen.onkey(down, 'Down')
screen.onkey(right, 'Right')
screen.onkey(left, 'Left')
screen.onkey(right_angle, ',')
screen.onkey(left_angle, '.')
screen.onkey(square, 's')
screen.onkey(triangle, 't')
screen.onkey(circle, 'c')
screen.onkey(penup, 'u')
screen.onkey(pendown, 'p')
screen.onkey(move, 'm')
screen.onkey(undo, 'z')
screen.onkey(white, 'F1')
screen.onkey(red, 'F2')
screen.onkey(orange, 'F3')
screen.onkey(yellow, 'F4')
screen.onkey(green, 'F5')
screen.onkey(blue, 'F6')
screen.onkey(indigo, 'F7')
screen.onkey(violet, 'F8')
screen.onkey(start, 'b')
screen.onkey(instruction, 'i')
screen.onkey(draw, 'd')
screen.onkey(canvas1, 'j')
screen.onkey(canvas2, 'k')
screen.onkey(save, '0')
screen.onkey(pic, 'a')
screen.onkey(pic1, '1')
screen.onkey(pic2, '2')
screen.onkey(pic3, '3')
screen.onkey(pic4, '4')
screen.onkey(pic5, '5')


t.hideturtle()
t.penup()
t.goto(-1000, 1000)
t.pendown()

t.color("light blue")
t.begin_fill()
for i in range(4):
    t.fd(10000)
    t.rt(90)
t.end_fill()

t.penup()
t.goto(-670, 350)
t.pendown()

t.color("black", "white")
t.begin_fill()
for i in range(2):
    t.fd(1340)
    t.rt(90)
    t.fd(650)
    t.rt(90)
t.end_fill()

t.penup()
t.goto(-330, 180)
t.pendown()

t.write("ShapeSketch", font=("arial", 80, "bold"))

t.penup()
t.goto(-100, 0)
t.pendown()

t.write("[D] Draw", font=("arial", 30, "bold"))

t.penup()
t.goto(-100, -80)
t.pendown()

t.write("[A] Album", font=("arial", 30, "bold"))

t.penup()
t.goto(-100, -160)
t.pendown()

t.write("[I] Instructions", font=("arial", 30, "bold"))
t.penup()



