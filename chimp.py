# Adapted from pygame.examples.chimp


# Import Modules
import os
import pygame

if not pygame.font:
    print("Warning, fonts disabled")
if not pygame.mixer:
    print("Warning, sound disabled")

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")


# functions to create our resources
def load_image(name, colorkey=None):
    fullname = os.path.join(data_dir, name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()


def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join(data_dir, name)
    return pygame.mixer.Sound(fullname)


# classes for our game objects
class Fist(pygame.sprite.Sprite):
    """moves a clenched fist on the screen, following the mouse"""

    def __init__(self):
        super().__init__()
        self.image, self.rect = load_image("fist.bmp", -1)
        self.punching = False

    def update(self):
        """move the fist based on the mouse position"""
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.punching:
            self.rect.move_ip(5, 10)

    def punch(self, target):
        """returns true if the fist collides with the target"""
        if not self.punching:
            self.punching = True
            hit_box = self.rect.inflate(-5, -5)
            return hit_box.colliderect(target.rect)

    def un_punch(self):
        """called to pull the fist back"""
        self.punching = False


class Chimp(pygame.sprite.Sprite):
    """moves a monkey critter across the screen. it can spin the
       monkey when it is punched."""

    def __init__(self):
        super().__init__()
        self.image, self.rect = load_image("chimp.bmp", -1)
        self.original_image = self.image
        screen = pygame.display.get_surface()
        self.screen_rect = screen.get_rect()
        self.rect.topleft = 10, 10
        self.speed = 9
        self.rotation_angle = 0

    def update(self):
        """walk or spin, depending on the monkeys state"""
        if self.rotation_angle:
            self._spin()
        else:
            self._walk()

    def _walk(self):
        """move the monkey across the screen, and turn at the ends"""
        if self.rect.left < self.screen_rect.left or self.rect.right > self.screen_rect.right:
            self.speed = -self.speed
            self.image = pygame.transform.flip(self.image, 1, 0)
        self.rect.move_ip((self.speed, 0))

    def _spin(self):
        """spin the monkey image"""
        center = self.rect.center
        self.rotation_angle += 12
        if self.rotation_angle >= 360:
            self.rotation_angle = 0
            self.image = self.original_image
        else:
            self.image = pygame.transform.rotate(self.original_image, self.rotation_angle)
        self.rect = self.image.get_rect(center=center)

    def punched(self):
        """this will cause the monkey to start spinning"""
        if self.rotation_angle == 0:
            self.rotation_angle = 1


def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
    # Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((468, 60))
    pygame.display.set_caption("Monkey Fever")
    pygame.mouse.set_visible(0)

    # Create The background
    background = pygame.Surface(screen.get_size())
    background = background.convert_alpha()
    background.fill((250, 250, 250))

    # Put Text On The Background, Centered
    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render("Pummel The Chimp, And Win $$$", 1, (10, 10, 10))
        text_position = text.get_rect(centerx=background.get_width() / 2)
        background.blit(text, text_position)

    # Prepare Game Objects
    clock = pygame.time.Clock()
    whiff_sound = load_sound("whiff.wav")
    punch_sound = load_sound("punch.wav")
    chimp = Chimp()
    fist = Fist()
    all_sprites = pygame.sprite.RenderPlain((fist, chimp))

    # Main Loop
    running = True
    while running:
        clock.tick(60)

        # Handle Input Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if fist.punch(chimp):
                    punch_sound.play()  # punch
                    chimp.punched()
                else:
                    whiff_sound.play()  # miss
            elif event.type == pygame.MOUSEBUTTONUP:
                fist.un_punch()

        all_sprites.update()

        # Draw Everything
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        pygame.display.update()

    pygame.quit()


# Game Over


# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()
