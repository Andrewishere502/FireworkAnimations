import random
from math import cos, sin, pi


class Charge:
    def __init__(self, location, color, vel, max_height, num_particles, particle_vel, particle_life):
        self.location = location
        self.color = color
        self.vel = vel
        self.tick_life = max_height / vel

        self.num_particles = num_particles
        self.particle_vel = particle_vel
        self.particle_life = particle_life
        self.lit = False
        self.exploded = False
        return

    def light(self):
        self.lit = True
        return

    def fly(self):
        if self.tick_life > 0:
            self.location[1] -= self.vel
            self.tick_life -= 1
        return

    def explode(self):
        has_particles = getattr(self, "particles", False)
        if not has_particles:
            self.particles = [self.location.copy() for i in range(self.num_particles)]
        else:
            self.exploded = True
            angle = 2 * pi
            angle_per = angle / self.num_particles
            move_x = lambda i: self.particle_vel * cos(angle_per * i)
            move_y = lambda i: self.particle_vel * sin(angle_per * i)
            for i in range(len(self.particles)):
                self.particles[i][0] -= move_x(i)
                self.particles[i][1] -= move_y(i)
            if self.particle_life > 0:
                self.particle_vel = self.particle_vel**0.95
                self.particle_life -= 1
                return False
            else:
                return True
