from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
import math
import pygame
def draw_cir1( r = .3 , xc = 0 , yc = 0 ,begin = 0 , end = 2):
    glPointSize(4)
    glBegin(GL_POINTS)
    glColor3f(0,0,0)
    for theta in np.arange(begin, end*math.pi, .001):
        x = r * math.cos(theta) + xc
        y = r * math.sin(theta) + yc
        glVertex(x, y)
    glEnd()

    glFlush()

def draw_cir8( r = .3 , xc = 0 , yc = 0 ,begin = 0 , end = 2):
    glBegin(GL_POLYGON)
    glColor3f(0.643,0.702,0.725)
    for theta in np.arange(begin, end*math.pi, .001):
        x = r * math.cos(theta) + xc
        y = r * math.sin(theta) + yc
        glVertex(x, y)
    glEnd()

    glFlush()

def draw_cir7( r = .3 , xc = 0 , yc = 0 ,begin = 0 , end = 2):
    glBegin(GL_POLYGON)
    glColor3f(0.839,0.859,0.894)
    for theta in np.arange(begin, end*math.pi, .001):
        x = r * math.cos(theta) + xc
        y = r * math.sin(theta) + yc
        glVertex(x, y)
    glEnd()

    glFlush()

def draw_cir6( r = .3 , xc = 0 , yc = 0 ,begin = 0 , end = 2):

    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3f(0,0,0)
    for theta in np.arange(begin, end*math.pi, .001):
        x = r * math.cos(theta) + xc
        y = r * math.sin(theta) + yc
        glVertex(x, y)
    glEnd()

    glFlush()
def draw_cir4( r = .3 , xc = 0 , yc = 0 ,begin = 0 , end = 2):
    glColor3f(0.773,0.890, 0.918)
    glPointSize(3)
    glBegin(GL_POLYGON)
    for theta in np.arange(begin, end*math.pi, .001):
        x = r * math.cos(theta) + xc
        y = r * math.sin(theta) + yc
        glVertex(x, y)
    glEnd()

    glFlush()

def draw_cir5( r = .3 , xc = 0 , yc = 0 ,begin = 0 , end = 2):
    glColor3f(0.145, 0.275, 0.454)
    glPointSize(3)
    glBegin(GL_POINTS)
    for theta in np.arange(begin, end*math.pi, .001):
        x = r * math.cos(theta) + xc
        y = r * math.sin(theta) + yc
        glVertex(x, y)
    glEnd()

    glFlush()
def draw_cir2( r = .3 , xc = 0 , yc = 0):


    glBegin(GL_POLYGON)
    glColor3f(.88,0,0)
    for theta in np.arange(0, 2*3.14, .001):
        x = r * math.cos(theta) + xc
        y = r * math.sin(theta) + yc
        glVertex(x, y)
    glEnd()

    glFlush()

def draw_cir3( r = .3 , xc = 0 , yc = 0):

    glBegin(GL_POLYGON)
    glColor3f(0.145, 0.275, 0.454)
    for theta in np.arange(0, 2*3.14, .001):
        x = r * math.cos(theta) + xc
        y = r * math.sin(theta) + yc
        glVertex(x, y)
    glEnd()

    glFlush()

def body():
    glColor3f(0.984, 0.812, 0.302)
    glBegin(GL_POLYGON)
    glVertex(0.5, -0.55)
    glVertex(0.5, 0.35)
    glVertex(-0.5, 0.35)
    glVertex(-0.5, -0.55)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3f(0.984, 0.812, 0.302)
    glVertex(-0.5, 0.35)
    glVertex(-0.45, 0.4)
    glVertex(0.45, 0.4)
    glVertex(0.5, 0.35)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3f(0.984, 0.812, 0.302)
    glVertex(-0.5, -0.55)
    glVertex(-0.45, -0.6)
    glVertex(0.45,- 0.6)
    glVertex(0.5, -0.55)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0,0,0)

    glVertex(0.5, -0.55)
    glVertex(0.5, 0.35)
    glVertex(-0.5, 0.35)
    glVertex(-0.5, -0.55)

    glVertex(-0.5, 0.35)
    glVertex(-0.45, 0.4)
    glVertex(0.45, 0.4)
    glVertex(0.5, 0.35)

    glVertex(-0.5, -0.55)
    glVertex(-0.45, -0.6)
    glVertex(0.45,- 0.6)
    glVertex(0.5, -0.55)

    glVertex(-0.45, 0.4)
    glVertex(0.45, 0.4)

    glVertex(-0.45, -0.6)
    glVertex(0.45, -0.6)

    glVertex(-.5 ,.2 )
    glVertex(.5 ,.2 )

    glVertex(-.3 , .4)
    glVertex(-.3 , .2)

    glVertex(-.1 , .4)
    glVertex(-.1 , .2)

    glVertex(.3 , .4)
    glVertex(.3 , .2)

    glVertex(.0 , .35)
    glVertex(.25 , .35)
    glVertex(.25 , .35)
    glVertex(.25 , .25)
    glVertex(.25 , .25)
    glVertex(.0 , .25)
    glVertex(.0 , .25)
    glVertex(.0 , .35)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5294117647,0.80784313725,1)
    glVertex(.0 , .35)
    glVertex(.25 , .35)
    glVertex(.25 , .25)
    glVertex(.0 , .25)
    glEnd()
    glFlush()
