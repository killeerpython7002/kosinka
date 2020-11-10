import pygame, random, os, time, copy
from all_card import *

WIDTH = 1000  # ширина игрового окна
HEIGHT = 1000 # высота игрового окна
FPS = 60 # частота кадров в секунду

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (44, 115, 59)
BLUE = (0, 0, 255)

pygame.init()
pygame.mixer.init()  # для звука
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kosinka")
clock = pygame.time.Clock()

move = False
victory = [False, False]
lose = False


class CardDeck(pygame.sprite.Sprite):

    def __init__(self, x, y):
        global all_card
        pygame.sprite.Sprite.__init__(self)

        self.image = pole_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.card_deck = []
        self.card_deck_use = []
        self.group = pygame.sprite.Group()
        self.group_use = pygame.sprite.Group()
        self.give_time = 0
        copy_all_card = copy.copy(all_card)
        while all_card:
            ind = random.randint(0, len(all_card)-1)
            card = all_card.pop(ind)
            self.card_deck.append(Card(x, y, card[1], card[0], card[2], card[3], cover_img))
            self.card_deck[-1].flip()

        self.width = self.card_deck[-1].rect.width
        self.height = self.card_deck[-1].rect.height
        all_card = copy_all_card

    def update(self):
        global cards_group_draw, cards_use_group_draw

        if not move:
            self.give_card()

        if self.card_deck_use:
            self.card_deck_use[-1].update()

        self.card_deck.reverse()
        cards_group_draw.add(self)
        for i in self.card_deck:
            cards_group_draw.add(i)

        self.card_deck.reverse()

        self.card_deck_use.reverse()
        for i in self.card_deck_use:
            cards_use_group_draw.add(i)

        self.card_deck_use.reverse()

    def give_card(self):
        x, y = pygame.mouse.get_pos()
        try:
            if self.give_time < time.time() and x > self.rect.x and x < self.rect.x + self.width and \
                    y > self.rect.y and y < self.rect.y + self.height and pygame.mouse.get_pressed()[0]:

                self.card_deck[-1].rect.x = self.rect.x + self.card_deck[-1].rect.width + 10
                self.card_deck[-1].flip()
                self.card_deck_use.append(self.card_deck.pop(-1))
                self.give_time = time.time() + 0.3

        except:
            if self.give_time < time.time() and x > self.rect.x and x < self.rect.x + self.width and \
                    y > self.rect.y and y < self.rect.y + self.height and pygame.mouse.get_pressed()[0]:
                self.card_deck_use.reverse()
                for i in self.card_deck_use:
                    i.flip()
                    i.rect.x = self.rect.x
                    self.card_deck.append(i)
                self.card_deck_use = []
                self.give_time = time.time() + 0.1


class Card(pygame.sprite.Sprite):

    def __init__(self, x, y, color, nom, price, image, cover):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.image_simple = image
        self.cover = cover
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

        self.color = color
        self.nom = nom
        self.price = price
        self.past_rect = copy.copy(self.rect)
        self.move_I = False
        self.width = self.rect.right - self.rect.left
        self.height = self.rect.bottom - self.rect.top
        self.change = []

    def update(self, list=()):
        self.move(list)

    def flip(self):
        x, y = self.rect.x, self.rect.y
        self.image, self.cover = self.cover, self.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def move(self, list):
        global move, move_group
        if list:
            list.reverse()
        if list and self.image == cover_img:
            return
        if not move and pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            if x > self.rect.left and x < self.rect.right and \
               y > self.rect.top and y < self.rect.bottom:
                self.past_rect = copy.copy(self.rect)
                self.change = [x - self.rect.x, y - self.rect.y]
                move = True
                self.move_I = True
        elif self.move_I:
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                self.rect.x = x - self.change[0]
                self.rect.y = y - self.change[1]
                move_group.add(self)
                y = self.rect.y + 30
                for i in list:
                    i.rect.x = self.rect.x
                    i.rect.y = y
                    y += 30
                    move_group.add(i)
                if not list:
                    reset_1.cheak(self)
                    reset_2.cheak(self)
                    reset_3.cheak(self)
                    reset_4.cheak(self)
                if not self in m_card_deck_1.list:
                    m_card_deck_1.cheak(self, list)
                if not self in m_card_deck_2.list:
                    m_card_deck_2.cheak(self, list)
                if not self in m_card_deck_3.list:
                    m_card_deck_3.cheak(self, list)
                if not self in m_card_deck_4.list:
                    m_card_deck_4.cheak(self, list)
                if not self in m_card_deck_5.list:
                    m_card_deck_5.cheak(self, list)
                if not self in m_card_deck_6.list:
                    m_card_deck_6.cheak(self, list)
                if not self in m_card_deck_7.list:
                    m_card_deck_7.cheak(self, list)
            else:
                self.rect = self.past_rect
                y = self.rect.y + 30
                for i in list:
                    i.rect.x = self.rect.x
                    i.rect.y = y
                    y += 30
                move_group.empty()
                move = False
                self.move_I = False


