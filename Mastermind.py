#Mastermind Using Turtle Module
#By Kaustubh Kulkarni 

import turtle as t
from random import shuffle
from time import sleep
from os import system

#Window
wn=t.Screen()
wn.title("Mastermind")
wn.bgcolor("light grey")
wn.setup(height=650, width=400)

#Variables
y_fill1_t=270
y_fill1_b=240

#Game Logic
code_list=["red","green","yellow","blue","black","white","deeppink","darkorange"]
shuffle(code_list)
c0=code_list[0]
c1=code_list[2]
c2=code_list[4]
c3=code_list[6]
code=c0+c1+c2+c3
ans_count=1
ans_limit=10
gameover=False
a0=""
a1=""
a2=""
a3=""

#Message Turtle
msg=t.Turtle()
msg.ht()
msg.speed(0)
msg.penup()
msg.color("grey")
msg.goto(-20,277)

#Mastermind
mastermind=t.Turtle()
mastermind.ht()
mastermind.speed(0)
mastermind.penup()
mastermind.color("grey")
mastermind.pensize(10)
mastermind.goto(-150,-280)
mastermind.write("MASTERMIND",align="left", font=("Arial Black",25,"bold"))

#Painter Turtle
pic=t.Turtle()
pic.ht()
pic.color("grey")
pic.penup()
pic.speed(0)
pic.pensize(10)
pic.goto(-150,-230)
pic.pendown()
pic.fd(250)
pic.penup()
pic.pensize(0.5)

#Drawing the main circles
xline=-120
yline=240
line_no=1
while line_no<=10:
    while xline>=-130 and xline<=30:
        pic.goto(xline,yline)
        pic.pendown()
        pic.circle(15)
        pic.penup()
        xline+=50
    xline=-120
    yline-=50
    line_no+=1

#Drawing Indicator Cirles
linesmall=1
ysmall=260
while linesmall<=10:
    pic.goto(70,ysmall)
    pic.pendown()
    pic.circle(5)
    pic.penup()
    pic.goto(90,ysmall)
    pic.pendown()
    pic.circle(5)
    pic.penup()
    pic.goto(70,ysmall-20)
    pic.pendown()
    pic.circle(5)
    pic.penup()
    pic.goto(90,ysmall-20)
    pic.pendown()
    pic.circle(5)
    pic.penup()
    linesmall+=1
    ysmall-=50
    
#Giving line numbers
line=1
ydraw=245
while line<=10:
    pic.goto(-150,ydraw)
    pic.write(line,align="center", font=("Arial", 10, "normal"))
    line+=1
    ydraw-=50

#Enter and Reset Buttons
pic.goto(175,245)
pic.write("ENTER", align="right", font=("Arial", 15,"normal"))
pic.goto(175,-205)
pic.write("RESET", align="right", font=("Arial", 15,"normal"))
    
#Color Picking Circles
colors=["red","green","yellow","blue","black","white","deeppink","darkorange"]
color_no=0
ycol=190
while color_no<=7:
    pic.goto(140,ycol)
    pic.fillcolor(colors[color_no])
    pic.begin_fill()
    pic.circle(15)
    pic.end_fill()
    ycol-=50
    color_no+=1

