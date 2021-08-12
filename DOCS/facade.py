from genieCivilOuvrage2D import *
from turtle import *
if __name__=="__main__":
    setup(1366,768)
    speed(600)

    
    #Rectangle pieds de la maison  
                    
    deplacer(-350,-250)
    rectangle(800,10)
    #Fin rectangle pieds
    
    #rectangle gauche
    fillcolor('light grey')
    begin_fill()
    deplacer(-350,-240)
    rectangle(320,400)
    end_fill()
    #fin rectangle gauche

    #fenetre 1 2 3 gauche
    deplacer(-335,-230)
    fillcolor('grey')
    begin_fill()
    rectangle(75,375)
    end_fill()
    deplacer(-235,-230)
    fillcolor('grey')
    begin_fill()
    rectangle(75,375)
    end_fill()
    deplacer(-135,-230)
    fillcolor('grey')
    begin_fill()
    rectangle(75,375)
    end_fill()
    #fin fenetre 1 2 3 gauche

    #contenu fenetre 1
    deplacer(-328,-220)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    deplacer(-298,-220)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    deplacer(-328,-135)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    deplacer(-298,-135)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    deplacer(-328,35)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    deplacer(-298,35)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    deplacer(-328,80)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    deplacer(-298,80)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    #contenu fenetre 1

    #contenu fenetre 2
    deplacer(-228,-220)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    deplacer(-198,-220)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    deplacer(-228,-135)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    deplacer(-198,-135)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    deplacer(-228,35)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    deplacer(-228,80)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    deplacer(-198,80)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    deplacer(-198,35)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    #fin contenu fenetre 2
    #contenu fenetre 3
    deplacer(-128,-220)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    deplacer(-98,-220)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    deplacer(-98,-135)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    deplacer(-128,-135)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    deplacer(-128,35)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    deplacer(-128,80)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    deplacer(-98,80)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    deplacer(-98,35)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    
    #fin contenu fenetre 3

    #rectangle droite
    fillcolor('light grey')
    begin_fill()
    deplacer(125,-240)
    rectangle(325,400)
    end_fill()

    #fenetre 1 2 3
    deplacer(150,-230)
    fillcolor('grey')
    begin_fill()
    rectangle(75,375)
    end_fill()
    deplacer(255,-230)
    fillcolor('grey')
    begin_fill()
    rectangle(75,375)
    end_fill()
    deplacer(355,-230)
    fillcolor('grey')
    begin_fill()
    rectangle(75,375)
    end_fill()
    #fin fenetre 1 2 3
    #contenu 1 2 3
    #contenu 1
    deplacer(157,-220)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    deplacer(157,-135)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    deplacer(187,-135)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    deplacer(187,-220)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    #petit contenu 1
    deplacer(157,35)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    deplacer(157,80)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    deplacer(187,80)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    deplacer(187,35)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    #petit contenu 1
    #fin contenu 1
    #contenu 2
    deplacer(262,-220)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    deplacer(262,-135)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    deplacer(292,-220)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    deplacer(292,-135)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    #petit contenu 2
    deplacer(262,35)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    deplacer(262,80)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    deplacer(292,35)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    deplacer(292,80)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    #fin petit contenu 2
    #fin contenu 2
    #contenu 3
    deplacer(362,-220)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    deplacer(362,-135)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    deplacer(392,-135)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    deplacer(392,-220)
    fillcolor('white')
    begin_fill()
    rectangle(30,85)
    end_fill()
    #petit contenu 3
    deplacer(362,35)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    deplacer(362,80)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    deplacer(392,35)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    deplacer(392,80)
    fillcolor('white')
    begin_fill()
    rectangle(30,45)
    end_fill()
    #fin petit contenu 3
    #fin contenu 3
    #fin rectangle droite 

   

    # toit 1 2 3
    deplacer(-230,198)
    rectangle(160,50)
    deplacer(-70,198)
    rectangle(240,50)
    deplacer(170,198)
    rectangle(160,50)
    # fin toit 1 2 3

    #trapeze du toit
    deplacer(-350,160)
    begin_fill()
    fillcolor('light grey')
    rt(210)
    fd(75)
    rt(150)
    fd(930)
    rt(-210)
    fd(75)
    #rt(30)
    #fd(800)
    
    end_fill()
    #fin trapeze du toit
    
    # triangle 1 2 du toit
    deplacer(-230,248)
    fillcolor('limegreen')
    begin_fill()
    rt(180)
    fd(100)
    rt(65)
    fd(91)
    end_fill()

    deplacer(170,248)
    fillcolor('limegreen')
    pensize(2)
    begin_fill()
    lt(65)
    fd(100)
    rt(65)
    fd(91)

    end_fill()
    # fin triangle 1 2 du toit
    
    #trait du toit
    deplacer(-144,298)
    penup()
    lt(35)
    fd(400)
    #fin trait

    #1 petit rectangle
    deplacer(-210,198)
    rectangle(15,40)
    deplacer(-195,198)
    rectangle(15,40)
    #fin petit rectangle

    #2 petit rectangle
    deplacer(-170,198)
    rectangle(15,40)
    deplacer(-155,198)
    rectangle(15,40)

    # fin petit rectangle

    #3 petit rectangle
    deplacer(-125,198)
    rectangle(15,40)
    deplacer(-110,198)
    rectangle(15,40)

    #fin petit rectangle

    #4 petit rectangle 
    deplacer(-60,198)
    rectangle(15,40)
    deplacer(-45,198)
    rectangle(15,40)

    #fin petit rectangle

    #5 petit rectangle
    deplacer(-15,198)
    rectangle(15,40)
    deplacer(0,198)
    rectangle(15,40)

    # fin petit rectangle

    # 6 petit rectangle
    deplacer(30,198)
    rectangle(15,40)
    deplacer(45,198)
    rectangle(15,40)

    # fin petit rectangle

    # 7 petit rectangle
    deplacer(75,198)
    rectangle(15,40)
    deplacer(90,198)
    rectangle(15,40)

    # fin petit rectangle

    # 8 petit rectangle
    deplacer(120,198)
    rectangle(15,40)
    deplacer(135,198)
    rectangle(15,40)

    # fin petit rectangle
    # 9 petit rectangle
    deplacer(185,198)
    rectangle(15,40)
    deplacer(200,198)
    rectangle(15,40)

    # fin petit rectangle
    # 10 petit rectangle
    deplacer(230,198)
    rectangle(15,40)
    deplacer(245,198)
    rectangle(15,40)

    # fin petit rectangle

    # 11 petit rectangle
    deplacer(275,198)
    rectangle(15,40)
    deplacer(290,198)
    rectangle(15,40)

    # fin petit rectangle
    #porte en color
    deplacer(-10,148)
    fillcolor('light grey')
    begin_fill()
    rectangle(115,-275)
    end_fill()
    #fin porte en color
    #partie gauche  de la porte
    deplacer(-30,148)
    rectangle(10,-275)
    deplacer(-20,148)
    rectangle(10,-275)
    deplacer(-30,-127)
    rectangle(40,-10)
    deplacer(-30,-137)
    rectangle(10,-103)
    #fin partie gauche porte

    #partie droite de la porte
    deplacer(105,148)
    rectangle(10,-275)
    deplacer(115,148)
    rectangle(10,-275)
    deplacer(82,-127)
    rectangle(43,-10)
    deplacer(115,-137)
    rectangle(10,-103)
    #fin partie doite

    #escalier
    deplacer(9,-127)
    rectangle(72,-10)
    deplacer(5,-137)
    rectangle(80,-10)
    deplacer(3,-147)
    rectangle(85,-10)
    deplacer(1,-157)
    rectangle(90,-10)
    deplacer(-2,-167)
    rectangle(95,-10)
    deplacer(-4,-177)
    rectangle(100,-10)
    deplacer(-6,-187)
    rectangle(105,-10)
    deplacer(-8,-197)
    rectangle(110,-10)
    deplacer(-10,-207)
    rectangle(115,-10)
    deplacer(-12,-217)
    rectangle(120,-10)
    deplacer(-15,-227)
    rectangle(125,-12)
    #fin escalier

    # devant porte
    deplacer(9,-127)
    fillcolor('white')
    begin_fill()
    rectangle(36,65)
    end_fill()
    deplacer(45,-127)
    fillcolor('white')
    begin_fill()
    rectangle(36,65)
    end_fill()
    deplacer(9,-62)
    fillcolor('white')
    begin_fill()
    rectangle(36,65)
    end_fill()
    deplacer(45,-62)
    fillcolor('white')
    begin_fill()
    rectangle(36,65)
    end_fill()
    deplacer(45,64)
    dot(30,'black')
    deplacer(45,90)
    fillcolor('white')
    begin_fill()
    rectangle(36,45)
    end_fill()
    deplacer(9,90)
    fillcolor('white')
    begin_fill()
    rectangle(36,45)
    end_fill()
    deplacer(80,3)
    seth(95)
    demicercle(36)
    #fin devant porte
   
    penup()
    goto(-144,298)
    pendown()
    pensize(1)
    fillcolor('limegreen')
    begin_fill()
    rt(310)
    fd(91)
    rt(325)
    pensize(1.5)
    fd(240)
    pensize(1.4)
    rt(328)
    fd(98)
    rt(212)
    fd(400)
    end_fill()
    #continuite des triangles
    deplacer(-230,247)
    pensize(1.5)
    rt(180)
    forward(159)
    deplacer(168,246)
    forward(160)
    #fin des triangles
    #rectangle en bas du toit
    fillcolor('white')
    begin_fill()
    deplacer(-60,198)
    rectangle(210,-50)
    end_fill()
    # fin rectangle en bas du toit
    penup()
    done()

