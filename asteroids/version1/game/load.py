import math
import random
import pyglet
from .phisical_object import PhysicalObject
from . import resources


def distance(p1=(0, 0), p2=(0, 0)):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def asteroids(num_asteroids, player_position, batch=None):
    asteroids = []
    for i in range(num_asteroids):
        asteroid_x, asteroid_y = player_position
        while distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)

        new_asteroid = PhysicalObject(
            img=resources.asteroid_img, x=asteroid_x, y=asteroid_y, batch=batch
        )

        new_asteroid.rotation = random.randint(0, 360)
        new_asteroid.velocity_x = random.random()*40
        new_asteroid.velocity_y = random.random()*40
        asteroids.append(new_asteroid)

    return asteroids


def player(batch=None):
    return PhysicalObject(img=resources.player_img, x=400, y=300, batch=batch)