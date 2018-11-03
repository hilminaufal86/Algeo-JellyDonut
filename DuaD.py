import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


n = int(input("Banyaknya Titik : "))
print("Masukkan Titik\n")

titik = ()
x = [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

titik = (
    (x[0], x[1], 0),
    (x[2], x[3], 0),
    (x[4], x[5], 0),
    (x[6], x[7], 0),
    (x[8], x[9], 0),
    (x[10], x[11], 0),
    (x[12], x[13], 0),
    (x[14], x[15], 0),
    (x[16], x[17], 0),
    (x[18], x[19], 0)
)


print(titik[0][1])


def Garis() :
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, titik)
    glDrawArrays(GL_POLYGON, 0, 3)
    glDisableClientState(GL_VERTEX_ARRAY)



def main():
    pygame.init()
    display = (500,500)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(100, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Garis()
        pygame.display.flip()
        pygame.time.wait(10)


main()