def check():
    global ans_count
    global gameover
    global y_fill1_t
    global y_fill1_b
    global a0
    global a1
    global a2
    global a3
    ans=a0+a1+a2+a3
    red=0
    white=0
    if a0!=a1 and a0!=a2 and a0!=a3 and a1!=a2 and a1!=a3 and a2!=a3 and a0!="" and a1!="" and a2!=""and a3!="" and gameover==False:
        y_fill1_t-=50
        y_fill1_b-=50
        ans_count+=1
        if a0==c0:
            red+=1
        elif a0 in code:
            white+=1
        if a1==c1:
            red+=1
        elif a1 in code:
            white+=1
        if a2==c2:
            red+=1
        elif a2 in code:
            white+=1
        if a3==c3:
            red+=1
        elif a3 in code:
            white+=1
        if ans != code:
                ind=[(70,360-50*ans_count),(90,360-50*ans_count),(70,340-50*ans_count),(90,340-50*ans_count)]
                shuffle(ind)
                draw_white=0
                draw_red=0
                while draw_white<white:
                    pic.goto(ind[0])
                    pic.pendown()
                    pic.fillcolor("white")
                    pic.begin_fill()
                    pic.circle(5)
                    pic.end_fill()
                    pic.penup()
                    ind.remove(ind[0])
                    draw_white+=1
                while draw_red<red:
                    pic.goto(ind[0])
                    pic.pendown()
                    pic.fillcolor("red")
                    pic.begin_fill()
                    pic.circle(5)
                    pic.end_fill()
                    pic.penup()
                    ind.remove(ind[0])
                    draw_red+=1
        if ans != code and ans_count>ans_limit:
            msg.write("You ran out of chances!",align="center", font=("Arial", 20, "normal"))
            gameover=True
            mastermind.clear()
            xw=-120
            n=0
            while xw<=30 and n<=6:
                mastermind.goto(xw,-285)
                mastermind.fillcolor(code_list[n])
                mastermind.begin_fill()
                mastermind.circle(15)
                mastermind.end_fill()
                xw+=50
                n+=2
        elif ans==code:
            gameover=True
            msg.write("Congrats! You Won!", align="center", font=("Arial", 20, "normal"))
            mastermind.clear()
            xw=-120
            n=0
            while xw<=30 and n<=6:
                mastermind.goto(xw,-285)
                mastermind.fillcolor(code_list[n])
                mastermind.begin_fill()
                mastermind.circle(15)
                mastermind.end_fill()
                xw+=50
                n+=2
        a0=""
        a1=""
        a2=""
        a3=""
    else:
        msg.write("Invalid Input", align="center", font=("Arial", 20, "normal"))
        sleep(1)
        msg.clear()

#Mouse Click Function
def clk(x,y):
    global a0
    global a1
    global a2
    global a3
    global ans_count
    global y_fill1_b
    global y_fill1_t
    #Colour Picking
    if x>125 and x<155 and gameover==False:
        if y>190 and y<220:
            pic.fillcolor("red")
        if y>140 and y<170:
            pic.fillcolor("green")
        if y>90 and y<120:
            pic.fillcolor("yellow")
        if y>40 and y<70:
            pic.fillcolor("blue")
        if y>-10 and y<20:
            pic.fillcolor("black")
        if y>-60 and y<-30:
            pic.fillcolor("white")
        if y>-110 and y<-80:
            pic.fillcolor("deeppink")
        if y>-160 and y<-130:
            pic.fillcolor("darkorange")
    
    #Enter Button
    if x>105 and x<175 and y>245 and y<275 and gameover==False:
        check()
    #Filling Circles
    if y>y_fill1_b and y<y_fill1_t and ans_count<=ans_limit and gameover==False:
        if x<-105 and x>-135:
            pic.goto(-120,290-50*ans_count)
            pic.pendown()
            pic.begin_fill()
            pic.circle(15)
            pic.end_fill()
            pic.penup()
            a0=pic.fillcolor()
        if x<-55 and x>-85:
            pic.goto(-70,290-50*ans_count)
            pic.pendown()
            pic.begin_fill()
            pic.circle(15)
            pic.end_fill()
            pic.penup()
            a1=pic.fillcolor()
        if x<-5 and x>-35:
            pic.goto(-20,290-50*ans_count)
            pic.pendown()
            pic.begin_fill()
            pic.circle(15)
            pic.end_fill()
            pic.penup()
            a2=pic.fillcolor()
        if x<45 and x>15:
            pic.goto(30,290-50*ans_count)
            pic.pendown()
            pic.begin_fill()
            pic.circle(15)
            pic.end_fill()
            pic.penup()
            a3=pic.fillcolor()
        
    #Reset Button
    if x>110 and x<175 and y>-207 and y<-188:
        wn.bye()
        system("Mastermind.py")
          
#Listening to mouse click
t.onscreenclick(clk)
t.listen()
t.done()
