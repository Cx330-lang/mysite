import matplotlib.pyplot as plt
from 练习.random_walk import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=5)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running =='n':
        break