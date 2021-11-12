# Helicopter Crash Game in Python 3 using Turtle Graphic module
# Programmer by : SHAHID

# Use space bar to move helicopter up
# ------------------------------------------------------------


import turtle
import time


wn = turtle.Screen()
wn.title('#VirtualGamer_SHAHID_AKHTAR')

wn.tracer(0)
time.sleep(4)
wn.bgcolor('green')


load_pen=turtle.Turtle()
load_pen.hideturtle()
load_pen.penup()
load_pen.goto(-180,-250)
load_pen.hideturtle()
load_pen.color('white')
load_pen.write('Press any key to Continue ',False,align='left',font=("Courier",18,"bold"))

again2=turtle.Turtle()
again2.hideturtle()
pos='nload'

heli_mode="stop"
def choose_mode():
    pass


def change():
    
    #pygame.mixer.music.load("gta_song.mp3")
    #pygame.mixer.music.play()
    #winsound.PlaySound("shoot-type.wav",winsound.SND_ASYNC)
    time.sleep(3)
    wn.bgcolor('lightblue')
    load_pen.reset()
    load_pen.penup()
    load_pen.shape('circle')
    load_pen.goto(-200,-200)
    load_pen.pendown()
    
    load_pen.pencolor('red')
    load_pen.width(6)
    global pos
    pos='load'
    

#game----------------

