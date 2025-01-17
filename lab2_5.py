#!/usr/bin/env python3
import sys
from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *
from random import *
import random

val = random.random()
mouseX, mouseY = 1.0, 1.0

def mouse_callback(window, button, action, mods):
    global mouseX, mouseY
    if button == GLFW_MOUSE_BUTTON_LEFT and action == GLFW_PRESS:
        mouseX, mouseY = glfwGetCursorPos(window)  # Pobierz współrzędne kursora
        print(f"Kliknięto w: x={mouseX}, y={mouseY}")


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.2, 0.2, 0.2, 1.0)


def shutdown():
    pass


def render(time):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3ub(69, 235, 9)
    random.seed(val)
    run(0,0)
    glFlush()


def run(x,y):
    global mouseX, mouseY
    
    a1=-0.67; a2=0.4+mouseX/100;  a3=-0.40; a4=-0.10
    b1=-0.02; b2=0.4+mouseX/100;  b3=-0.4;  b4=0.0
    d1=-0.18; d2=-0.1+mouseY/100; d3=-0.1;  d4=0.44
    e1=0.81;  e2=0.4+mouseY/100;  e3=0.4;   e4=0.44
    f1=10;    f2=0;    f3=0;     f4=-2   
    c=0
    
    n = 5000
    for n in range(n):
        temp = randint(1,4)  # losowanie zmiennej
        if temp == 1:
            x = a1*x+b1*y+c
            y = d1*x+e1*y+f1
        elif temp == 2:
            x = a2*x+b2*y+c
            y = d2*x+e2*y+f2
        elif temp == 3:
            x = a3*x+b3*y+c
            y = d3*x+e3*y+f3
        else:
            x = a4*x+b4*y+c
            y = d4*x+e4*y+f4
                              
        glPointSize(2) #rozmier piksela czy cuś
        glBegin(GL_POINTS)
        glVertex2f(x,y)
        glEnd()       


def update_viewport(window, width, height):
    if height == 0:
        height = 1
    if width == 0:
        width = 1
    aspectRatio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, -50, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-45.0, 45.0, -45.0 / aspectRatio, 45.0 / aspectRatio,
                1.0, -1.0)
    else:
        glOrtho(-45.0 * aspectRatio, 45.0 * aspectRatio, -45.0, 45.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# main robi brr
def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    # zbieranie akcji myszki
    glfwSetMouseButtonCallback(window, mouse_callback) 
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()
    glfwTerminate()


if __name__ == '__main__':
    main() 