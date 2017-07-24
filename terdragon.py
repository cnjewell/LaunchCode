#levy c curves
import turtle

def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'X':
        newstr = 'X+YF+'   
    elif ch == 'Y':
        newstr = '−FX−Y'
    else:
        newstr = ch

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == 'X' or cmd == 'Y':
            continue

def main():
    inst = createLSystem(12, "FX")   # create the string
    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()

    t.speed(0)
    t.hideturtle()
    drawLsystem(t, inst, 90, 2)   # draw the picture
                                  # angle 60, segment length 5
    wn.exitonclick()

main()