def start_game():

    
    #pygame.mixer.init()
    wn.setup(width=780,height=630)
    wn.tracer(0)
    penc= turtle.Turtle()

    sid=turtle.Turtle()
    again=turtle.Turtle()

        
    def text(t,string,x,y,color,size):
        t.penup()
        t.color(color)
        t.setposition(x,y)
        t.write(string,False,align="left",font=("Courier",size,"bold"))
        

    
        
    
    def ex():
        wn.clear()
        #wn.bgpic('logo4.gif')
        wn.bgcolor('red')
        load_pen.color('white')
        load_pen.up()
        load_pen.goto(-170,-180)
        load_pen.write("Click on Screen to exit",False,align="left",font=("Courier",18,"bold"))
        wn.exitonclick()
        #pygame.mixer.music.stop()
    

    
    def about():
        wn.clear()
        wn.bgcolor('black')
        
        n=turtle.Turtle()
        n.hideturtle()
        st='CreDits'
        text(n,st,-100,220,"blue",30)
        st2='This Program is created by Shahid Akhtar.'
        text(n,st2,-280,100,"white",16)
        st2='Love Programming and building crazy'
        text(n,st2,-280,70,"white",16)
        st2='stuff of Turtle graphic in Python'
        text(n,st2,-280,40,"white",16)
        
        
        time.sleep(9)
        wn.clear()
        choose_mode(again2)



    def start_game():
        global col
        
        
        
        again.hideturtle()
        sid.hideturtle()
        
        penc.clear()
        wn.bgcolor('lightblue')
        #wn.bgpic("sidcloud.gif")

        global x
        x=1.4

        
        
        day_turtle=turtle.Turtle()
        night_turtle=turtle.Turtle()
        day_turtle.shape('circle')
        day_turtle.color('yellow')
        day_turtle.penup()
        day_turtle.shapesize(0.7,0.7)
        day_turtle.up()
        day_turtle.setposition(-270,255)

        night_turtle.color('black')
        night_turtle.shape('square')
        night_turtle.shapesize(0.7,0.7)
        night_turtle.penup()
        night_turtle.up()
        night_turtle.setposition(-270,278)
        
        start_turtle=turtle.Turtle()
        pause_turtle=turtle.Turtle()





        start_turtle.color('green')
        start_turtle.shape('square')
        start_turtle.shapesize(0.7,1,5)
        start_turtle.penup()
        start_turtle.setposition(-130,280)

        pause_turtle.color('red')
        pause_turtle.shape('square')
        pause_turtle.shapesize(0.7,1,5)
        pause_turtle.penup()
        pause_turtle.setposition(20,280)
        h=turtle.Turtle()
        h.up()
        h.setposition(-230,270)
        h.down()
        h.hideturtle()
        h.penup()
        h.color("blue")
        h.write("Continue", False, align="left", font=("Courier", 14, "bold"))

        h.up()
        h.setposition(-50,270)
        h.color("blue")
        h.write("Pause", False, align="left", font=("Courier", 14, "bold"))







        global p
        p=0
        global n
        n=0



        cpen=turtle.Turtle()


        obj = turtle.Turtle()
        obj.penup()
        obj2=turtle.Turtle()
        obj2.penup()

        obj.shape('square')
        obj.shapesize(4,5,4)
                
        obj2.shape('square')
        obj2.color('brown')
        obj2.shapesize(0.5,6,2)
        obj.color('grey')
        obj.setposition(400,-240)        
        obj2.up()
        obj2.setposition(obj.xcor(),obj.ycor()+40)
        obj.hideturtle()
        obj2.hideturtle()


        global score
        score=0
        cpen.penup()
        cpen.speed(0)
        cpen.hideturtle()
        cpen.setposition(70,290)
        scorestring="Distance : %s m"%score
        cpen.write(scorestring,False,align = "left",font=("Arial",14,"bold"))

        score_pen = turtle.Turtle()
        score_pen.hideturtle()
        score_pen.speed(0)


        
        score_pen.up()
        score_pen.color('black')
        score_pen.setposition(-370,270)
        score_pen.write("Nightmode ",False,align="left",font=("Arial",11,"bold"))
        score_pen.up()
        score_pen.color('yellow')
        score_pen.setposition(-370,245)
        score_pen.write("Daymode ",False,align="left",font=("Arial",11,"bold"))
        


        brush = turtle.Turtle()
        brush.up()
        brush.setposition(-400,-325)
        brush.down()

        brush.begin_fill()
        brush.fillcolor('green')
        brush.forward(800)
        brush.left(90)
        brush.forward(100)
        brush.left(90)
        brush.pencolor('green')
        brush.forward(800)
        brush.pencolor('black')
        brush.left(90)
        brush.forward(100)
        brush.end_fill()
        brush.hideturtle()

        l=turtle.Turtle()
        l.shape('square')
        l.shapesize(0.2,40)
        l.color('black')
        l.up()
        l.goto(0,230)
        
        #upper_boundary

        brush.up()
        brush.setposition(-400,230)
        brush.down()
        brush.setheading(0)
        brush.width(5)
        brush.color("black")
        brush.forward(798)
        brush.left(90)
        brush.forward(98)
        brush.left(90)
        brush.fd(798)
        brush.lt(90)
        brush.fd(98)
        
        #bar1
        bar1=turtle.Turtle()
        bar1.shape('square')
        bar1.shapesize(8,3)
        bar1.color('black')
        bar1.penup()
        bar1.setposition(-100,149)

        #bar1.speed(0)
        bar1.setheading(180)

        #bar2
        bar2 = turtle.Turtle()
        bar2.shape('square')
        bar2.shapesize(6,3)
        bar2.color('black')
        bar2.penup()
        bar2.setposition(100,-166)

        bar2.setheading(180)

        #bar3

        bar3 = turtle.Turtle()
        bar3.shape('square')
        bar3.shapesize(9,3)
        bar3.color('black')
        bar3.penup()
        bar3.setposition(300,140)

        bar3.setheading(180)

        #bar4
        bar4 = turtle.Turtle()
        bar4.shape('square')
        bar4.shapesize(8,3)

        bar4.penup()
        bar4.setposition(-300,-145)
        bar4.color('black')
        bar4.setheading(180)


        #creating helicopter
        #---------------------------------------------------

        heli = turtle.Turtle()
        heli.shape('square')
        heli.shapesize(0.7,1,8)
        heli.penup()
        heli.color('darkblue')

        tail = turtle.Turtle()
        tail.shape('square')
        tail.shapesize(0.2,1,4)
        tail.penup()
        tail.setposition(heli.xcor()-25,heli.ycor())
        tail.color('darkblue')
        tail2 = turtle.Turtle()
        tail2.penup()
        tail2.shape('square')
        tail2.shapesize(0.4,0.2)
        tail2.setposition(tail.xcor()-10,tail.ycor()+6)
        tail2.color('darkblue')
        pos="stop"

        bit = turtle.Turtle()
        bit.shape('square')
        bit.shapesize(0.2,0.4)
        bit.penup()
        bit.setposition(heli.xcor(),heli.ycor()+12)
        bit.color('darkblue')

        fan=turtle.Turtle()
        fan.shape('square')
        fan.penup()
        fan.shapesize(0.1,2)
        fan.setposition(bit.xcor(),bit.ycor()+4)

        head = turtle.Turtle()
        head.shape('circle')
        head.color('darkblue')
        head.penup()
        head.setposition(heli.xcor()+10,heli.ycor())

        dot1=turtle.Turtle()
        dot1.color('white')
        dot1.penup()
        dot1.shape('circle')
        dot1.shapesize(0.1,0.1)
        dot1.setposition(heli.xcor()+1,heli.ycor())

        dot2=turtle.Turtle()
        dot2.color('white')
        dot2.penup()
        dot2.shape('circle')
        dot2.shapesize(0.1,0.1)
        dot2.setposition(heli.xcor()+8,heli.ycor())

        dot3=turtle.Turtle()
        dot3.color('white')
        dot3.penup()
        dot3.shape('circle')
        dot3.shapesize(0.1,0.1)
        dot3.setposition(heli.xcor()+15,heli.ycor())



        #-----------------------------------------------

        def gobar(x,y):
            # winsound.PlaySound("helicopter-hovering-01.wav",winsound.SND_ASYNC+winsound.SND_LOOP+winsound.SND_PURGE)
            global heli_mode
            heli_mode='start'
            start_turtle.color('darkgreen')
            
             
                
        def stop(x,y):
            pause_turtle.color('yellow')
            global heli_mode
            heli_mode='stop'
           #winsound.PlaySound(None,winsound.SND_PURGE+winsound.SND_ASYNC)

        def goup():
            
            
            heli.sety(heli.ycor()+9)

        def day(x,y):
            #winsound.PlaySound("shoot-type.wav",winsound.SND_ASYNC)
            """
            wn.bgpic("sidcloud.gif")
            """
            wn.bgcolor('lightblue')
            bar1.color("black")
            bar2.color("black")
            l.color('black')
            bar3.color("black")
            bar4.color("black")
            cpen.color("black")
            fan.color('black')
            
            
            
        def night(x,y):
            """
            #winsound.PlaySound("shoot-type.wav",winsound.SND_ASYNC)
            wn.bgpic("darkcloud.gif")
            """
            wn.bgcolor('black')
            bar1.color("red")
            bar2.color("red")
            l.color('white')
            bar3.color("red")
            bar4.color("red")
            cpen.color("white")
            fan.color('white')
            h.color('white')
            brush.color('white')
            
            
        def start_unglow(x,y):
            start_turtle.color('green')

        def pause_unglow(x,y):
            pause_turtle.color('red')


        turtle.listen()
        start_turtle.onclick(gobar)
        start_turtle.onrelease(start_unglow)
      
        pause_turtle.onclick(stop)
        pause_turtle.onrelease(pause_unglow)
        turtle.onkeypress(goup,"space")
        day_turtle.onclick(day)
        night_turtle.onclick(night)


        while True:
            wn.update()
            
            if heli_mode =='start':
                
                score=score+1
                cpen.clear()
                scorestring="Distance : %s m"%score
                cpen.write(scorestring,False,align = "left",font=("Arial",14,"bold"))
                c=heli.ycor()
                c=c-x
                heli.sety(c)
                tail.sety(c)
                v=tail.ycor()+6
                tail2.sety(v)
                head.sety(heli.ycor())
                dot1.sety(heli.ycor())
                dot2.sety(heli.ycor())
                dot3.sety(heli.ycor())
                z=heli.ycor()+13
                bit.sety(z)
                j=bit.ycor()+4
                fan.sety(j)

                obj.setx(obj.xcor()-n)
                obj2.sety(obj.ycor()+40)
                obj2.setx(obj.xcor())
                    
                bar1.setx(bar1.xcor()-p)
                bar2.setx(bar2.xcor()-p)
                bar3.setx(bar3.xcor()-p)
                bar4.setx(bar4.xcor()-p)
            

            if bar4.xcor() < -420:
                bar4.setposition(400,-145)
                
            if bar1.xcor() < -420:
                bar1.setposition(350,150)
                
            if bar2.xcor() < -420:
                bar2.setposition(350,-166)
            if bar3.xcor() < -420:
                bar3.setposition(350,140)

            
            
            if heli.xcor() < bar1.xcor() +55 and heli.xcor() > bar1.xcor()- 40 and heli.ycor() < bar1.ycor() +90 and heli.ycor() > bar1.ycor()-90:
                
                time.sleep(2)
                wn.clear()
                wn.bgcolor('lightblue')
                
                cpen.up()
                cpen.color('red')
                cpen.setposition(-200,0)
                cpen.write("Distance travelled : %s m" %score,False,align="left",font=("Courier",20,"bold"))
                        
                cpen.hideturtle()
                cpen.setposition(-200,40)
                cpen.write("Game Over !!",False,align="left",font=("Courier",20,"bold"))
                time.sleep(5)
                cpen.clear()
                wn.clear()
                choose_mode(again)

                break
              

                

            if heli.xcor() < bar2.xcor() +55 and heli.xcor() > bar2.xcor()- 40 and heli.ycor() < bar2.ycor() +70 and heli.ycor() > bar2.ycor()-60:
                
                time.sleep(2)
                wn.clear()
                
                wn.bgcolor('lightblue')
                cpen.up()
                cpen.color('red')
                cpen.setposition(-200,0)
                cpen.write("Distance travelled : %s m" %score,False,align="left",font=("Courier",20,"bold"))
                        
                cpen.hideturtle()
                cpen.setposition(-200,40)
                cpen.write("Game Over !!",False,align="left",font=("Courier",20,"bold"))
                time.sleep(5)
                cpen.clear()
                wn.clear()
                choose_mode(again)

                break
              

            if heli.xcor() < bar3.xcor() +55 and heli.xcor() > bar3.xcor()- 40 and heli.ycor() < bar3.ycor() +90 and heli.ycor() > bar3.ycor()-105:
                time.sleep(2)
                wn.clear()
                wn.bgcolor('lightblue')
                
                cpen.up()
                cpen.color('red')
                cpen.setposition(-200,0)
                cpen.write("Distance travelled : %s m" %score,False,align="left",font=("Courier",20,"bold"))
                        
                cpen.hideturtle()
                cpen.setposition(-200,40)
                cpen.write("Game Over !!",False,align="left",font=("Courier",20,"bold"))
                time.sleep(3)
                cpen.clear()
                choose_mode(again)

                break
                
            if heli.xcor() < bar4.xcor() +55 and heli.xcor() > bar4.xcor()- 40 and heli.ycor() < bar4.ycor() +80 and heli.ycor() > bar4.ycor()-90:
            
                time.sleep(2)
                wn.clear()
                wn.bgcolor('lightblue')
                
                cpen.up()
                cpen.color('red')
                cpen.setposition(-200,0)
                cpen.write("Distance travelled : %s m" %score,False,align="left",font=("Courier",20,"bold"))
                        
                cpen.hideturtle()
                cpen.setposition(-200,40)
                cpen.write("Game Over !!",False,align="left",font=("Courier",20,"bold"))
                time.sleep(5)
                cpen.clear()
                choose_mode(again)

                break
            if heli.ycor() <-250:
                time.sleep(2)
                wn.clear()
                wn.bgcolor('lightblue')
                
                cpen.up()
                cpen.color('red')
                cpen.setposition(-200,0)
                cpen.write("Distance travelled : %s m" %score,False,align="left",font=("Courier",20,"bold"))
                        
                cpen.hideturtle()
                cpen.setposition(-200,40)
                cpen.write("Game Over !!",False,align="left",font=("Courier",20,"bold"))
                time.sleep(5)
                cpen.clear()
                choose_mode(again)

                break
                
            if heli.ycor() > 210:
               
                heli.sety(210)
            
              
            if score <=1000:
                p=4
            if score>1000:
                p=5

            if score>2000:
                p=6


            if score >2500:
              
                n=5
                p=3
                obj.showturtle()
                obj2.showturtle()
                
                
                if obj.xcor()==heli.xcor():
                    if heli.xcor() > obj.xcor():
                        heli.setx(obj.xcor())

                    if heli.ycor()>200:
                        heli.sety(200)
                        
                    
                    p=0
                    n=0
                
                bar1.setposition(-1000,0)
                bar2.setposition(-1000,0)
                bar3.setposition(-1000,0)
                bar4.setposition(-1000,0)
                    
                x=1.4
                cpen.clear()
                cpen.up()
                cpen.hideturtle()
                
                cpen.setposition(1000,1000)
                gpen=turtle.Turtle()
                gpen.hideturtle()
                
                if p==0 and n==0:
                    
                    if heli.ycor()<-185:
                        heli.sety(-185)
                        gpen.up()
                        gpen.setposition(-25,-285)
                        gpen.write("H",False,align="left",font=("Arial",50,"bold"))

                       # winsound.PlaySound(None,winsound.SND_PURGE)
                        time.sleep(2)
                        wn.clear()
                        wn.bgcolor('lightblue')
                        cpen.up()
                        cpen.color('blue')
                        cpen.setposition(-200,0)
                        cpen.write("Distance travelled : 2500 m",False,align="left",font=("Courier",20,"bold"))
                        
                        cpen.hideturtle()
                        cpen.setposition(-200,40)
                        cpen.write("Level 1 Compeleted",False,align="left",font=("Courier",20,"bold"))
                        time.sleep(3)
                        cpen.clear()
                        
                        choose_mode(again)

                        break
              
     

    def choose_mode(opt):
        global heli_mode
        """
        wn.bgpic('heli_logo.gif')
        """
        heli_mode="stop"
        opt=turtle.Turtle()
        opt.shape('triangle')
        opt.shapesize(1.2,1.2,6)
        opt.color('blue')
        opt.up()
        opt.setposition(40,-100)
        
        
        
        

        
        penc.hideturtle()
        penc.up()
        penc.color('black')
        
        penc.setposition(69,-120)
        penc.write("START GAME",False,align="left",font=("AR CHRISTY",25,"bold"))
        penc.up()
        penc.setposition(69,-160)

        penc.write("ABOUT PROGRAMMER",False,align="left",font=("AR CHRISTY",25,"bold"))
        penc.up()
        penc.setposition(69,-200)
        penc.color('red')
        penc.write("EXIT",False,align="left",font=("AR CHRISTY",25,"bold"))

        
        

        def down():
            
            #winsound.PlaySound('pause.wav',winsound.SND_ASYNC+winsound.SND_PURGE)
            opt.sety(opt.ycor()-40)

        def up():
            #winsound.PlaySound('pause.wav',winsound.SND_ASYNC+winsound.SND_PURGE)
            opt.sety(opt.ycor()+40)

        
        def menu():
            wn.tracer(0)
        
            if opt.ycor()==-100:
               # winsound.PlaySound("shoot-type.wav",winsound.SND_ASYNC)
                penc.clear()
                opt.up()
                opt.setposition(500,500)
                start_game()
            
            
            elif opt.ycor()==-140:
                #winsound.PlaySound("shoot-type.wav",winsound.SND_ASYNC)
                about()
                penc.clear()

            elif opt.ycor()==-180:
                #winsound.PlaySound("shoot-type.wav",winsound.SND_ASYNC)
                ex()
                

        turtle.listen()
        
        turtle.onkey(up,'Up')
        turtle.onkey(down,'Down')
        turtle.onkey(menu,"\n")
        
        
        
          
        

        
          

        while True:
            wn.update()
            

            if opt.ycor() < -180:
                opt.sety(-100)

            if opt.ycor() >-100:
                opt.sety(-180)
            

            
    def main():
        
        sid.hideturtle()
        choose_mode(sid)
        mainloop()

    main()


#-----------------

turtle.listen()
turtle.onkey(change,"\n")

while True:
    wn.update()

    if pos=='load':
        load_pen.setx(load_pen.xcor()+0.07)
        
    if load_pen.xcor()>=240:
        load_pen.setx(240)
        load_pen.hideturtle()
        load_pen.clear()
        start_game()
