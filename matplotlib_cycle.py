"""
Drawing cycle by using matplotlib.pyplot
"""
import matplotlib.pyplot as plt

plt.style.use('ggplot')

baseline_x_axis = [0, 1]
baseline_y_axis = [0, 0]

horizontal_bar_1_x_axis = [.33, .6]
horizontal_bar_1_y_axis = [.3, .3]

horizontal_bar_2_x_axis = [.3, .42, .6]
horizontal_bar_2_y_axis = [.25, .1, .1]

vertical_bar_1_x_axis = [.2, .4]
vertical_bar_1_y_axis = [.1, .4]

vertical_bar_2_x_axis = [.6, .6]
vertical_bar_2_y_axis = [.1, .35]

handle_x_axis = [.35, .4, .45]
handle_y_axis = [.37, .4, .43]

seat_x = [.57, .63]
seat_y = [.35, .35]


figure, axes = plt.subplots()
my_circle_1 = plt.Circle((.2, .1), .1, color='#55828b')
my_circle_2 = plt.Circle((.6, .1), .1, color='#55828b')
pedal = plt.Circle((.42, .1), .02)
axes.set_aspect(1)

plt.plot(baseline_x_axis, baseline_y_axis)
axes.add_artist(my_circle_1)
plt.plot(vertical_bar_1_x_axis, vertical_bar_1_y_axis, color='#ff9966')
axes.add_artist(my_circle_2)
plt.plot(vertical_bar_2_x_axis, vertical_bar_2_y_axis, color='#ff9966')
plt.plot(horizontal_bar_1_x_axis, horizontal_bar_1_y_axis, color='#ff9966')
plt.plot(horizontal_bar_2_x_axis, horizontal_bar_2_y_axis, color='#ff9966')
plt.plot(handle_x_axis, handle_y_axis, color='#ff9966')
plt.plot(seat_x, seat_y)
axes.add_artist(pedal)

plt.title('My Cycle')
plt.tight_layout()
plt.show()
