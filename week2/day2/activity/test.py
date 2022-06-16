import pygame as pg
from pygame.math import Vector2


class Player(pg.sprite.Sprite):

    def __init__(self, pos,dimensions,*groups):
        super().__init__(*groups)
        self.image = pg.Surface((50, 50), pg.SRCALPHA)
        self.screen = dimensions
        pg.draw.circle(self.image, pg.Color('dodgerblue'), (25, 25), 25)
        self.rect = self.image.get_rect(center=pos)
        self.vel = Vector2(3, 3)
        self.pos = Vector2(pos)

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
        if self.rect.right >= self.screen[0] or self.rect.left <= 0:
            self.vel.x *= -1
        if self.rect.bottom >= self.screen[1] or self.rect.top <= 0:
            self.vel.y *= -1
        


def main():
    pg.init()
    screen = pg.display.set_mode((1000,720))
    # Blit objects with trails onto this surface instead of the screen.
    alpha_surf = pg.Surface(screen.get_size(), pg.SRCALPHA)
    clock = pg.time.Clock()
    all_sprites = pg.sprite.Group()
    player = Player((150, 150),(screen.get_width(),screen.get_height()),all_sprites)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    player.vel.x = 5
                elif event.key == pg.K_a:
                    player.vel.x = -5
                elif event.key == pg.K_w:
                    player.vel.y = -5
                elif event.key == pg.K_s:
                    player.vel.y = 5
            elif event.type == pg.KEYUP:
                if event.key == pg.K_d and player.vel.x > 0:
                    player.vel.x = 0
                elif event.key == pg.K_a and player.vel.x < 0:
                    player.vel.x = 0
                elif event.key == pg.K_w:
                    player.vel.y = 0
                elif event.key == pg.K_s:
                    player.vel.y = 0

        # Reduce the alpha of all pixels on this surface each frame.
        # Control the fade speed with the alpha value.
        alpha_surf.fill((255, 255, 255, 240), special_flags=pg.BLEND_RGBA_MULT)

        all_sprites.update()
        screen.fill((20, 50, 80))  # Clear the screen.
        all_sprites.draw(alpha_surf)  # Draw the objects onto the alpha_surf.
        screen.blit(alpha_surf, (0, 0))  # Blit the alpha_surf onto the screen.
        pg.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
    pg.quit()