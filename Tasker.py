# 
#  Tasker.py
# 
#  Created by w0rng on 18.12.2020.
#  Copyright © 2020 w0rng. All rights reserved.
# 

from threading import Thread
import time
import  datetime


class Task:
    def __init__(self, func, time=None, timedelta=None):
        assert time or timedelta, 'Не задано время'
        assert bool(time) ^ bool(timedelta), 'Передано слишком много параметров'

        self.timedelta = timedelta
        self.func = func
        self.time = time
        self.thread = Thread(target=self.run, daemon=True)

    def run(self):
        while True:
            self.func()
            self.sleep()

    def sleep(self):
        if self.time:
            time.sleep(self.time)
        else:
            timedelta = self.__convert(self.timedelta)
            t = self.__get_time(timedelta)
            print(t)
            time.sleep(t)

    def __get_time(self, timedelta):
        a = datetime.datetime(**timedelta) - datetime.datetime.now()
        return a.seconds

    def __convert(self, timedelta):
        result = {
            'year': datetime.datetime.now().year,
            'month': datetime.datetime.now().month,
            'day': datetime.datetime.now().day,
            'hour': datetime.datetime.now().hour,
            'minute': datetime.datetime.now().minute,
            'second': datetime.datetime.now().second
        }
        for key in timedelta:
            result[key] = timedelta[key]
        return result


class Tasker:
    def __init__(self):
        self.__tasks = []

    def make_task(self, time=None, timedelta=None):
        def decorator(func):
            self.__tasks.append(Task(func, time, timedelta))
            def tmp():
                return func()
            return tmp
        return decorator

    def start(self):
        for task in self.__tasks:
            task.thread.start()

    def __del__(self):
        for task in self.__tasks:
            task.thread.join()
