import pgzrun

WIDTH = 585
# HEIGHT = penguin.height + 50
HEIGHT = 780

alien = Actor('factory')
alien.bottom = 780


def draw():
    screen.clear()
    alien.draw()


def update():
    print(alien.top)
    alien.top += 2
    if alien.top > 0:
        alien.bottom = 780


pgzrun.go()
