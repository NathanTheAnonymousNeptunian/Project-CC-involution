import pgzrun
import pgzero
HEIGHT = 600
WIDTH = 450
TITLE = "Project CCI"
FPS = 30
may = Actor("maymc")
def draw():
    screen.fill("white")
    may.draw()
pgzrun.go()