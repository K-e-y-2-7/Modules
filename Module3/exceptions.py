'''
EXCEPTIONS
========================================

Cодержит в себе кастомные исключения
созданные для контроля игрового процесса
и необходимый для них функционал.

'''

import settings as stg

class GameOver(Exception):
    pass
    

class EnemyDown (Exception):
    pass

class Exit(Exception):
    pass
  