class Reset(pygame.sprite.Sprite):

    def __init__(self, card_deck, nom):
        pygame.sprite.Sprite.__init__(self)

        self.image = pole_img
        self.list = []
        self.my_group = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = card_deck.rect.x + card_deck.card_deck[-1].rect.width * (nom + 1) + 10 * (nom + 1)
        self.rect.y = card_deck.rect.y
        self.my_price = 0
        self.my_color = None
        self.my_nom = None
        self.reset = [0, None]

        self.width = 111
        self.height = 158

    def draw(self):
        # print([[i.price, i.color, i.nom] for i in self.list])
        if not self.list:
            self.my_price = 0
            self.my_color = None
            self.my_nom = None
        self.list.reverse()
        for i in self.list:
            self.my_group.add(i)

        self.my_group.update()
        self.my_group.empty()
        self.my_group.add(self)

        self.list.reverse()
        for i in self.list:
            self.my_group.add(i)
        for i in self.my_group.sprites():
            if type(i) != Reset:
                print([i.price, i.color, i.nom], end=' ')
            else:
                print("Reset", end=" ")
        print('')

        self.my_group.draw(win)
        self.my_group.empty()

    def update(self, *args):
        pass

    def cheak(self, card):
        global card_deck
        x, y = pygame.mouse.get_pos()
        if move and x > self.rect.left and x < self.rect.right and \
               y > self.rect.top and y < self.rect.bottom:

            if self.my_price == card.price - 1 and self.my_color == card.color and self.my_nom == card.nom:

                self.my_price = card.price

                if card in card_deck.card_deck_use:
                    cardd = card_deck.card_deck_use.pop(card_deck.card_deck_use.index(card))
                    self.list.append(cardd)

                for i in range(1, 5):
                    if eval(f"reset_{i}") != self:
                        reset_i = eval(f"reset_{i}")
                        if card in reset_i.list:
                            cardd = reset_i.list.pop(reset_i.list.index(card))
                            self.list.append(cardd)
                            if reset_i.my_price > 1:
                                reset_i.my_price -= 1
                            else:
                                reset_i.my_price = 0
                                reset_i.my_nom = None
                                reset_i.my_color = None

                for i in range(1, 8):
                    if card in eval(f"m_card_deck_{i}.list"):
                        cardd = eval(f"m_card_deck_{i}.list.pop(m_card_deck_{i}.list.index(card))")
                        self.list.append(cardd)
                        try:
                            if eval(f"m_card_deck_{i}.list[0].image") == cover_img:
                                eval(f"m_card_deck_{i}.list[0].flip()")
                        except:
                            pass

                card.past_rect.x, card.past_rect.y = self.rect.x, self.rect.y

            elif card.price == 1 and not self.my_color and not self.my_nom:

                self.my_price = card.price

                self.my_color = card.color
                self.my_nom = card.nom

                if card in card_deck.card_deck_use:
                    cardd = card_deck.card_deck_use.pop(card_deck.card_deck_use.index(card))
                    self.list.append(cardd)

                for i in range(1, 5):
                    if eval(f"reset_{i}") != self:
                        reset_i = eval(f"reset_{i}")
                        if card in reset_i.list:
                            cardd = reset_i.list.pop(reset_i.list.index(card))
                            self.list.append(cardd)
                            if reset_i.my_price > 1:
                                reset_i.my_price -= 1
                            else:
                                reset_i.my_price = 0
                                reset_i.my_nom = None
                                reset_i.my_color = None

                for i in range(1, 8):
                    if card in eval(f"m_card_deck_{i}.list"):
                        cardd = eval(f"m_card_deck_{i}.list.pop(m_card_deck_{i}.list.index(card))")
                        self.list.append(cardd)
                        try:
                            if eval(f"m_card_deck_{i}.list[0].image") == cover_img:
                                eval(f"m_card_deck_{i}.list[0].flip()")
                        except:
                            pass

                # for i in range(1, 5):
                #     if eval(f"reset_{i}.")

                card.past_rect.x, card.past_rect.y = self.rect.x, self.rect.y


