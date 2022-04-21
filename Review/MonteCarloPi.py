from random import random

tries = int(input("# of tries:"))

hits = 0

for i in range(0,tries,1):
    r = random()
    x = -1 + 2*r
    r = random()
    y = -1 + 2*r

    if x**2 + y**2 <= 1:
        hits = hits + 1

piestimation = 4.0 * hits / tries
print("Estimation for pi: %f" % piestimation)