print("bonjour")
from collections import namedtuple
point1D = namedtuple("point1D", ["x"])
print(point1D)

point2D = namedtuple("point2D", ["x", "y"])
print(point2D)
p2d = point2D(x = 0, y = 1)
print(p2d)


p_04 = point1D(0.4)
print(p_04)

p_05 = point1D(0.5)
print(p_05)


def ajout_point(point1, point2) :
  x = point1[0] + point2[0]
  print(x)
  return point1D(x)
print(f"addiction ok : {ajout_point(p_05, p_04)}")