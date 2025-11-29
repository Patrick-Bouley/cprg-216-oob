import random
import statistics as st # This lets us import statistics, but shortens the function call to st for faster typing
from math import cos, sin, log, factorial #This lets us import specific function from a module. letting us use them without calling the math module in the code. EX math.cos just becoms cos


for i in range(100):
    print(random.randint(0,10), end=" ")
print()

print(cos(0))
print(factorial(5))
print(st.mean([4,7,8,9,10]))
print(st.stdev([4,7,8,9,10]))
print(st.stdev([8.9,9.0,8.8,9.2,9.1]))