from ducks import MallardDuck,ModelDuck
from fly_behavior import FlyRocketPowered

mallard = MallardDuck()
mallard.perform_fly()
mallard.perform_quack()

model = ModelDuck()
model.perform_fly()
model.fly_behavior = FlyRocketPowered()
model.perform_fly()