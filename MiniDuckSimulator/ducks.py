# -*- coding: UTF-8 -*-

from abstract import Duck
from quack_behavior import Quack
from fly_behavior import FlyWithWings,FlyNoWay

class MallardDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print('I\'m a mallard duck')

class ModelDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Quack()

    def display(self):
        print('I\'m a model duck')

