import numpy

wolrd_alcohol = numpy.genfromtxt("world_alcohol.txt", delimiter=",", dtype=str)
print(type(wolrd_alcohol))
print(wolrd_alcohol)
print(help(numpy.genfromtxt))