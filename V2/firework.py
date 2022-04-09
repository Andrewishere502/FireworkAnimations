import pygame

from charge import Charge


class Firework:
    def __init__(self, location, size, color, fuse_length, charges, name):
        self.location = location
        self.size = size
        self.color = color

        self.lit = False
        self.dead = False
        self.fuse_size = [2, 6 + self.size[1]]
        self.fuse_location = [self.location[0] + self.size[0] // 2 - self.fuse_size[0] // 2,
                              self.location[1] - self.fuse_size[1] + self.size[1]
                                ]
        self.fuse_length = fuse_length
        self.reduce_fuse_by = self.fuse_size[1] / self.fuse_length
        self.charges = charges
        self.lit_charges = []

        self.name = name
        return

    @staticmethod
    def charge_location(location, size):
        location = [location[0] + size[0] / 2 - 2,  # -2 is half a charge size
                    location[1] + size[1]
                    ]
        return location

    def draw_fuse(self, win):
        pygame.draw.rect(win, (200, 200, 200), (*self.fuse_location, *self.fuse_size))
        if self.lit:
            pygame.draw.rect(win, (255, 162, 0), (*self.fuse_location, self.fuse_size[0], 2))
        return

    def draw_fuse_outline(self, win):
        location = self.fuse_location[0] - 1, self.fuse_location[1] - 1
        size = self.fuse_size[0] + 2, self.fuse_size[1] + 2
        pygame.draw.rect(win, (0, 0, 0), (location, size), 1)
        return

    def draw_body(self, win):
        pygame.draw.rect(win, (self.color), (*self.location, *self.size))
        return

    def draw_body_outline(self, win):
        location = self.location[0] - 1, self.location[1] - 1
        size = self.size[0] + 2, self.size[1] + 2
        pygame.draw.rect(win, (0, 0, 0), (location, size), 1)
        return

    def draw_charges(self, win):
        for charge in self.lit_charges:
            if not charge.exploded:
                pygame.draw.rect(win, charge.color, (*charge.location, 5, 5))
            if getattr(charge, "particles", False):
                self.draw_particles(win, charge.particles, charge.color)
        return

    def draw_particles(self, win, particles, color):
        for particle in particles:
            x, y = particle
            pygame.draw.rect(win, (color), (x, y, 2, 2))
        return

    def draw(self, win):
        self.draw_fuse_outline(win)
        self.draw_body_outline(win)
        self.draw_fuse(win)
        self.draw_charges(win)
        self.draw_body(win)
        return

    def light(self):
        self.lit = True
        return

    def reduce_fuse(self):
        if self.fuse_length == 0:
            self.dead = True
            self.lit = False
        self.fuse_size[1] -= self.reduce_fuse_by
        self.fuse_location[1] += self.reduce_fuse_by
        return

    def launch_at_length(self):
        inds_to_remove = []
        for i in range(len(self.charges)):
            launch_length, charge = self.charges[i]
            if launch_length == self.fuse_length:
                charge.light()
                self.lit_charges.append(charge)
                inds_to_remove.append(i)

        for i in inds_to_remove:
            self.charges.pop(i)
        return

    def control_lit_charges(self):
        dead_charges_i = []
        for i in range(len(self.lit_charges)):
            charge = self.lit_charges[i]
            if charge.tick_life == 0:
                charge_dead = charge.explode()
                if charge_dead:
                    dead_charges_i.append(i)
            else:
                charge.fly()
        
        for i in dead_charges_i:
            self.lit_charges.pop(i)
        return

    def fuse_tick(self):
        if self.lit and self.fuse_size[1] > 0:
            self.fuse_length -= 1
            self.reduce_fuse()
            self.launch_at_length()
        self.control_lit_charges()
        return
