from car import * 
from student import *

c1 = Car('Red', 'Toyota', 'Tacoma', 100)
c2 = Car('Blue', 'Toyota', 'Corolla', 80)

print(c1.model, c2.model)
c1.brake()
c2.accelerate()