def draw_neck():
    glPopMatrix()
    glLineWidth(3)
    glBegin(GL_LINES)
    glColor3f(0,0,0)
    glVertex(-.08 , .6)
    glVertex(.08 , .6)
    glVertex(.08 , .6)
    glVertex(.08,0)
    glVertex(-.08 , .6)
    glVertex(-.08,0)
    glVertex(-.08 , .6)
    glVertex(.08 , .6)

    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.984, 0.812, 0.302)
    glVertex(-.08,0)
    glVertex(-.08 , .6)
    glVertex(.08 , .6)
    glVertex(.08 , .6)
    glVertex(.08,0)
    glVertex(-.08 , .6)
    glEnd()
    glLoadIdentity
    glPushMatrix()
    glFlush()
def draw_neck2():
    glBegin(GL_POLYGON)
    glColor3f(0.984, 0.812, 0.302)
    glVertex(-.06 , .74)
    glVertex(.06 , .74)
    glVertex(.06,.6)
    glVertex(-.06,0.6)
    glVertex(.06 , .74)
    glVertex(.06,.6)
    glVertex(-.06 , .74)
    glVertex(-.06,0.6)
    glEnd()
    glBegin(GL_LINES)
    glColor3f(0,0,0)
    glVertex(-.06 , .74)
    glVertex(.06 , .74)
    glVertex(.06,.6)
    glVertex(-.06,0.6)
    glVertex(.06 , .74)
    glVertex(.06,.6)
    glVertex(-.06 , .74)
    glVertex(-.06,0.6)
    glVertex(.08,.6)
    glVertex(-.08,0.6)


    glEnd()
    glFlush()
def draw_legs1():
    glBegin(GL_POLYGON)
    glColor3f(.5 , .5 , .5)
    glVertex(.9, -.4)
    glVertex(.63 , -.4)
    glVertex(.63 ,-.75 )
    glVertex(.9 ,-.75 )
    glEnd()
    glBegin(GL_LINES)
    glColor3f(0,0,0)
    glVertex(.9, -.4)
    glVertex(.63 , -.4)
    glVertex(.63 , -.4)
    glVertex(.63 ,-.75 )
    glVertex(.63 ,-.75 )
    glVertex(.9 ,-.75 )
    glVertex(.9 ,-.75 )
    glVertex(.9 ,-.4 )


    glVertex(.9, -.45)
    glVertex(.63 , -.45)
    glVertex(.63 ,-.6 )
    glVertex(.9 ,-.6 )
    glVertex(.63, -.55)
    glVertex(.9, -.55)
    glVertex(.63, -.5)
    glVertex(.9, -.5)
    glVertex(.63, -.7)
    glVertex(.9, -.7)
    glVertex(.63, -.65)
    glVertex(.9, -.65)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    glVertex(.4, -.45)
    glVertex(.1, -.45)
    glVertex(.1, -.6)
    glVertex(.4, -.6)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.5, 0.5)
    glVertex(.5, -.45)
    glVertex(.55, -.45)
    glVertex(.55, -.45)
    glVertex(.55, -.57)
    glVertex(.55, -.57)
    glVertex(.52, -.6)
    glVertex(.52, -.6)
    glVertex(.52, -.66)
    glVertex(.52, -.66)
    glVertex(.45, -.66)
    glVertex(.45, -.66)
    glVertex(.42, -.63)
    glVertex(.42, -.63)
    glVertex(.42, -.6)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.5, 0.5)
    glVertex(.55, -.48)
    glVertex(.63, -.48)
    glVertex(.63, -.48)
    glVertex(.63, -.52)
    glVertex(.63, -.52)
    glVertex(.55, -.52)

    glEnd()
    glFlush()


