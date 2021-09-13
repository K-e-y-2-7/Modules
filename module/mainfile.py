from FuntionsForModule import profile1
import sys
import pathlib


print('Привет,', profile1.user_name, '!!!')

way_to_directory = str(pathlib.Path(__file__).parent.absolute())
while True:   
    
    print('''
    1 -- Скрипт со стенкой (h/w #4)
    2 -- Скрипт со словарями и списком ключей (h/w #5)
    3 -- Скрипт с сортировкой числовой последовательности
    4 -- Крестики-нолики
    5 -- Игра мозаика 
    6 -- 
    change -- изменить имя
    q/quit -- выход с программы
    
    +=================+
    |  1  |  2  |  3  |
    |-----+-----+-----|
    |  4  |  5  |  6  |
    |-----+-----+-----|
    |  q |change| quit|
    +=================+
    
    ''')
    valid_choices = ['1','2','3','4','5','6','q','quit','change']
    user_choice = input(profile1.user_name + ', выберите символ из предложенных выше из предложенных выше: ').lower()
    

    if user_choice not in valid_choices:
        print('Вы ввели недопустимый символ. Повторите ввод: ')
        continue

    if user_choice == 'change':
        profile1.user_name = input('Введите ваше имя: ')
    if user_choice == 'q' or user_choice == 'quit':
        break
       
    elif user_choice == '1':
       from homework4 import *
       continue
    elif user_choice == '2': 
        from homework5 import *
        continue
    elif user_choice == '3':
        from sorting import *
        continue
    elif user_choice == '4':
        from TicTac import *
        continue
    elif user_choice == '5':
        from mosaic import *
        continue
    elif user_choice == '6':
        ...
        continue
    else:
        pass
                    


