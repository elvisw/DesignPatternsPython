# -*- coding: UTF-8 -*-

from abstract import IFlyBehavior

class FlyNoWay(IFlyBehavior):
    def fly(self):
        print('I can\'t fly.')

class FlyRocketPowered(IFlyBehavior):
    def fly(self):
        print('I\'m flying with a rocket!')

class FlyWithWings(IFlyBehavior):
    def fly(self):
        print('I\'m Flying!!')

    