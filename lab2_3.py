#!/usr/bin/env python3

# ścieżka do interpretera shebang

# losowość kolorów i deformacja 

# załadowanie bibliotek
import sys
import random

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

# funkcje pomocnicze docelowo raz wykonywane
def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0) # a to ustawia kolor bufora

# placeholder
def shutdown():
    pass

def narysujProstokatPls(x, y, a, b, d, r, g, bl):
    a=a*d # nie wiem czy o to chodziło 
    glColor3f(r, g, bl)
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y) # origin point
    glVertex2f(x, y+a)
    glVertex2f(x+b, y)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(x+b, y+a) # origin point
    glVertex2f(x, y+a)
    glVertex2f(x+b, y)
    glEnd()

# rysuje pojedynczą klatkę
# ma być szybko bez zbędnych obliczeń
def render(time, r, g, bl):
    glClear(GL_COLOR_BUFFER_BIT) # czyszczenie ramki w pamięci

    narysujProstokatPls(-50, -50, 60, 70, 2, r, g, bl)

    glFlush()  # pamięć wysyłamy do wyświetlenia

# przekształca przedział rysowania na [-100; 100]dla X i Y
# domyślnie jest [-1;1]
# to wywołujemy w startupie i po makecontextcurrent w mainie
def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit(): # inicjujemy bibliotekę GLFW
        sys.exit(-1) # jak się nie uda to wyjebuje

    # tworzymy okienko 
    window = glfwCreateWindow(400, 400, __file__, None, None) # wymiary, nazwa tytuł, i coś jeszcze
    if not window:
        glfwTerminate()
        sys.exit(-1) # jak nie zadziała to wyjebuje

    # określa miejsce aktywnego obecnie kontekstu opengl
    glfwMakeContextCurrent(window) # czyli że chyba nasz kontekst wrzucamy w to okno co stowrzyliśmy
    # można stworzyć wiele okien i je przełączać
    # aktualny kontekst przenosimy do innego okna?

    # updejtujemy obszar rysowania na fajniejszy
    glfwSetFramebufferSizeCallback(window, update_viewport)

    # włącza synchronizachę pionową czyli nie wiem co, ogranicza szybkość funkcji swap buffer    
    glfwSwapInterval(1)

    startup()
    
    # jak tu daje random to kolor się zmienia przy kolejnym odpalaniu programu
    # można dać to w funkcji narysujprostokątpls to wtedy robi rave bo sie od nowa losują kolorki przy kazdym rysowaniu okna
    r=random.random() # to daje float między 0 i 1 czyli to czego potrzebujemy do funkcji glColor3f
    g=random.random()
    bl=random.random()
    # powtarzamy aż do zamknięcia okna
    while not glfwWindowShouldClose(window):
        render(glfwGetTime(), r, g, bl) # nie ruszaj to sie renderuje, podmieniamy ramki obrazu
        
        # przetwarzanie zaistniałych okien i wejść i guess
        glfwSwapBuffers(window) 
        
        glfwPollEvents() # czemu nie wait events
    shutdown()

    glfwTerminate()

# python high wtajemniczenie moment
if __name__ == '__main__':
    main()