class MiniCardDeck(pygame.sprite.Sprite):

    def __init__(self, card_deck, x, y, nom):
        pygame.sprite.Sprite.__init__(self)

        self.image = pole_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.list = [self]
        self.my_group = pygame.sprite.Group()
        for i in range(nom):
            card = card_deck.card_deck.pop(-1)
            self.list.append(card)
            card.rect.y = y
            card.rect.x = x
            card.past_rect.y = y
            card.past_rect.x = x
            y += 30
        self.list[-1].flip()
        self.price = self.list[-1].price
        self.color = None

        self.width = 111
        self.height = 158

    def draw(self):
        if self.list == [self]:
            self.price = 0
            self.color = None
        else:
            self.price = self.list[-1].price
            self.color = self.list[-1].color

        self.list.reverse()

        for i in self.list:
            i.update(self.list[:self.list.index(i)])

        self.list.reverse()

        for i in self.list:
            self.my_group.add(i)

        self.my_group.draw(win)
        self.my_group.empty()

    def update(self, *args):
        pass

    def cheak(self, card, list):
        global card_deck
        x, y = pygame.mouse.get_pos()
        try:
            if move and x > self.list[-1].rect.left and x < self.list[-1].rect.right and \
                   y > self.list[-1].rect.top and y < self.list[-1].rect.bottom:

                print("///", card.color, self.color, "///", card.price, self.price)

                if card.color != self.color and card.price == self.price-1 or \
                        self.price == 0 and card.price == 13:

                    if self.price != 0:
                        y, x = self.list[-1].rect.y + 30, self.list[-1].rect.x
                    else:
                        y, x = self.list[-1].rect.y, self.list[-1].rect.x

                    if card in card_deck.card_deck_use:
                        cardd = card_deck.card_deck_use.pop(card_deck.card_deck_use.index(card))
                        self.list.append(cardd)
                        card.past_rect.x, card.past_rect.y = x, y

                    for i in range(1, 5):
                        if eval(f"reset_{i}") != self:
                            reset_i = eval(f"reset_{i}")
                            if card in reset_i.list:
                                cardd = reset_i.list.pop(reset_i.list.index(card))
                                self.list.append(cardd)
                                if reset_i.my_price > 1:
                                    reset_i.my_price -= 1
                                else:
                                    reset_i.my_price = 0
                                    reset_i.my_nom = None
                                    reset_i.my_color = None
                                card.past_rect.x, card.past_rect.y = x, y

                    for i in range(1, 8):
                        if card in eval(f"m_card_deck_{i}.list"):
                            cardd = eval(f"m_card_deck_{i}.list.pop(m_card_deck_{i}.list.index(card))")
                            self.list.append(cardd)
                            card.past_rect.x, card.past_rect.y = x, y
                            if list:
                                for cardd in list:
                                    cardd = eval(f"m_card_deck_{i}.list.pop(m_card_deck_{i}.list.index(cardd))")
                                    self.list.append(cardd)
                                    cardd.past_rect.x, cardd.past_rect.y = x, y-30
                                    y += 30
                            try:
                                if eval(f"m_card_deck_{i}.list[0].image") == cover_img:
                                    eval(f"m_card_deck_{i}.list[0].flip()")
                            except:
                                pass

                    # for i in range(1, 5):
                    #     if eval(f"reset_{i}.")
        except:
            pass


class Button(pygame.sprite.Sprite):

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()

    def x_y(self, x, y):
        self.rect.x, self.rect.y = x, y

    def update(self):
        x, y = pygame.mouse.get_pos()
        if x > self.rect.left and x < self.rect.right and \
                y > self.rect.top and y < self.rect.bottom and pygame.mouse.get_pressed()[0]:
            return True
        return False


