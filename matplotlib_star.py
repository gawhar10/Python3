"""
Print star on x - y plane.
"""
import matplotlib.pyplot as plt
plt.style.use('bmh')
up_x = [1, 3, 5, 1]
up_y = [3, 6, 3, 3]
down_x = [1, 3, 5, 1]
down_y = [5, 2, 5, 5]
plt.plot(up_x, up_y)
plt.plot(down_x, down_y)
plt.tight_layout()
# print(plt.style.available)
plt.show()