def draw_legs2():
    glBegin(GL_POLYGON)
    glColor3f(.5 , .5 , .5)
    glVertex(-.9, -.4)
    glVertex(-.63 , -.4)
    glVertex(-.63 ,-.75 )
    glVertex(-.9 ,-.75 )
    glEnd()
    glBegin(GL_LINES)
    glColor3f(0,0,0)

    glVertex(-.9, -.4)
    glVertex(-.63 , -.4)
    glVertex(-.63 , -.4)
    glVertex(-.63 ,-.75 )
    glVertex(-.63 ,-.75 )
    glVertex(-.9 ,-.75 )
    glVertex(-.9 ,-.75 )
    glVertex(-.9 ,-.4 )


    glVertex(-.9, -.45)
    glVertex(-.63 , -.45)
    glVertex(-.63 ,-.6 )
    glVertex(-.9 ,-.6 )
    glVertex(-.63, -.55)
    glVertex(-.9, -.55)
    glVertex(-.63, -.5)
    glVertex(-.9, -.5)
    glVertex(-.63, -.7)
    glVertex(-.9, -.7)
    glVertex(-.63, -.65)
    glVertex(-.9, -.65)

    glEnd()

    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    glVertex(.4, -.45)
    glVertex(.1, -.45)
    glVertex(.1, -.6)
    glVertex(.4, -.6)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.5, 0.5)
    glVertex(-.5, -.45)
    glVertex(-.55, -.45)
    glVertex(-.55, -.45)
    glVertex(-.55, -.57)
    glVertex(-.55, -.57)
    glVertex(-.52, -.6)
    glVertex(-.52, -.6)
    glVertex(-.52, -.66)
    glVertex(-.52, -.66)
    glVertex(-.45, -.66)
    glVertex(-.45, -.66)
    glVertex(-.42, -.63)
    glVertex(-.42, -.63)
    glVertex(-.42, -.6)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.5, 0.5)
    glVertex(-.55, -.48)
    glVertex(-.63, -.48)
    glVertex(-.63, -.48)
    glVertex(-.63, -.52)
    glVertex(-.63, -.52)
    glVertex(-.55, -.52)

    glEnd()
    glFlush()


def hand1():
    glColor3f(0,0,0)
    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)
    glVertex(.3 , .36)
    glVertex(.3 , .4)
    glVertex(.3 , .4)
    glVertex(.45 , .4)
    glVertex(.45 , .4)
    glVertex(.45 , .36)
    glVertex(.45 , .36)
    glVertex(.3 , .36)
    glEnd()
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3f(.5,.5,.5)
    glVertex(.3 , .36)
    glVertex(.3 , .4)
    glVertex(.3 , .4)
    glVertex(.45 , .4)
    glVertex(.45 , .4)
    glVertex(.45 , .36)
    glVertex(.45 , .36)
    glVertex(.3 , .36)
    glEnd()
    glPopMatrix()


    glBegin(GL_POLYGON)
    glColor3f(0.773,0.890, 0.918)
    glVertex(.3 , .38)
    glVertex(.3 , .44)
    glVertex(.3 , .44)
    glVertex(.34 , .44)
    glVertex(.34 , .44)
    glVertex(.34 , .32)
    glVertex(.34 , .32)
    glVertex(.3 , .32)
    glVertex(.3 , .32)
    glVertex(.3 , .3)
    glEnd()

    glPushMatrix()
    glTranslate(0,-.12,0)
    glBegin(GL_POLYGON)
    glColor3f(0.773,0.890, 0.918)
    glVertex( .5,.4 )
    glVertex( .5,.48 )
    glVertex( .5,.48 )
    glVertex( .3,.48 )
    glVertex( .3,.48 )
    glVertex( .3,.4 )
    glVertex( .3,.4 )
    glVertex( .5,.4 )
    glEnd()
    glPopMatrix()

    glBegin(GL_POLYGON)
    glColor3f(0.773,0.890, 0.918)
    glVertex( .5,.4 )
    glVertex( .5,.48 )
    glVertex( .5,.48 )
    glVertex( .3,.48 )
    glVertex( .3,.48 )
    glVertex( .3,.4 )
    glVertex( .3,.4 )
    glVertex( .5,.4 )
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0,0,0)
    glVertex( .5,.4 )
    glVertex( .5,.48 )
    glVertex( .5,.48 )
    glVertex( .3,.48 )
    glVertex( .3,.48 )
    glVertex( .3,.4 )
    glVertex( .3,.4 )
    glVertex( .5,.4 )
    glEnd()


    glPushMatrix()
    glTranslate(0,-.12,0)
    glBegin(GL_LINES)
    glColor3f(0,0,0)
    glVertex( .5,.4 )
    glVertex( .5,.48 )
    glVertex( .5,.48 )
    glVertex( .3,.48 )
    glVertex( .3,.48 )
    glVertex( .3,.4 )
    glVertex( .3,.4 )
    glVertex( .5,.4 )
    glEnd()
    glPopMatrix()

    glBegin(GL_LINES)
    glColor3f(0,0,0)
    glVertex(.3 , .36)
    glVertex(.3 , .4)
    glVertex(.3 , .4)
    glVertex(.45 , .4)
    glVertex(.45 , .4)
    glVertex(.45 , .36)
    glVertex(.45 , .36)
    glVertex(.3 , .36)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0,0,0)
    glVertex(.3 , .38)
    glVertex(.3 , .44)
    glVertex(.3 , .44)
    glVertex(.34 , .44)
    glVertex(.34 , .44)
    glVertex(.34 , .32)
    glVertex(.34 , .32)
    glVertex(.3 , .32)
    glVertex(.3 , .32)
    glVertex(.3 , .3)
    glEnd()
    glFlush()
