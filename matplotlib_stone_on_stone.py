"""
stone on stone graph using matplotlib.
"""
import matplotlib.pyplot as plt
# plt.style.use('ggplot')
ax = plt.subplot()
circle_1 = plt.Circle((.5, .13), .1, fill=False)
ax.set_aspect(1)
ax.add_artist(circle_1)

circle_2 = plt.Circle((.5, .35), .13, fill=False)
ax.set_aspect(.6)
ax.add_artist(circle_2)

circle_3 = plt.Circle((.5, .6), .16, fill=False)
ax.set_aspect(.6)
ax.add_artist(circle_3)

circle_4 = plt.Circle((.5, .8), .19, fill=False)
ax.set_aspect(.6)
ax.add_artist(circle_4)

plt.show()
