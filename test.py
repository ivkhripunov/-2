import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
from scipy import interpolate



'''
x = np.array([int(i) for i in range(0, len(y))])
x_interpolated = np.linspace(0, x[-1], 10000)
f = interpolate.interp1d(x, y)
y_interpolated = f(x_interpolated)
y_filtered = signal.savgol_filter(y_interpolated, 525, 1)
plt.plot(x_interpolated, y_filtered)
plt.show()
'''

try:
    vals00 = []
    vals10 = []
    vals20 = []
    vals30 = []
    vals40 = []
    vals50 = []
    vals60 = []
    vals70 = []
    vals80 = []
    vals90 = []
    distance = []
    for i in range(50, 0 , -1):
        distance.append(- (11 / 19) * i)
    for i in range(50):
        distance.append((11 / 19) * i)

    with open("E:\общеинженерная подготовка\лабораторная 2\-2-main\Scripts\\00.txt", "r") as f:
        for a in f.readlines():
            vals00.append(float(int(a) * 0.15353028816454084-160)) # + 1057.0927272727272
    vals00 = np.array(vals00)
    vals00 = 2 * vals00 / 1.184
    vals00 = np.sqrt(abs(vals00))
    with open("E:\общеинженерная подготовка\лабораторная 2\-2-main\Scripts\\10.txt", "r") as f:
        for a in f.readlines():
            vals10.append(float(int(a) * 0.15353028816454084 - 160)) # + 1057.0927272727272
    vals10 = np.array(vals10)
    vals10 = 2 * vals10 / 1.184
    vals10 = np.sqrt(abs(vals10))
    with open("E:\общеинженерная подготовка\лабораторная 2\-2-main\Scripts\\20.txt", "r") as f:
        for a in f.readlines():
            vals20.append(float(int(a) * 0.15353028816454084 - 160)) # + 1057.0927272727272
    vals20 = np.array(vals20)
    vals20 = 2 * vals20 / 1.184
    vals20 = np.sqrt(abs(vals20))
    with open("E:\общеинженерная подготовка\лабораторная 2\-2-main\Scripts\\30.txt", "r") as f:
        for a in f.readlines():
            vals30.append(float(int(a) * 0.15353028816454084 - 160)) # + 1057.0927272727272
    vals30 = np.array(vals30)
    vals30 = 2 * vals30 / 1.184
    vals30 = np.sqrt(abs(vals30))
    with open("E:\общеинженерная подготовка\лабораторная 2\-2-main\Scripts\\40.txt",  "r") as f:
        for a in f.readlines():
            vals40.append(float(int(a) * 0.15353028816454084 - 160)) # + 1057.0927272727272
    vals40 = np.array(vals40)
    vals40 = 2 * vals40 / 1.184
    vals40 = np.sqrt(abs(vals40))
    with open("E:\общеинженерная подготовка\лабораторная 2\-2-main\Scripts\\50.txt", "r") as f:
        for a in f.readlines():
            vals50.append(float(int(a) * 0.15353028816454084 - 160)) # + 1057.0927272727272
    vals50 = np.array(vals50)
    vals50 = 2 * vals50 / 1.184
    vals50 = np.sqrt(abs(vals50))
    with open("E:\общеинженерная подготовка\лабораторная 2\-2-main\Scripts\\60.txt", "r") as f:
        for a in f.readlines():
            vals60.append(float(int(a) * 0.15353028816454084 - 160)) # + 1057.0927272727272
    vals60 = np.array(vals60)
    vals60 = 2 * vals60 / 1.184
    vals60 = np.sqrt(abs(vals60))
    with open("E:\общеинженерная подготовка\лабораторная 2\-2-main\Scripts\\70.txt",  "r") as f:
        for a in f.readlines():
            vals70.append(float(int(a) * 0.15353028816454084 - 160)) # + 1057.0927272727272
    vals70 = np.array(vals70)
    vals70 = 2 * vals70 / 1.184
    vals70 = np.sqrt(abs(vals70))

    distance_interpolated = np.linspace(distance[0], distance[-1], 10000)

    f0 = interpolate.interp1d(distance, vals00)
    f1 = interpolate.interp1d(distance, vals10)
    f2 = interpolate.interp1d(distance, vals20)
    f3 = interpolate.interp1d(distance, vals30)
    f4 = interpolate.interp1d(distance, vals40)
    f5 = interpolate.interp1d(distance, vals50)
    f6 = interpolate.interp1d(distance, vals60)
    f7 = interpolate.interp1d(distance, vals70)

    vals00_interpolated = f0(distance_interpolated)
    vals10_interpolated = f1(distance_interpolated)
    vals20_interpolated = f2(distance_interpolated)
    vals30_interpolated = f3(distance_interpolated)
    vals40_interpolated = f4(distance_interpolated)
    vals50_interpolated = f5(distance_interpolated)
    vals60_interpolated = f6(distance_interpolated)
    vals70_interpolated = f7(distance_interpolated)

    vals00 = signal.savgol_filter(vals00_interpolated, 701, 1)
    vals10 = signal.savgol_filter(vals10_interpolated, 701, 1)
    vals20 = signal.savgol_filter(vals20_interpolated, 701, 1)
    vals30 = signal.savgol_filter(vals30_interpolated, 701, 1)
    vals40 = signal.savgol_filter(vals40_interpolated, 701, 1)
    vals50 = signal.savgol_filter(vals50_interpolated, 701, 1)
    vals60 = signal.savgol_filter(vals60_interpolated, 701, 1)
    vals70 = signal.savgol_filter(vals70_interpolated, 701, 1)

    distance = distance_interpolated

