from features.tuples import *

class Projectile:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        return


class Environment:
    def __init__(self, gravity, wind):
        self.wind = wind
        self.gravity = gravity
        return


def tick(env, proj):
    position = proj.position + proj.direction
    direction = proj.direction + env.gravity + env.wind
    return Projectile(position, direction)

def ground(proj):
    if proj.position.y <= 0:
        return True
    else:
        return False



pos = Point(0, 1, 0)
dir = Vector(1, 1, 0)
dir_norm = dir.normalize()
p = Projectile(pos, dir_norm)

grav = Vector(0, -0.1, 0)
wind = Vector(-0.01, 0, 0)
e = Environment(grav, wind)


while not ground(p):
    print(p.position)
    p_next = tick(e, p)
    p = p_next

print(p.position)






