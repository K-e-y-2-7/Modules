'''
Models
===================================

Содержит классы игрока и противника.

'''

import random as rndm


import settings as stg
import exceptions as exc


class Enemy:
    ''' Имеет атрибуты: level, lives.
        Имеет методы: select_attack(), decrease_lives(self), get_info(self)
        Имеет конструктор. 

    '''

    def __init__(self, level):
        self.level = level
        self.lives = self.level

    def get_info(self) -> str:
        ''' Method get info. 
        '''
        return f'Уровень противника {self.level}, его жизни {self.lives} '
    
    @staticmethod
    def select_attack() -> int:
        ''' Возвращает случайное число от одного до трёх.
            Тем самым выбирая кем будет ходить Enemy: 
            Волшебник, Воин, Разбойник.

        '''
        enemy_attack = rndm.randint(1, 3) 

        return enemy_attack 

    def decrtase_lives(self, player):
        ''' Уменьшает количество жизней Enemy.
            Когда жизней становится 0 вызывает исключение EnemyDown.

        '''

        self.lives -= 1
        if self.lives == 0:
            player.add_5_point() 
            raise exc.EnemyDown()   
        print(f'У противника осталось жизней: {self.lives}.') 

        return self.lives


class Player:
    ''' Имеет атрибуты: name, lives, score, allowed_attacks.
        Имеет методы: fight, decrease_lives, attack, defence, add_5_point.
        Имеет конструктор.

    '''
    
    def __init__(self, name):
        self.name = name
        self.lives = stg.PLAYER_LIVES
        self.score = 0
        self.allowed_attacks = ['1', '2', '3', 'Exit', 'E']
    
    def get_info(self) -> str:
        ''' Method get info. 
        '''
        return f'Имя игрока: {self.name} .Жизни игрока {self.lives} '
    
    def add_5_point(self):
        '''Метод добавляет 5 очков к счёту игрока
           после победы над противником.

        '''
        self.score += 5

        return self.score

    @staticmethod
    def fight(att, deff):
        '''Возвращает результат раунда - 0 если ничья,
           -1 если атака неуспешна, 1 если атака успешна.

        '''

        # Связал цифры с типами персонажей для красивого вывода.
        if att == 1:
            att = 'ᏰσλɯɛҕϰϞκ'
        if att == 2:
            att = 'ᛒᛟᛋᚺ'
        if att == 3:
            att = 'Рᥲɜδ᧐ᥔнᥙκ'        
        if deff == 1:
            deff = 'ᏰσλɯɛҕϰϞκ'
        if deff == 2:
            deff = 'ᛒᛟᛋᚺ'
        if deff == 3:
            deff = 'Рᥲɜδ᧐ᥔнᥙκ' 
        print('+', '~'* 75, '+')
        print(' ' * 15 + f'Атакующий {att} 𝐕𝐒 Защищающийся {deff}') 
        print('+', '~'* 75, '+')
        
        
        # В блоке if/else ниже, просто принты для прикольного вывода в консоли
        # Поэтому он такой масивный.
        # По-факту в if результат боя 0 в elif -- 1 в else -- -1.

        if att == deff:
            print(f'{att} и {deff} нᴇ ᴄᴛᴀᴧи ᴄᴩᴀжᴀᴛьᴄя!')
            fight_result = 0
        elif deff == 'ᏰσλɯɛҕϰϞκ' and att == 'Рᥲɜδ᧐ᥔнᥙκ':
            print(f'Аᴛᴀᴋующий {att} убиᴧ Зᴀщищᴀʙɯᴇᴦᴏᴄя {deff}ᴀ!')
            fight_result = 1
        elif deff == 'ᛒᛟᛋᚺ' and att == 'ᏰσλɯɛҕϰϞκ':
            print(f'Зᴀщищᴀющийᴄя {deff} ᴨᴀᴧ ᴏᴛ чᴀᴩ Нᴀᴨᴀдᴀʙɯᴇᴦᴏ ʍᴀᴦᴀ!')
            fight_result = 1
        elif deff == 'Рᥲɜδ᧐ᥔнᥙκ' and att == 'ᛒᛟᛋᚺ':
            print(f'Аᴛᴀᴋующий {att} ᴏдᴏᴧᴇᴧ Зᴀщищᴀʙɯᴇᴦᴏᴄя {deff}ᴀ!')
            fight_result = 1
        else: 
            if att == 'ᏰσλɯɛҕϰϞκ' and deff == 'Рᥲɜδ᧐ᥔнᥙκ':
                print(f'Зᴀщищᴀющийᴄя {deff} убиᴧ Нᴀᴨᴀдᴀющᴇᴦᴏ {att}ᴀ!')
                fight_result = -1
            if att == 'ᛒᛟᛋᚺ' and deff == 'ᏰσλɯɛҕϰϞκ':
                print(f'Нᴀᴨᴀдᴀющий {att} ᴨᴀᴧ ᴏᴛ чᴀᴩ Зᴀщищᴀʙɯᴇᴦᴏᴄя ʍᴀᴦᴀ!')
                fight_result = -1
            if att == 'Рᥲɜδ᧐ᥔнᥙκ' and deff == 'ᛒᛟᛋᚺ':
                print(f'Зᴀщищᴀющийᴄя {deff} ᴏдᴏᴧᴇᴧ Нᴀᴨᴀдᴀющᴇᴦᴏ {att}ᴀ!')
                fight_result = -1

        return fight_result 
    
    def decrease_lives(self):
        ''' Уменьшает количество жизней Player.
            Когда жизней становится 0 вызывает исключение GameOver.

        '''

        self.lives -= 1
        if self.lives == 0:   
            with open (stg.SCORE_FILE_PATH, 'a') as user_score:
                user_score.write(f'Player score: {self.name} = {self.score} \n')
            raise exc.GameOver                   
        print('ሃ ɞαс σсτα᧘σсь жυʒʜϱύ: ', self.lives)

        return self.lives

    def attack(self, enemy_obj):
        '''Получает ввод от пользователя (1, 2, 3),
           выбирает атаку противника из объекта enemy_obj;
           вызывает метод fight();

        '''

        player_att = input ('Выберите кем будете атаковать: \
        Волшебник = 1, Воин = 2, Разбойник = 3.\
        "Exit" / "E" = выход. Ввод: ').title()
        
        while True:
           
            if player_att in self.allowed_attacks:
                if player_att == 'Exit' or player_att == 'E':
                    raise exc.Exit()
                player_att = int(player_att)
                break
            else:
                player_att = input('Тᴀᴋᴏᴦᴏ ᴨᴇᴩᴄᴏнᴀжᴀ нᴇ ᴄущᴇᴄᴛʙуᴇᴛ.\
                Выбᴇᴩиᴛᴇ ᴏднᴏᴦᴏ ᴨᴇᴩᴄᴏнᴀжᴀ иɜ ᴨᴩᴇдᴧᴏжᴇнных ʙыɯᴇ. ').title()

        enemy_def = enemy_obj.select_attack()
        fight_results = self.fight(player_att, enemy_def)
 
        if fight_results == 0:
            print('''
                               +~~~~~~~~+
                               ⌇  𝑫𝑹𝑨𝑾  ⌇
                               +~~~~~~~~+
            ''')
            print("Стороны не захотели сражаться!") 
        elif fight_results == 1:
            print('''
                         +~~~~~~~~~~~~~~~~~~~~~+
                         ⌇  𝑺𝑼𝑪𝑪𝑬𝑺𝑺𝑭𝑼𝑳 𝑨𝑻𝑻𝑨𝑪𝑲! ⌇
                         +~~~~~~~~~~~~~~~~~~~~~+
            ''')
            print("Вы убили вражеского персонажа! Ваша атака победила!")
            self.score += 1
            enemy_obj.decrtase_lives(self)
        else:
            print('''
                        +~~~~~~~~~~~~~~~~~~~~~~+
                        ⌇ 𝚄𝙽𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻 𝙰𝚃𝚃𝙰𝙲𝙺! ⌇
                        +~~~~~~~~~~~~~~~~~~~~~~+
            ''')
            print('''Вражесский персонаж смог сдержать ваше наступление!
             Защита врага победила!
            ''')
        print('+' + '-' * 77 + '+')

    def defence(self, enemy_obj):
        '''В метод fight первым передается атака противника,
           и при удачной атаке противника вызывается метод
           decrease_lives игрока.

        '''
        
        player_def = input ('Выберите кем будете защищаться: \
        Волшебник = 1, Воин = 2, Разбойник = 3.\
        "Exit" / "E" = выход. Ввод: ').title()
        
        while True: 
            if player_def in self.allowed_attacks:
                if player_def == 'Exit' or player_def == 'E':
                    raise exc.Exit()
                player_def = int(player_def)
                break
            else:
                player_def = input('Тᴀᴋᴏᴦᴏ ᴨᴇᴩᴄᴏнᴀжᴀ нᴇ ᴄущᴇᴄᴛʙуᴇᴛ.\
                Выбᴇᴩиᴛᴇ ᴏднᴏᴦᴏ ᴨᴇᴩᴄᴏнᴀжᴀ иɜ ᴨᴩᴇдᴧᴏжᴇнных ʙыɯᴇ. ').title()
            
            if player_def == 'Exit':
                raise exc.Exit()
        

        enemy_att = enemy_obj.select_attack()
        fight_results = self.fight(enemy_att, player_def)

        if fight_results == 0:
            print('''
                             +~~~~~~~~+
                             ⌇ 𝑫𝑹𝑨𝑾   ⌇
                             +~~~~~~~~+
            ''')
            print("Стороны не захотели сражаться!") 
        elif fight_results == 1:
            print('''
                    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
                    ⌇  𝙿𝚁𝙾𝚃𝙴𝙲𝚃𝙸𝙾𝙽 𝙷𝙰𝚂 𝙱𝙴𝙴𝙽 𝙳𝙴𝙵𝙴𝙰𝚃𝙴𝙳!  ⌇
                    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
            ''')
            print("Ваш персонаж пал в бою. Атака врага победила!")
            self.decrease_lives()
        else:
            print('''
                        +~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
                        ⌇  𝑻𝑯𝑬 𝑷𝑹𝑶𝑻𝑬𝑪𝑻𝑰𝑶𝑵 𝑹𝑬𝑳𝑬𝑨𝑺𝑬𝑫!  ⌇
                        +~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
            ''')
            print('''Вы смогли отстоять наступление врага!
                  Поздравляю!
                  Но это не повод расслабляться!
                  Ваша защита победила!
                  ''')
            self.score += 1
        print('+' + '-' * 77 + '+')
    


if __name__ == '__main__':
    print(stg.SCORE_FILE_PATH)