finally:
    print(distance)
    #Значения дистанс это флоаты!!!!!!!!!!!!!!!!
    fig, ax = plt.subplots(figsize=(12, 9))
    ax.plot(distance, vals00,
            linestyle='-',
            linewidth=1,
            # markevery=markers_on,
            color='darkmagenta')
    ax.plot(distance, vals10,
            linestyle='-',
            linewidth=1,
            # markevery=markers_on,
            color='b')
    ax.plot(distance, vals20,
            linestyle='-',
            linewidth=1,
            # markevery=markers_on,
            color='g')
    ax.plot(distance, vals30,
            linestyle='-',
            linewidth=1,
            # markevery=markers_on,
            color='c')
    ax.plot(distance, vals40,
            linestyle='-',
            linewidth=1,
            # markevery=markers_on,
            color='r')
    ax.plot(distance, vals50,
            linestyle='-',
            linewidth=1,
            # markevery=markers_on,
            color='m')
    ax.plot(distance, vals60,
            linestyle='-',
            linewidth=1,
            # markevery=markers_on,
            color='orange')
    ax.plot(distance, vals70,
            linestyle='-',
            linewidth=1,
            # markevery=markers_on,
            color='aquamarine')
    ax.set_title('Зависимость скорости потока от расстояния ', style='italic')
    ax.legend(labels=("Q (00мм) = 4.94 (г/с)","Q (10мм) = 5.29 (г/с)","Q (20мм) = 5.99 (г/с)" ,"Q (30мм) = 5.57 (г/с)"
                      ,"Q (40мм) = 6.22 (г/с)" ,"Q (50мм) = 6.43 (г/с)" ,"Q (60мм) = 6.66 (г/с)" ,"Q (70мм) = 7.69 (г/с)"), loc="upper right")
    ax.set_ylabel('Скорость[м/с]')
    ax.set_xlabel('расстояние до центра потока[мм]')
    # ax.figure(figsize=(10, 7))
    ax.axes.grid(
        which="major",
        linewidth="0.4",
    )
    ax.minorticks_on()
    ax.axes.grid(
        which="minor",
        linewidth="0.2"
    )

    # укажи путь к папке для сохранения графика
    #plt.savefig('/home/gr106/Desktop/blood-starter-kit/plots/fitness.png')
    plt.show()

'''
        #Считаем расход
    q100 = 0
    q200 = 0
    for i in range(3790, 5000):
        q100 += distance[i] * vals00[i] * 29 / 5000
    q100 *= 2 * 1.2 * 3.1415 /1000
    for i in range(5000, 6250):
        q200 += distance[i] * vals00[i] * 29 / 5000
    q200 *= 2 * 1.2 * 3.1415/ 1000
    print( (abs(q100) + q200) / 2)

    q110 = 0
    q210 = 0
    for i in range(3700, 5000):
        q110 += distance[i] * vals10[i] * 29 / 5000
    q110 *= 2 * 1.2 * 3.1415 / 1000
    for i in range(5000, 6300):
        q210 += distance[i] * vals10[i] * 29 / 5000
    q210 *= 2 * 1.2 * 3.1415 / 1000
    print((abs(q110) + q210) / 2)

    q120 = 0
    q220 = 0
    for i in range(3300, 5000):
        q120 += distance[i] * vals20[i] * 29 / 5000
    q120 *= 2 * 1.2 * 3.1415 / 1000
    for i in range(5000, 6700):
        q220 += distance[i] * vals20[i] * 29 / 5000
    q220 *= 2 * 1.2 * 3.1415 / 1000
    print((abs(q120) + q220) / 2)

    q130 = 0
    q230 = 0
    for i in range(2900, 5000):
        q130 += distance[i] * vals30[i] * 29 / 5000
    q130 *= 2 * 1.2 * 3.1415 / 1000
    for i in range(5000, 6700):
        q230 += distance[i] * vals30[i] * 29 / 5000
    q230 *= 2 * 1.2 * 3.1415 / 1000
    print((abs(q130) + q230) / 2)

    q140 = 0
    q240 = 0
    for i in range(2550, 5000):
        q140 += distance[i] * vals40[i] * 29 / 5000
    q140 *= 2 * 1.2 * 3.1415 / 1000
    for i in range(5000, 6700):
        q240 += distance[i] * vals40[i] * 29 / 5000
    q240 *= 2 * 1.2 * 3.1415 / 1000
    print((abs(q140) + q240) / 2)

    q150 = 0
    q250 = 0
    for i in range(2200, 5000):
        q150 += distance[i] * vals50[i] * 29 / 5000
    q150 *= 2 * 1.2 * 3.1415 / 1000
    for i in range(5000, 7000):
        q250 += distance[i] * vals50[i] * 29 / 5000
    q250 *= 2 * 1.2 * 3.1415 / 1000
    print((abs(q150) + q250) / 2)

    q160 = 0
    q260 = 0
    for i in range(3790, 5000):
        q160 += distance[i] * vals60[i] * 29 / 5000
    q160 *= 2 * 1.2 * 3.1415 / 1000
    for i in range(5000, 6250):
        q260 += distance[i] * vals60[i] * 29 / 5000
    q260 *= 2 * 1.2 * 3.1415 / 1000
    print((abs(q160) + q260) / 2)

    q170 = 0
    q270 = 0
    for i in range(3790, 5000):
        q170 += distance[i] * vals70[i] * 29 / 5000
    q170 *= 2 * 1.2 * 3.1415 / 1000
    for i in range(5000, 6250):
        q270 += distance[i] * vals70[i] * 29 / 5000
    q270 *= 2 * 1.2 * 3.1415 / 1000
    print((abs(q170) + q270) / 2)

'''