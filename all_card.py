import pygame, os

pole_img = pygame.image.load(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pole.png'))
cover_img = pygame.image.load(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'cover.jpg'))
button_lose_img = pygame.image.load(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'button_lose.png'))
button_win_img = pygame.image.load(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'button_win.png'))

black_1 = os.path.join(os.path.abspath(os.path.dirname(__file__)), "black_1")
black_2 = os.path.join(os.path.abspath(os.path.dirname(__file__)), "black_2")
red_1 = os.path.join(os.path.abspath(os.path.dirname(__file__)), "red_1")
red_2 = os.path.join(os.path.abspath(os.path.dirname(__file__)), "red_2")

black_1_2_img = pygame.image.load(os.path.join(black_1, '2.jpg'))
black_1_3_img = pygame.image.load(os.path.join(black_1, '3.jpg'))
black_1_4_img = pygame.image.load(os.path.join(black_1, '4.jpg'))
black_1_5_img = pygame.image.load(os.path.join(black_1, '5.jpg'))
black_1_6_img = pygame.image.load(os.path.join(black_1, '6.jpg'))
black_1_7_img = pygame.image.load(os.path.join(black_1, '7.jpg'))
black_1_8_img = pygame.image.load(os.path.join(black_1, '8.jpg'))
black_1_9_img = pygame.image.load(os.path.join(black_1, '9.jpg'))
black_1_10_img = pygame.image.load(os.path.join(black_1, '10.jpg'))
black_1_j_img = pygame.image.load(os.path.join(black_1, 'j.jpg'))
black_1_q_img = pygame.image.load(os.path.join(black_1, 'q.jpg'))
black_1_k_img = pygame.image.load(os.path.join(black_1, 'k.jpg'))
black_1_a_img = pygame.image.load(os.path.join(black_1, 'a.jpg'))

black_2_2_img = pygame.image.load(os.path.join(black_2, '2.jpg'))
black_2_3_img = pygame.image.load(os.path.join(black_2, '3.jpg'))
black_2_4_img = pygame.image.load(os.path.join(black_2, '4.jpg'))
black_2_5_img = pygame.image.load(os.path.join(black_2, '5.jpg'))
black_2_6_img = pygame.image.load(os.path.join(black_2, '6.jpg'))
black_2_7_img = pygame.image.load(os.path.join(black_2, '7.jpg'))
black_2_8_img = pygame.image.load(os.path.join(black_2, '8.jpg'))
black_2_9_img = pygame.image.load(os.path.join(black_2, '9.jpg'))
black_2_10_img = pygame.image.load(os.path.join(black_2, '10.jpg'))
black_2_j_img = pygame.image.load(os.path.join(black_2, 'j.jpg'))
black_2_q_img = pygame.image.load(os.path.join(black_2, 'q.jpg'))
black_2_k_img = pygame.image.load(os.path.join(black_2, 'k.jpg'))
black_2_a_img = pygame.image.load(os.path.join(black_2, 'a.jpg'))

red_1_2_img = pygame.image.load(os.path.join(red_1, '2.jpg'))
red_1_3_img = pygame.image.load(os.path.join(red_1, '3.jpg'))
red_1_4_img = pygame.image.load(os.path.join(red_1, '4.jpg'))
red_1_5_img = pygame.image.load(os.path.join(red_1, '5.jpg'))
red_1_6_img = pygame.image.load(os.path.join(red_1, '6.jpg'))
red_1_7_img = pygame.image.load(os.path.join(red_1, '7.jpg'))
red_1_8_img = pygame.image.load(os.path.join(red_1, '8.jpg'))
red_1_9_img = pygame.image.load(os.path.join(red_1, '9.jpg'))
red_1_10_img = pygame.image.load(os.path.join(red_1, '10.jpg'))
red_1_j_img = pygame.image.load(os.path.join(red_1, 'j.jpg'))
red_1_q_img = pygame.image.load(os.path.join(red_1, 'q.jpg'))
red_1_k_img = pygame.image.load(os.path.join(red_1, 'k.jpg'))
red_1_a_img = pygame.image.load(os.path.join(red_1, 'a.jpg'))

