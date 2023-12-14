import random
from time import sleep


# Доп. Задание - блэкджэк. Sleep добавил для более простого восприятия самой игры

def win(hand1, hand2):  # Определние победителя 1 - комп, 2 - игрок, 0 - ничья /// hand1 - рука игрока hand2 - рука компа
    if hand1 > 21 or hand2 > 21:
        if hand1 > 21 and hand2 > 21:
            if hand1 > hand2:
                return 1
            elif hand1 < hand2:
                return 2
            else:
                return 0
        if hand1 > hand2:
            return 1
        elif hand1 < hand2:
            return 2
    elif (21 - hand1) < (21 - hand2):
        return 2
    elif (21 - hand1) > (21 - hand2):
        return 1
    else:
        return 0


def titles(num):  # переделывает индексы карт без цифр в вальта, даму и тд
    if num == 2:
        num = 'Jack'
    elif num == 3:
        num = 'Queen'
    elif num == 4:
        num = 'King'
    elif num == 1:
        num = 'Ace'
    return num


def ost(hand):  # ИИ, отвратительный, примитивный, мне за это стыдно
    chance = hand
    if chance >= 20:
        return 0 # 100% шанс, что out
    if chance <= 11:
        return 1 # 100% шанс, что In
    if 12 <= chance <= 14:
        a = random.randint(1, 4)
        if a == 4: # 75% шанс , что in
            return 0
        else:
            return 1
    if 15 <= chance <= 16:
        a = random.randint(0, 1)
        return a # 50 на 50
    if 17 <= chance <= 19:
        a = random.randint(1, 10)
        if a == 10:
            return 1 # 90% шанс, что out
        else:
            return 0


loses = 0 #статистика
wins = 0
draws = 0
print('Hello, my friend and welcome to "21" game! I hope you know the rules! Good luck!')
print('Your go first!')
while True:
    cards = []  # Задаю колоду(пропускаю 5 тк её нет в картах) + изначалную руку + статус возможности хода
    p_hand = 0
    c_hand = 0
    p_turn = True
    c_turn = True
    for i in range(1, 5):
        cards.append(str(i))
        cards.append(str(i))
        cards.append(str(i))
        cards.append(str(i))
    for i in range(6, 11):
        cards.append(str(i))
        cards.append(str(i))
        cards.append(str(i))
        cards.append(str(i))
    while True:
        if not c_turn and not p_turn:  # Проверка обоих игроков. Если оба вышли - результат игры
            if win(p_hand, c_hand) == 1:
                sleep(2)
                print('Hell nah! You lost! Such a sad story with your', p_hand, 'points in hand and their', c_hand, '!')
                loses += 1
                break
            elif win(p_hand, c_hand) == 2:
                sleep(2)
                print('Oh yeah! Piece of cake! What do you have?', p_hand, '? Nice! Their', c_hand, 'is nothing he-he!')
                wins += 1
                break
            elif win(p_hand, c_hand) == 0:
                sleep(2)
                print('Such a case, both have', p_hand, c_hand, '. Good luck next time mate...')
                draws += 1
                break
        if p_turn:  # Проверка возможности хода
            sleep(0.5)
            answer = str(input('Are you in or out? '))
            if answer == 'in':  # Проверка ответа игрока
                pick_p = (random.choice(cards))
                cards.remove(pick_p)  # Убирает карту из колоды, плюсует её к руке
                p_hand += int(pick_p)
                sleep(0.5)
                print('Okay... You took', titles(int(pick_p)), '. Now you have', pick_p, 'points more.', p_hand,
                      'total.')
            else:
                p_turn = False  # -Право ходить у игрока
                sleep(0.2)
                print("Mkay, you will have no other chance. Let's see who will win")
        if c_turn:  # Проверка возможности хода
            if ost(c_hand) == 1:  # Проверка ответа компа
                sleep(1)
                print("*Opponent* I'm in.")
                pick_c = random.choice(cards)
                cards.remove(pick_c)
                c_hand += int(pick_c)
                sleep(1)
                print('Your opponent took their card. Next round...')
            else:
                sleep(1)
                print("*Opponent* I'm out.")
                c_turn = False  # -Право ходить у компа
    sleep(2)
    print('Your statistics:')
    print('Defeats:', loses)
    print('Victories:', wins)
    print('Draws:', draws)
    print('Wanna play again?')
    answer = str(input())
    if answer == 'yes':
        print('Welcome back, mate, it is still a 21 game!')
        continue
    else:
        print('See you, then!')
        break
