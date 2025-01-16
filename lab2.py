#!/usr/bin/env python3

# ścieżka do interpretera shebang

# załadowanie bibliotek
import sys

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

# rysuje pojedynczą klatkę
# ma być szybko bez zbędnych obliczeń
def render(time):
    glClear(GL_COLOR_BUFFER_BIT) # czyszczenie ramki w pamięci

    # nadaje kolor trójkątowi
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES) # wskazujemy prymityw do rysowania
    glVertex2f(0.0, 50.0) # umieszczamy wierzchołek w pamięci
    glVertex2f(-50.0, 0.0)
    glVertex2f(50.0, 0.0)
    glEnd()

    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 50.0)
    glVertex2f(-50.0, 0.0)
    glEnd()

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
    # powtarzamy aż do zamknięcia okna
    while not glfwWindowShouldClose(window):
        render(glfwGetTime()) # nie ruszaj to sie renderuje, podmieniamy ramki obrazu
        
        # przetwarzanie zaistniałych okien i wejść i guess
        glfwSwapBuffers(window) 
        
        glfwPollEvents() # czemu nie wait events
    shutdown()

    glfwTerminate()

# python high wtajemniczenie moment
if __name__ == '__main__':
    main()