def addition_LinesAndShapes():
    glColor3f(0,0,0)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex(.08 ,.45 )
    glVertex(-.08 ,.45 )
    glVertex(.08 ,.55 )
    glVertex(-.08 ,.55 )
    glVertex(.06 , .74)
    glVertex(.1 , .82)
    glVertex(.1 , .82)
    glVertex(.1 , .88)
    glVertex(.1 , .88)
    glVertex(-.06 , .88)
    glVertex(-.06 , .74)
    glVertex(-.1 , .82)
    glVertex(-.1 , .82)
    glVertex(-.1 , .88)
    glVertex(-.1 , .88)
    glVertex(-.06 , .88)
    glEnd()


    glBegin(GL_POLYGON)
    glColor3f(0.984, 0.812, 0.302)
    glVertex(.06 , .74)
    glVertex(.1 , .82)
    glVertex(.1 , .82)
    glVertex(.1 , .88)
    glVertex(.1 , .88)
    glVertex(-.06 , .88)
    glVertex(-.06 , .74)
    glVertex(-.1 , .82)
    glVertex(-.1 , .82)
    glVertex(-.1 , .88)
    glVertex(-.1 , .88)
    glVertex(-.06 , .88)
    glEnd()
    glFlush()
def draw():
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.5,0.5,0.5)
    glLineWidth(4)
    glBegin(GL_LINES)
    glVertex(1,-0.535)
    glVertex(-1,-.535)

    glVertex(.3,-0.6)
    glVertex(.1,-.6)

    glVertex(-.3,-0.6)
    glVertex(-.1,-.6)

    glVertex(.1,-0.67)
    glVertex(-.1,-.67)
    glEnd()
    glPushMatrix()
    glScale(.7,.7,.7)


    glPushMatrix()
    glTranslate(0 , -.2 , 0 )
    draw_neck()
    addition_LinesAndShapes()
    draw_legs2()
    draw_neck2()
    draw_legs1()
    body()

    glPopMatrix()

    glPopMatrix()

    glPushMatrix()
    glTranslate(-.7 , -.4 , 0)
    hand1()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.7 , -.4 , 0)
    glRotate(180 , 0 ,1 ,0)
    hand1()
    glPopMatrix()

    draw_cir6(.036,-.28 , .2)
    draw_cir2(.027,-.28 , .2)
    glPushMatrix()
    glTranslate(0.2 , 0 , 0)
    draw_cir4(.055 ,-.14 , .64 , begin= .3, end=1.35)
    draw_cir4(.085 , -0.07 , .56, begin=math.pi , end=2.5)
    draw_cir5(.055 ,-.14 , .64 , begin= .3, end=1.35)
    draw_cir5(.085 , -0.07 , .56, begin=math.pi , end=2.5)
    draw_cir1(.08 , -.1 , .6)
    draw_cir3(.076 , -.1 , .6)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-.2 , 0 ,0)
    glRotate(180 , 0 , 1 ,0)
    draw_cir4(.055 ,-.14 , .64 , begin= .3, end=1.35)
    draw_cir4(.085 , -0.07 , .56, begin=math.pi , end=2.5)
    draw_cir5(.055 ,-.14 , .64 , begin= .3, end=1.35)
    draw_cir5(.085 , -0.07 , .56, begin=math.pi , end=2.5)
    draw_cir1(.08 , -.1 , .6)
    draw_cir3(.076 , -.1 , .6)
    glPopMatrix()
    draw_cir7(.02 , .12 , .625)
    draw_cir7(.02 ,- .08 , .625)

    draw_cir8(.013 , .07 , .59)
    draw_cir8(.013 , -.13 , .59)


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE)
glutInitWindowSize(500, 500)
glutCreateWindow(b'test')
glutDisplayFunc(draw)                            # Initialize our window.
glutMainLoop()