class WinOrLose:

    def __init__(self):
        self.lose_button = Button(button_lose_img)
        self.lose_button.x_y(WIDTH - self.lose_button.rect.width, 50)

        self.buttons = [self.lose_button]
        self.group = pygame.sprite.Group()

    def update(self):
        global lose
        if self.lose_button.update():
            lose = True
        if reset_1.my_price == 13 and reset_2.my_price == 13 and reset_3.my_price == 13 and reset_4.my_price == 13:
            victory[0] = True
        if victory[0]:
            self.win_button = Button(button_win_img)
            self.win_button.x_y(WIDTH // 2 - self.win_button.rect.width // 2, HEIGHT // 2 - self.win_button.rect.height // 2)
            self.buttons = []
            self.buttons.append(self.win_button)
        if victory[0] and self.win_button.update():
            victory[1] = True

    def draw(self):
        for i in self.buttons:
            self.group.add(i)
        self.group.draw(win)
        self.group.empty()


def update():

    win_or_lose.update()
    if not victory[0]:
        card_deck.update()
    if pygame.mouse.get_pressed()[1]:
        victory[0] = True


def draw():

    win.fill(GREEN)
    if not victory[0]:
        cards_group_draw.draw(win)
        cards_use_group_draw.draw(win)
        reset_group_draw.draw(win)
        reset_1.draw()
        reset_2.draw()
        reset_3.draw()
        reset_4.draw()
        m_card_deck_1.draw()
        m_card_deck_2.draw()
        m_card_deck_3.draw()
        m_card_deck_4.draw()
        m_card_deck_5.draw()
        m_card_deck_6.draw()
        m_card_deck_7.draw()
        reset_group.empty()
    win_or_lose.draw()
    move_group.draw(win)
    print('\n//////////////////////////////////////////////')


def empty():
    if not victory[0]:
        cards_group_draw.empty()


def declare():
    global cards_in_polia_group, cards_group_draw, reset_group, reset_group_draw, cards_use_group_draw, card_deck
    global m_card_deck_1, m_card_deck_2, m_card_deck_3, m_card_deck_4, m_card_deck_5, m_card_deck_6, m_card_deck_7
    global reset_1, reset_2, reset_3, reset_4, reset, win_or_lose

    cards_in_polia_group = pygame.sprite.Group()
    cards_group_draw = pygame.sprite.Group()
    reset_group = pygame.sprite.Group()
    reset_group_draw = pygame.sprite.Group()
    cards_use_group_draw = pygame.sprite.Group()
    card_deck = CardDeck(100, 100)
    m_card_deck_1 = MiniCardDeck(card_deck, 50, 300, 1)
    m_card_deck_2 = MiniCardDeck(card_deck, 178, 300, 2)
    m_card_deck_3 = MiniCardDeck(card_deck, 306, 300, 3)
    m_card_deck_4 = MiniCardDeck(card_deck, 434, 300, 4)
    m_card_deck_5 = MiniCardDeck(card_deck, 562, 300, 5)
    m_card_deck_6 = MiniCardDeck(card_deck, 690, 300, 6)
    m_card_deck_7 = MiniCardDeck(card_deck, 818, 300, 7)
    reset_1 = Reset(card_deck, 1)
    reset_2 = Reset(card_deck, 2)
    reset_3 = Reset(card_deck, 3)
    reset_4 = Reset(card_deck, 4)
    reset = [reset_1, reset_2, reset_3, reset_4]
    win_or_lose = WinOrLose()


cards_in_polia_group = pygame.sprite.Group()
cards_group_draw = pygame.sprite.Group()
reset_group = pygame.sprite.Group()
reset_group_draw = pygame.sprite.Group()
cards_use_group_draw = pygame.sprite.Group()
card_deck = CardDeck(100, 100)
m_card_deck_1 = MiniCardDeck(card_deck, 50, 300, 1)
m_card_deck_2 = MiniCardDeck(card_deck, 178, 300, 2)
m_card_deck_3 = MiniCardDeck(card_deck, 306, 300, 3)
m_card_deck_4 = MiniCardDeck(card_deck, 434, 300, 4)
m_card_deck_5 = MiniCardDeck(card_deck, 562, 300, 5)
m_card_deck_6 = MiniCardDeck(card_deck, 690, 300, 6)
m_card_deck_7 = MiniCardDeck(card_deck, 818, 300, 7)
reset_1 = Reset(card_deck, 1)
reset_2 = Reset(card_deck, 2)
reset_3 = Reset(card_deck, 3)
reset_4 = Reset(card_deck, 4)
reset = [reset_1, reset_2, reset_3, reset_4]
move_group = pygame.sprite.Group()
win_or_lose = WinOrLose()

run = True
while run:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if victory[1]:
        run = False

    if lose:
        declare()
        victory = [False, False]
        lose = False
    update()
    draw()
    empty()
    # //////////////////////////////////////////flip//////////////////////////////////////////
    pygame.display.flip()

pygame.quit()

