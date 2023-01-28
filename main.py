import random
number = random.randint(1, 100)
allowed_g = 7
g_made = 0
while True:
    player_g = int(input(" Угалай число от 1 до 100"))
    g_made = g_made + 1
    if player_g == number:
        print("Ты офигенный везунчик и угадал за {} попыток".format(g_made))
        break
    elif player_g < number:
        print("Слишком мало!!!")
    else:
        print("Слишком много!!!")
    if g_made == allowed_g:
        print("Ты неудачник и использовал все попытки!GG")
        break
    else:
        print("Осталось {} попыток!".format(allowed_g - g_made))
