# -*- coding: UTF-8 -*-

from abc import ABC, abstractmethod

class IFlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class IQuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass

class Duck(ABC):
    def __init__(self):
        self._fly_behavior = None
        self._quack_behavior = None

    @property
    def fly_behavior(self):
        return self._fly_behavior

    @fly_behavior.setter
    def fly_behavior(self,value:IFlyBehavior):
        self._fly_behavior = value

    @property
    def quack_behavior(self):
        return self._quack_behavior

    @quack_behavior.setter
    def quack_behavior(self,value:IQuackBehavior):
        self._quack_behavior = value
    
    @abstractmethod
    def display(self):
        pass

    def perform_fly(self):
        self._fly_behavior.fly()

    def perform_quack(self):
        self._quack_behavior.quack()
    
    def swim(self):
        print('All ducks float, even decoys.')

