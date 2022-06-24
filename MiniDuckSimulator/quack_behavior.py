# -*- coding: UTF-8 -*-

from abstract import IQuackBehavior

class Quack(IQuackBehavior):
    def quack(self):
        print('Quack')

class Squeak(IQuackBehavior):
    def quack(self):
        print('Squeak')

class MuteQuack(IQuackBehavior):
    def quack(self):
        print('<<  Silence  >>')

