# 
#  main.py
# 
#  Created by w0rng on 18.12.2020.
#  Copyright © 2020 w0rng. All rights reserved.
# 

from Tasker import Tasker


tasker = Tasker()


# Выполняется каждую минуту
@tasker.make_task(time=60)
def test():
    print('test')


# Выполняется каждую полночь
@tasker.make_task(timedelta={'hour': 0, 'minute': 0})
def test2():
    print('test2')


tasker.start()

# Имитация работы основого потока приложения
while 1:
    pass