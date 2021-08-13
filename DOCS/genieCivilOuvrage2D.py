""" Module pour turtle des fonctions cercle, rectangle, 
triangle, trapeze, carre, polygone, losange, Ellipse, demi-cercle
"""
from turtle import *

def deplacer(x,y):
    up() #relever le crayon
    goto(x, y) # deplacer en haut à gauche
    down() #baisser le crayon
    
def carre(cote):
    """
    Commentaires de spécification
    Bloc carre
    Objectif : Ce bloc permet de dessiner un carre
    Méthode : On dessine un carre avec le module turtle
    Besoins : cote, couleur et couleur2 (la couleur 2 c'est pour une éventuelle couleur de fond)
    Connues : -
    Entrées : -
    Sorties : -
    Résultats : carre
    Hypothèses : -
    """
    for i in range(4) :
        forward(cote)
        left(90)

def cercle(rayon):
    """
    Commentaires de spécification
    Bloc cercle
    Objectif : Ce bloc permet de dessiner un cercle
    Méthode : On dessine un cercle avec le module turtle
    Besoins : rayon, couleur et couleur2 (la couleur 2 c'est pour une éventuelle couleur de fond)
    Connues : -
    Entrées : -
    Sorties : -
    Résultats : cercle
    Hypothèses : -
    """   
    circle(rayon)
  
def demicercle(rayon):
    """
    Commentaires de spécification
    Bloc demi_cercle
    Objectif : Ce bloc permet de dessiner un demi_cercle
    Méthode : On dessine un demi_cercle avec le module turtle
    Besoins : rayon
    Connues : -
    Entrées : -
    Sorties : -
    Résultats : demi_cercle
    Hypothèses : -
    """
    circle(rayon, 180)
  
def rectangle(longueur, largeur):
    """
    Commentaires de spécification
    Bloc rectangle
    Objectif : Ce bloc permet de dessiner un rectangle
    Méthode : On dessine un rectangle avec le module turtle
    Besoins : longueur, largeur, couleur et couleur2 (la couleur 2 c'est pour une éventuelle couleur de fond)
    Connues : -
    Entrées : -
    Sorties : -
    Résultats : rectangle
    Hypothèses : -
    """       
    for i in range(2):
        width(1.5)
        forward(longueur)
        left(90)
        forward(largeur)
        left(90)

def triangle(a,b,c):
    """
    Commentaires de spécification
    Bloc triangle
    Objectif : Ce bloc permet de dessiner un triangle
    Méthode : On dessine un triangle avec le module turtle
    Besoins : cote, couleur et couleur2 (la couleur 2 c'est pour une éventuelle couleur de fond)
    Connues : -
    Entrées : -
    Sorties : -
    Résultats : triangle
    Hypothèses : -
    """
    forward(a)  
    rt(360/3)
    forward(b)
    rt(360/3)  
    forward(c)

def triangleRectangle(LARGEUR, HAUTEUR):
    """ Fonction dessine triangle rectangle python turtle """    
    forward(LARGEUR)  #Avance de d'un tiers de la largeur
    left(90)  #Tourne de 90° à gauche
    forward(HAUTEUR)
    pensize(3)  #Change l'épaisseur du tracé
    home()  #Retourne à la maison     

def polygone(n,cote):
    for i in range(n):
        forward(cote)
        lt(360/n)
 
def losange(cote):
    """
    Commentaires de spécification
    Bloc losange
    Objectif : Ce bloc permet de dessiner un losange
    Méthode : On dessine un losange avec le module turtle
    Besoins : cote
    Connues : -
    Entrées : -
    Sorties : -
    Résultats : losange
    Hypothèses : -
    """    
    for i in range(2):
        forward(cote)
        left(120)
        forward(cote)
        left(60)

def trapeze(cote1,
            cote2,
            cote3,
            cote4,
            couleur,
            couleur2='black'):
    """
    Commentaires de spécification
    Bloc trapeze
    Objectif : Ce bloc permet de dessiner un trapeze
    Méthode : On dessine un trapeze avec le module turtle
    Besoins : cote, couleur et couleur2 (la couleur 2 c'est pour une éventuelle couleur de fond)
    Connues : -
    Entrées : -
    Sorties : -
    Résultats : trapeze
    Hypothèses : -
    """
    color(couleur, couleur2)
    angle1 = 100
    angle2 = 70
    angle3 = 120
    angle4 = 70


    forward(cote1)
    right(angle1)
    forward(cote2)
    right(angle2)
    forward(cote3)
    right(angle3)
    forward(cote4)

def ellipse(r):
    """
    Commentaires de spécification
    Bloc ellipse
    Objectif : Ce bloc permet de dessiner un ellipse
    Méthode : On dessine une ellipse avec le module turtle
    Besoins : rayon
    Connues : -
    Entrées : -
    Sorties : -
    Résultats : ellipse
    Hypothèses : -
    """
    left(90)
    for loop in range(2):
        circle(r/2,90)
