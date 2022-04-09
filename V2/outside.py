import pygame

from firework import Firework
from fireworks import OldFaithful, BlueGoblin, RingOfFire


class Outside:
    def __init__(self):
        pygame.display.set_caption("Outside")
        self.width, self.height = 1000, 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont("arial", 20)

        self.button_actions = ("fire", OldFaithful, BlueGoblin, RingOfFire)
        self.buttons = []
        x = 25
        y = 625
        for button in self.button_actions:
            if isinstance(button, str):
                text = button
            else:
                text = button((0, 0)).name
            button_width, button_height = self.font.size(text)
            button = pygame.Rect(x, y, button_width + 10, button_height + 10)
            x += button_width + 25
            self.buttons.append(button)
        self.selected_btn = 0

        self.fireworks = []
        return

    @property
    def selected_firework(self):
        if self.selected_btn != 0:
            return self.button_actions[self.selected_btn]
        else:
            return None

    def clear(self):
        self.win.fill((0, 0, 0))
        return
    
    @staticmethod
    def update():
        pygame.display.update()
        return

    def draw_lower_bar(self):
        self.button_rects = []
        pygame.draw.rect(self.win, (255, 255, 255), (5, 600, self.width - 10, 95))
        for i in range(len(self.buttons)):
            button = self.buttons[i]
            action = self.button_actions[i]

            if i == self.selected_btn:
                pygame.draw.rect(self.win, (89, 140, 217), (button.x - 3, button.y - 3, button.width + 6, button.height + 6), 6)
            rect = pygame.draw.rect(self.win, (217, 89, 89), button)
            self.button_rects.append(rect)

            if isinstance(action, str):
                text = action
            else:
                text = action((0, 0)).name
            self.win.blit(self.font.render(text, True, (255, 255, 255)), (button.x + 5, button.y + 5))
        return

    def pos_in_bar(self, pos):
        return pos[1] > 600

    def clicked_button(self, pos):
        pos_rect = pygame.Rect(*pos, 1, 1)
        return pos_rect.collidelist(self.button_rects)

    def show_potential_firework_placement(self, pos):
        if not self.pos_in_bar(pos) and self.selected_firework != None:
            pos = (pos[0],
                (outside.height
                    - self.selected_firework((0, 0)).size[1]
                    - 100  # account for lower bar height
                    - 1  # account for bottom outline line
                        )
                )
            self.selected_firework(pos).draw(self.win)
        return

    def place_firework(self, pos):
        pos = (pos[0],
            (outside.height
                - self.selected_firework((0, 0)).size[1]
                - 100  # account for lower bar height
                - 1  # account for bottom outline line
                    )
            )
        self.fireworks.append(self.selected_firework(pos))
        return

    def button_up(self, pos):
        if self.pos_in_bar(pos):
            clicked_button = self.clicked_button(pos)
            if clicked_button != -1:
                self.selected_btn = clicked_button
        return

    def button_down(self, pos):
        if not self.pos_in_bar(pos):
            if self.selected_btn != 0:
                self.place_firework(pos)
            else:
                flame_width = 6
                pygame.draw.circle(self.win, (255, 162, 0), pos, flame_width)
                for firework in self.fireworks:
                    x_dis = (firework.fuse_location[0] + firework.fuse_size[0]//2) - pos[0]
                    y_dis = pos[1] - firework.fuse_location[1]
                    # Distance from the mouse pos and the fuse
                    dis = (x_dis**2 + y_dis**2)**0.5
                    if dis <= flame_width:
                        firework.light()
        return

    def tick_cycle(self):
        for firework in self.fireworks:
            firework.draw(self.win)
            if not firework.dead:
                firework.fuse_tick()
        return


pygame.init()

outside = Outside()

run = True
while run:
    pygame.time.delay(10)
    outside.clear()

    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONUP:
            outside.button_up(pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            outside.button_down(pos)

    outside.draw_lower_bar()
    outside.tick_cycle()
    outside.show_potential_firework_placement(pos)
    outside.update()

pygame.quit()
