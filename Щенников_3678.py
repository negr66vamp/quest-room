b = "y"
while (b == "y"):
    print("добро пожаловать в квест!")
    print("ты очнулся в комнате и ничего не помнишь")
    print("перед тобой дверь, так как выбора больше не было, ты открыл ее и прошел внутрь")
    print('"громкий хлопок!"')
    print("ты обернулся и увидел что дверь сзади захлопнулась")
    print("ты отчаялся и сдался, но потом ты увидел дырку на полу.")
    print("спуститься туда или нет?")
    a = input()
    if (a == "нет"):
        print("вы остались без помощи, конец игры")
        print("вы хотите начать заново? y/n?")
        b = input()  
    if (a == "да"):
        print("ты спустился вниз и увидел две двери.")
        print("открыть дверь или нет?")
        b = input()
        if (a == "да"):
            print("ты открыл дверь и увидел сундук при первой возможности ты открыл его и увидел записку")
            print("ты прочитал записку и в ней было записан код")
            print("1934")
            print("звук шагов")
            print("к тебе пришел человек в маске и зовет тебя")
            print("идти за ним?")
            b = input() 
    if (a == "нет"):
        print("вы остались без помощи, конец игры")
        print("вы хотите начать заново? y/n?")
        b = input()  
    if (a == "да"):
        print("он отвел тебя к двери в которой тебе надо было записать код")
        print("ты записал код 1934 и когда вышел, очнулся соным в своей кроватке)")
        print("Конец Игры!")     
        s = input()
    else:
        print("вы неправильно ответили на вопрос. Ответьте 'да' или 'нет'")
