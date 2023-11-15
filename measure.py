import lightFunctions as j
import matplotlib.pyplot as plt
import numpy as np

photos = ['white_mercury.jpg', 'blue_tungsten.jpg', 'green_tungsten.jpg', 'red_tungsten.jpg', 'white_tungsten.jpg', 'yellow_tungsten.jpg']

rgb, I0 = j.read_image(photos[0], 'graph1.png', 'ртутная лампа', 'белый лист')
I1 = j.read_image(photos[1], 'graph2.png', 'лампа накаливания', 'синий лист')[-1]
I2 = j.read_image(photos[2], 'graph3.png', 'лампа накаливания', 'зеленый лист')[-1]
I3 = j.read_image(photos[3], 'graph4.png', 'лампа накаливания', 'красный лист')[-1]
I4 = j.read_image(photos[4], 'graph5.png', 'лампа накаливания', 'белый лист')[-1]
I5 = j.read_image(photos[5], 'graph6.png', 'лампа накаливая', 'желтый лист')[-1]

r = [i[0] for i in rgb]
b = [i[2] for i in rgb]
r_max, b_max = max(r), max(b)
i_r, i_b = r.index(r_max), b.index(b_max)
k = 610 / i_r

x = np.linspace(0, 350, 350)
x = [i * k for i in x]
plt.cla()
plt.clf()

ax = plt.axes()
ax.set_facecolor(color='#E5E4E2')
ax.grid(which='major', linewidth=1)
ax.grid(which='minor', linewidth=0.7, linestyle='--')
ax.minorticks_on()

plt.plot(x, I1, color='blue', label='blue')
plt.plot(x, I2, color='green', label='green')
plt.plot(x, I3, color='red', label='red')
plt.plot(x, I4, color='white', label='white')
plt.plot(x, I5, color='yellow', label='yellow')

plt.legend()
plt.title('Отражённая интенсивность излучения лампы накаливания')
plt.ylabel('яркость')
plt.xlabel('длина волны, нм')
plt.savefig('I.png')

A1 = [I1[i] / I4[i] for i in range(len(I1))]
A2 = [I2[i] / I4[i] for i in range(len(I1))]
A3 = [I3[i] / I4[i] for i in range(len(I1))]
A4 = [I4[i] / I4[i] for i in range(len(I1))]
A5 = [I5[i] / I4[i] for i in range(len(I1))]

plt.cla()
plt.clf()

ax = plt.axes()
ax.set_facecolor(color='#E5E4E2')
ax.grid(which='major', linewidth=1)
ax.grid(which='minor', linewidth=0.7, linestyle='--')
ax.minorticks_on()

plt.plot(x, A1, color='blue', label='blue')
plt.plot(x, A2, color='green', label='green')
plt.plot(x, A3, color='red', label='red')
plt.plot(x, A4, color='white', label='white')
plt.plot(x, A5, color='yellow', label='yellow')

plt.legend()
plt.title('Зависимость альбедо поверхностей от длины волны падающего света')
plt.ylabel('альбедо')
plt.xlabel('длина волны, нм')
plt.savefig('A.png')
