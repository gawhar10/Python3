"""
House design using matplotlib.
"""
from matplotlib import pyplot as plt
# for Base (rectangle) = (1,1), (1,4), (6,4), (6,1), (1,1)
# for Roof (triangle) = (1,4), (3.5,6), (6,4)
# for Door (rectangle) = (6,1), (4.5,1), (4.5,3), (5.5,3), (5.5,1)
plt.style.use('fivethirtyeight')
x_base = [1, 1, 6, 6, 1]
y_base = [1, 4, 4, 1, 1]

x_roof = [1, 3.5, 6]
y_roof = [4, 6, 4]

x_door = [6, 4.5, 4.5, 5.5, 5.5]
y_door = [1, 1, 3, 3, 1]

plt.plot(x_base, y_base, x_roof, y_roof, x_door, y_door)
plt.title('House Design')
plt.tight_layout()
plt.show()
