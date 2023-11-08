import lightFunction  as j
import matplotlib.pyplot as pyplot 
# lumaR = j.readIntensity("red_mercury.jpg", "Wred_processed.jpg", "Лампа накаливания", "красный лист")
# lumaB = j.readIntensity("blue_mercury.jpg", "Wblue_processed.jpg", "Лампа накаливания", "синий лист")
# lumaG = j.readIntensity("green_mercury.jpg", "Wgreen_processed.jpg", "Лампа накаливания", "зелёный лист")
# lumaY = j.readIntensity("yellow_mercury.jpg", "Wyellow_processed.jpg", "Лампа накаливания", "жёлтый лист")
lumaW = j.readIntensity("white_mercury.jpg", "Wwhite_processed.jpg", "Лампа накаливания", "белый лист")

xs = [i for i in range(800, 800-len(lumaW)*2, -2)]
figure, ax = pyplot.subplots()
# ax.plot(xs, lumaG, color='g')
# pyplot.plot(xs, lumaR, color="r")
# pyplot.plot(xs, lumaB, color="b")
pyplot.plot(xs, lumaW, color="b")
# pyplot.plot(xs, lumaY, color="y")
pyplot.title("Калибровка")
pyplot.show()