red_2_2_img = pygame.image.load(os.path.join(red_2, '2.jpg'))
red_2_3_img = pygame.image.load(os.path.join(red_2, '3.jpg'))
red_2_4_img = pygame.image.load(os.path.join(red_2, '4.jpg'))
red_2_5_img = pygame.image.load(os.path.join(red_2, '5.jpg'))
red_2_6_img = pygame.image.load(os.path.join(red_2, '6.jpg'))
red_2_7_img = pygame.image.load(os.path.join(red_2, '7.jpg'))
red_2_8_img = pygame.image.load(os.path.join(red_2, '8.jpg'))
red_2_9_img = pygame.image.load(os.path.join(red_2, '9.jpg'))
red_2_10_img = pygame.image.load(os.path.join(red_2, '10.png'))
red_2_j_img = pygame.image.load(os.path.join(red_2, 'j.jpg'))
red_2_q_img = pygame.image.load(os.path.join(red_2, 'q.jpg'))
red_2_k_img = pygame.image.load(os.path.join(red_2, 'k.jpg'))
red_2_a_img = pygame.image.load(os.path.join(red_2, 'a.jpg'))

all_card = [
    [1, "b", 2, black_1_2_img],
    [1, "b", 3, black_1_3_img],
    [1, "b", 4, black_1_4_img],
    [1, "b", 5, black_1_5_img],
    [1, "b", 6, black_1_6_img],
    [1, "b", 7, black_1_7_img],
    [1, "b", 8, black_1_8_img],
    [1, "b", 9, black_1_9_img],
    [1, "b", 10, black_1_10_img],
    [1, "b", 11, black_1_j_img],
    [1, "b", 12, black_1_q_img],
    [1, "b", 13, black_1_k_img],
    [1, "b", 1, black_1_a_img],

    [2, "b", 2, black_2_2_img],
    [2, "b", 3, black_2_3_img],
    [2, "b", 4, black_2_4_img],
    [2, "b", 5, black_2_5_img],
    [2, "b", 6, black_2_6_img],
    [2, "b", 7, black_2_7_img],
    [2, "b", 8, black_2_8_img],
    [2, "b", 9, black_2_9_img],
    [2, "b", 10, black_2_10_img],
    [2, "b", 11, black_2_j_img],
    [2, "b", 12, black_2_q_img],
    [2, "b", 13, black_2_k_img],
    [2, "b", 1, black_2_a_img],

    [1, "r", 2, red_1_2_img],
    [1, "r", 3, red_1_3_img],
    [1, "r", 4, red_1_4_img],
    [1, "r", 5, red_1_5_img],
    [1, "r", 6, red_1_6_img],
    [1, "r", 7, red_1_7_img],
    [1, "r", 8, red_1_8_img],
    [1, "r", 9, red_1_9_img],
    [1, "r", 10, red_1_10_img],
    [1, "r", 11, red_1_j_img],
    [1, "r", 12, red_1_q_img],
    [1, "r", 13, red_1_k_img],
    [1, "r", 1, red_1_a_img],

    [2, "r", 2, red_2_2_img],
    [2, "r", 3, red_2_3_img],
    [2, "r", 4, red_2_4_img],
    [2, "r", 5, red_2_5_img],
    [2, "r", 6, red_2_6_img],
    [2, "r", 7, red_2_7_img],
    [2, "r", 8, red_2_8_img],
    [2, "r", 9, red_2_9_img],
    [2, "r", 10, red_2_10_img],
    [2, "r", 11, red_2_j_img],
    [2, "r", 12, red_2_q_img],
    [2, "r", 13, red_2_k_img],
    [2, "r", 1, red_2_a_img],
]
