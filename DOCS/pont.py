from genieCivilOuvrage2D import *
from turtle import *
if __name__=="__main__":
    setup(1366,768)
    speed(600)
    
setpos(-255,0)
speed(0)
pencolor('blue')
pensize(3)
pendown()
ellipse(400)
left(90)
forward(400)
penup()
setpos(0, 0)
pendown()
forward(400)
#deuxieme
setpos(145,0)

ellipse(400)
left(90)
forward(400)
penup()
setpos(35, 0)
pendown()
forward(500)
setpos(545, 0)

#troisieme
pendown()
ellipse(400)
left(90)
forward(350)
penup()
# setpos(60, 0)
#socle
setpos(-196, 0)

fillcolor('blue')
begin_fill()
pendown()
left(270)
forward(15)
right(270)
forward(15)

left(270)
forward(30)
right(90)
forward(150)

left(270)
forward(30)
right(90)
forward(15)


left(180)
# forward(30)
right(90)
forward(15)
end_fill()
penup()
#deuxieme socle
setpos(205, 0)
pendown()
fillcolor('blue')
begin_fill()
pendown()
left(180)
forward(15)
right(270)
forward(15)

left(270)
forward(30)
right(90)
forward(150)

left(270)
forward(30)
right(90)
forward(15)

left(180)
right(90)
forward(15)
end_fill()

#triangle second ellipse
left(-25)
forward(98)
penup()
setpos(80,0)

left(25)
pendown()
forward(144)
setpos(80,0)

left(25)
pendown()
forward(212)

right(-155)
pendown()
forward(194)

right(180)
penup()
forward(192)

left(155)
pendown()
forward(212)

right(155)
pendown()
forward(196)
penup()

left(180)
forward(195)

left(210)
pendown()
forward(176)
penup()

right(-150)
pendown()
forward(150)
penup()

left(210)
pendown()
forward(96)
penup()

# triangle premier ellipse
setpos(-320, 0)
right(60)
pendown()
forward(93)
penup()


left(180)
forward(93)

right(150)
pendown()
forward(141)
penup()
right(180)
forward(141)

right(155)
pendown()
forward(212)

right(205)
pendown()
forward(192)
penup()
left(180)

forward(196)

right(205)
pendown()
forward(213)
pendown()

right(155)
forward(190)
penup()

right(180)
forward(190)

left(210)
pendown()
forward(174)
penup()

right(-150)
pendown()
forward(152)
penup()

left(210)
pendown()
forward(98)
penup()

# troisieme triangle

setpos(480, 0)
right(60)
pendown()
forward(93)
penup()


left(180)
forward(93)

right(150)
pendown()
forward(141)
penup()
right(180)
forward(141)

right(155)
pendown()
forward(212)

right(205)
pendown()
forward(192)
penup()
left(180)

forward(196)

right(205)
pendown()
forward(213)
pendown()

right(155)
forward(190)
penup()

right(180)
forward(190)

left(210)
pendown()
forward(172)
penup()

right(-150)
pendown()
forward(152)
penup()

left(210)
pendown()
forward(98)
penup()


turtle.done()
