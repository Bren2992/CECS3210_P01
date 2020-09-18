from graphics import *
from random import*


def printInfo():
    print("This program simulates a throw of two dices and the user has to predict the value.")
    print("Rules: You must guess the numbers both dices will have to win the game.")
    
def getInputs():
    a = int(input("Which number will have dice #1 (1-6)?"))
    b = int(input("Which number will have dice #2 (1-6)?"))
    return a,b
        
def main():
    printInfo()
    a, b = getInputs()

    win = GraphWin("Dice Game", 300, 300)
    win.setBackground("purple")
    
    dice1 = Rectangle(Point(70,70), Point(20,20))
    dice1.setFill("blue4")
    dice1.draw(win)

    dice2 = Rectangle(Point(140,140),Point(90,90))
    dice2.setFill("blue4")
    dice2.draw(win)

    #Display message
    t = Text(Point(130,10), ("Click to roll dice: "))
    t.setFace("times roman")
    t.setSize(16)
    t.setStyle("bold")
    t.setTextColor("white")
    t.draw(win)
    
    ####DOTS FOR UPPER DICE:

    #Dot 1: Upper left corner
    c1 = Point(30,30)
    d1 = Circle(c1, 5)
    d1.setFill("yellow")
    #d1.draw(win)

    #Dot 2:Bottom right corner
    c2 = Point(60,60)
    d2 = Circle(c2, 5)
    d2.setFill("yellow")
    #d2.draw(win)

    #Dot 3: Middle 
    c3 = Point(45,46)
    d3 = Circle(c3, 5)
    d3.setFill("yellow")
    #d3.draw(win)

    #Dot 4: Upper right corner
    c4 = Point(62,30)
    d4 = Circle(c4, 5)
    d4.setFill("yellow")
    #d4.draw(win)

    #Dot 5: Bottom left corner
    c5 = Point(30, 60)
    d5 = Circle(c5, 5)
    d5.setFill("yellow")
    #d5.draw(win)

    #Dot 6: Middle left
    c6 = Point(30,45)
    d6 = Circle(c6,5)
    d6.setFill("yellow")
    #d6.draw(win)

    #Dot 7: Middle right
    c7 = Point(60, 45)
    d7 = Circle(c7, 5)
    d7.setFill("yellow")
    #d7.draw(win)

    ###DOTS FOR BOTTOM DICE:

    #Dot 1: Upper left corner
    c_1 = Point(100,100)
    d_1 = Circle(c_1, 5)
    d_1.setFill("yellow")
    #d_1.draw(win)

    #Dot 2:Bottom right corner
    c_2 = Point(130,130)
    d_2 = Circle(c_2, 5)
    d_2.setFill("yellow")
    #d_2.draw(win)

    #Dot 3: Middle 
    c_3 = Point(115,115)
    d_3 = Circle(c_3, 5)
    d_3.setFill("yellow")
    #d_3.draw(win)

    #Dot 4: Upper right corner
    c_4 = Point(130,100)
    d_4 = Circle(c_4, 5)
    d_4.setFill("yellow")
    #d_4.draw(win)

    #Dot 5: Bottom left corner
    c_5 = Point(100, 130)
    d_5 = Circle(c_5, 5)
    d_5.setFill("yellow")
    #d_5.draw(win)

    #Dot 6: Middle left
    c_6 = Point(100,115)
    d_6 = Circle(c_6,5)
    d_6.setFill("yellow")
    #d_6.draw(win)

    #Dot 7: Middle right
    c_7 = Point(130, 115)
    d_7 = Circle(c_7, 5)
    d_7.setFill("yellow")
    #d_7.draw(win)

    #Loops for Upper random dice
    win.getMouse()
    R = randint(1,6)
    if R == 1:
        win.getMouse()
        d3.draw(win)   
    elif R == 2:
        win.getMouse()
        d1.draw(win)
        d2.draw(win)   
    elif R == 3:
        win.getMouse()
        d4.draw(win)
        d3.draw(win)
        d5.draw(win)   
    elif R == 4:
        win.getMouse()
        d1.draw(win)
        d4.draw(win)
        d5.draw(win)
        d2.draw(win)
    elif R == 5:
        win.getMouse()
        d1.draw(win)
        d4.draw(win)
        d3.draw(win)
        d5.draw(win)
        d2.draw(win)
    elif R == 6:
        win.getMouse()
        d1.draw(win)
        d6.draw(win)
        d5.draw(win)
        d4.draw(win)
        d7.draw(win)
        d2.draw(win)

    #Loops for bottom random dice 
    win.getMouse()
    R2 = randint(1,6)
    if R2 == 1:
        win.getMouse()
        d_3.draw(win) 
    elif R2 == 2:
        win.getMouse()
        d_1.draw(win)
        d_2.draw(win) 
    elif R2 == 3:
        win.getMouse()
        d_4.draw(win)
        d_3.draw(win)
        d_5.draw(win)
    elif R2 == 4:
        win.getMouse()
        d_1.draw(win)
        d_4.draw(win)
        d_5.draw(win)
        d_2.draw(win)
    elif R2 == 5:
        win.getMouse()
        d_1.draw(win)
        d_4.draw(win)
        d_3.draw(win)
        d_5.draw(win)
        d_2.draw(win)
    elif R2 == 6:
        win.getMouse()
        d_1.draw(win)
        d_6.draw(win)
        d_5.draw(win)
        d_4.draw(win)
        d_7.draw(win)
        d_2.draw(win)

    #Goodbye Message
    t.undraw()
    t2 = Text(Point(130,10), ("Click in the screen to close program"))
    t2.setFace("times roman")
    t2.setSize(10)
    t2.setStyle("bold")
    t2.setTextColor("white")
    t2.draw(win)

    win.getMouse()
    win.close()
      
main()


    



        

