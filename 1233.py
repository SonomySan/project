import pygame
import os
import sys
import random

FPS = 50
pygame.init()
size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Перемещение героя")
clock = pygame.time.Clock()
size_im = 50, 50


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except:
        print('файл {} не найден'.format(name))
        exit()

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Перемещение героя", "",
                  "Герой двигается",
                  "Карта на месте",
                  "Доведите героя до финиша, но помните:",
                  "Наступать на пушистиков негуманно!"]

    fon = pygame.transform.scale(load_image('fon.png'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


def load_level(filename):
    try:
        level_map = [line.strip() for line in filename]
        max_width = max(map(len, level_map))
        return list(map(lambda x: x.ljust(max_width, '.'), level_map))
    except:
        print(---3)
        sys.exit()


lvl1 = ['...@......#......#..',
        '..##.#.####..##.##..',
        '.##..###..#..#......',
        '##........####...#..',
        '#.#...#.........##..',
        '###..###..#####..###',
        '..#..#....#.#......#',
        '.##.##.#.##.##.....#',
        '.#......##......####',
        '.#.....##...###.....',
        '.###.###...#..#.....',
        '..#...........#.....',
        '.#######......#.#.#.',
        '.......#.........##.',
        '.......#..##.....#..',
        '.......#...#...##...',
        '..#......##.###..#..',
        '#####....#.......#..',
        '....######.##.#..#..',
        '.$..................']

lvl2 = ['..#.....@....#.#....',
        '#.#.####.#####.#..#.',
        '#....#.......#.#....',
        '#####..#####.#.#..#.',
        '#..#...#.....#.#....',
        '#.##.###.....#.#..#.',
        '#.#..#.#...###.#..#.',
        '#.#####.#..#..#.#..##',
        '#.#..#.....#......#.',
        '#.##.#...#....#####.',
        '#.#..#####........#.',
        '#.##.#.#.###..#...#.',
        '#..........#..#...#.',
        '#######.#..####.###.',
        '#...#.#.#.........#.',
        '#.#.#.###.#.########.',
        '#.#.#...#.#.......#.',
        '#.#.#.#########.###.',
        '#.#................$',
        '#####################']

lvl3 = ['.....@..........#...',
        '###.###.#####.#.###.',
        '....#.......#.#...#.',
        '..#######.#.###.###.',
        '..#.......#.#...#...',
        '..###.###.#.#####...',
        '..#...#.#.#.....#.##',
        '#####.#.###.....#.#.',
        '..#...#.....#####.#.',
        '..#####.............',
        '........###.#...####',
        '.#..#.....#.#.......',
        '##.##...###.#.#####.',
        '.#..#...#.#.#...#...',
        '.#..#.###.#####.###.',
        '....#.#...#.......#.',
        '#.###.###.#.###.###.',
        '....#...#.#.#.#...#.',
        '.#..#####.#.#.#####.',
        '.#........#.#......$']

lvl4 = ['....#....@....#...#.',
        '.#..#########.#.###.',
        '.#...#.#......#...#.',
        '.#####.#..#######.#.',
        '.#.#......#...#...#.',
        '.#.#..#####.#.#.#.#.',
        '.#..........#...#...',
        '.###.#.##########.##',
        '.....#......#.....#.',
        '.#.#.#......#.#.###.',
        '.#.#.#......#.#.....',
        '.#.############.###.',
        '.#.......#....#.#...',
        '.#.#######.######.##',
        '.#.......#......#...',
        '.####.#..###.#..#...',
        '..#.#.#......#..###.',
        '..#.#.###..###..#.#.',
        '###.#...#....#..#.#.',
        '#...#...#.........#$']

lvl5 = ['@...#.......#.......',
        '.##.###.###.#####.#.',
        '..#...#.#.....#...#.',
        '..#.#.###.#.###.###.',
        '..#.#.....#.#...#.#.',
        '..#.###...###.###.#.',
        '....#.###.#...#.....',
        '###.....#.#.###.###.',
        '........#.#.......#.',
        '###.#####.#...#.#.##',
        '..#.#.#.......#.#...',
        '..#.....#.#...#.###.',
        '..#.....#.#...#.#.#.',
        '..#.###.#####.#.#.#.',
        '......#...#.......#.',
        '..#####.###.....###.',
        '......#...#...#...#.',
        '..#########.###...##',
        '......#.............',
        '#######.####..####$#']

lvl6 = ['@.#.......#...#.....',
        '..###.###.#.###.####',
        '....#.#...#.#.#.....',
        '###.###.#.#.#.#####.',
        '..#...#.#.#...#...#.',
        '..###.#.#####.#.###.',
        '..#...#.......#.....',
        '..#.#########.#.#.##',
        '..#.....#.....#.#.#.',
        '..#.###.#.###.#.###.',
        '....#.#...#...#.....',
        '..###.#.###.#####.##',
        '..#...#.#.#.#.......',
        '..###.###.#.#.......',
        '......#.............',
        '##.#..#######.......',
        '...#....#...#.......',
        '.#####..###.#####.#.',
        '...#......#.......#$',
        '####################']

my_level = load_level(random.choice([lvl1, lvl2, lvl3, lvl4, lvl5, lvl6]))  # Сюда добавить названия других уровней
tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png'),
    'end': load_image('end.jpg')
}
player_image = load_image('mario.png', -1)
tile_width = tile_height = 50
player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = pygame.transform.scale(tile_images[tile_type], size_im)
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.pos = (pos_x, pos_y)
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)

    def move(self, x, y):
        self.pos = (self.pos[0] + x, self.pos[1] + y)


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '$':
                Tile('end', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


player, level_x, level_y = generate_level(my_level)
running = True
start_screen()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        key = pygame.key.get_pressed()
        x = player.pos[0]
        y = player.pos[1]
        if key[pygame.K_LEFT]:
            if (my_level[y][x - 1] != '#') and ((x - 1) >= 0):
                player.rect.x -= tile_width
                player.move(-1, 0)
        elif key[pygame.K_RIGHT]:
            if x + 1 < len(my_level[y]):
                if (my_level[y][x + 1] != '#') and ((x + 1) <= max(list(map(len, my_level)))):
                    player.rect.x += tile_width
                    player.move(1, 0)
        elif key[pygame.K_UP]:
            if (my_level[y - 1][x] != '#') and ((y - 1) >= 0):
                player.rect.y -= tile_height
                player.move(0, -1)
        elif key[pygame.K_DOWN]:
            if (y + 1) < len(my_level):
                if my_level[y + 1][x] != '#':
                    player.rect.y += tile_height
                    player.move(0, 1)
        if my_level[y][x] == '$':
            running = False
    pygame.display.flip()
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    tiles_group.draw(screen)
    player_group.draw(screen)

while True:  # Концовка
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 100)
    text = font.render("You win!!!", True, (255, 255, 255))
    screen.blit(text, (480, 480))
    pygame.display.flip()
