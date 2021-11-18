import matplotlib.pyplot as plt
import numpy as np
import math
with open("/home/gr106/Desktop/Scripts/X.txt", "r") as settings:
    X = [float(i) for i in settings.read().split("\n")]


y0 = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []

f00 = open("00.txt", "r")
f10 = open("10.txt", "r")
f20 = open("20.txt", "r")
f30 = open("30.txt", "r")
f40 = open("40.txt", "r")
f50 = open("50.txt", "r")
f60 = open("60.txt", "r")
f70 = open("70.txt", "r")

i = 1
for line in f00:
    if i >= 9:
        y0.append(math.sqrt((int(line) - 812) * 0.16 * 2 / 1.2))
    i += 1

i = 1
for line in f10:
    if i >= 9:
        y1.append(math.sqrt((int(line) - 812) * 0.16 * 2 / 1.2))
    i += 1

i = 1
for line in f20:
    if i >= 9:
        y2.append(math.sqrt((int(line) - 812) * 0.16 * 2 / 1.2))
    i += 1

i = 1
for line in f30:
    if i >= 9:
        y3.append(math.sqrt((int(line) - 812) * 0.16 * 2 / 1.2))
    i += 1

i = 1
for line in f40:
    if i >= 9:
        y4.append(math.sqrt((int(line) - 812) * 0.16 * 2 / 1.2))
    i += 1

i = 1
for line in f50:
    if i >= 9:
        y5.append(math.sqrt((int(line) - 812) * 0.16 * 2 / 1.2))
    i += 1

i = 1
for line in f60:
    if i >= 9:
        y6.append(math.sqrt((int(line) - 812) * 0.16 * 2 / 1.2))
    i += 1

i = 1
for line in f70:
    if i >= 9:
        y7.append(math.sqrt((int(line) - 812) * 0.16 * 2 / 1.2))
    i += 1


fig, ax = plt.subplots(figsize=(16, 10), dpi = 100)
fig.suptitle("Скорость потока воздуха в сечении затопленной струи")
ax.plot(X, y0, lw = 1, c = "black", label = "Q (00mm) = ")
ax.plot(X, y1, lw = 1, c = "green", label = "Q (10mm) = ")
ax.plot(X, y2, lw = 1, c = "red", label = "Q (20mm) = ")
ax.plot(X, y3, lw = 1, c = "brown", label = "Q (30mm) = ")
ax.plot(X, y4, lw = 1, c = "orange", label = "Q (40mm) = ")
ax.plot(X, y5, lw = 1, c = "cyan", label = "Q (50mm) = ")
ax.plot(X, y6, lw = 1, c = "purple", label = "Q (60mm) = ")
ax.plot(X, y7, lw = 1, c = "lime", label = "Q (70mm) = ")


legend = ax.legend(loc='upper right', fontsize='medium')


plt.xlabel("Положение трубки Пито относительно центра струи [мм]")
plt.ylabel("Скорость воздуха [м/с]")
#plt.text(30, 1.2, "Время зарядки = 49.3с")
#plt.text(30, 0.75, "Время разрядки = 40.7с")
plt.grid(True, which = "major", linestyle = "-")
plt.minorticks_on()
plt.grid(True, which = "minor", linestyle = "--", alpha = 1)
#ax.axis([0, 90, 0, 3.5])
fig.savefig("velocity-outgo.png")
plt.show()