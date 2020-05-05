import random
import numpy as np

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    start = 0
    end = 100
    predict = (start + end)//2 # Начинаем поиск с середины интервала. Каждый раз сдвигаем верхнюю или нижнюю границу интервала
    print(number)
    while number != predict:
        count+=1
        print("predict is " + str(predict))
        if number > predict: # Если число больше, то сдвигаем start до уровня predict
            start = predict
        elif number < predict: # Если число меньше, то сдвигаем end до уровня predict
            end = predict
        predict = (start + end) // 2
    return(count) # выход из цикла, если угадали

def score_game(game_core_v2):
    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(100, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v2(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v2)