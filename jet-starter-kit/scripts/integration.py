import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
from scipy import interpolate, integrate



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

    with open("/home/ivankhripunov/Загрузки/-2-main/data sorted/00.txt", "r") as f:
        for a in f.readlines():
            vals00.append(float(int(a) * 0.15353028816454084-160)) # + 1057.0927272727272
    vals00 = np.array(vals00)
    vals00 = 2 * vals00 / 1.184
    vals00 = np.sqrt(abs(vals00))
    with open("/home/ivankhripunov/Загрузки/-2-main/data sorted/10.txt", "r") as f:
        for a in f.readlines():
            vals10.append(float(int(a) * 0.15353028816454084 - 160)) # + 1057.0927272727272
    vals10 = np.array(vals10)
    vals10 = 2 * vals10 / 1.184
    vals10 = np.sqrt(abs(vals10))
    with open("/home/ivankhripunov/Загрузки/-2-main/data sorted/20.txt", "r") as f:
        for a in f.readlines():
            vals20.append(float(int(a) * 0.15353028816454084 - 160)) # + 1057.0927272727272
    vals20 = np.array(vals20)
    vals20 = 2 * vals20 / 1.184
    vals20 = np.sqrt(abs(vals20))
    with open("/home/ivankhripunov/Загрузки/-2-main/data sorted/30.txt", "r") as f:
        for a in f.readlines():
            vals30.append(float(int(a) * 0.15353028816454084 - 160)) # + 1057.0927272727272
    vals30 = np.array(vals30)
    vals30 = 2 * vals30 / 1.184
    vals30 = np.sqrt(abs(vals30))
    with open("/home/ivankhripunov/Загрузки/-2-main/data sorted/40.txt",  "r") as f:
        for a in f.readlines():
            vals40.append(float(int(a) * 0.15353028816454084 - 160)) # + 1057.0927272727272
    vals40 = np.array(vals40)
    vals40 = 2 * vals40 / 1.184
    vals40 = np.sqrt(abs(vals40))
    with open("/home/ivankhripunov/Загрузки/-2-main/data sorted/50.txt", "r") as f:
        for a in f.readlines():
            vals50.append(float(int(a) * 0.15353028816454084 - 160)) # + 1057.0927272727272
    vals50 = np.array(vals50)
    vals50 = 2 * vals50 / 1.184
    vals50 = np.sqrt(abs(vals50))
    with open("/home/ivankhripunov/Загрузки/-2-main/data sorted/60.txt", "r") as f:
        for a in f.readlines():
            vals60.append(float(int(a) * 0.15353028816454084 - 160)) # + 1057.0927272727272
    vals60 = np.array(vals60)
    vals60 = 2 * vals60 / 1.184
    vals60 = np.sqrt(abs(vals60))
    with open("/home/ivankhripunov/Загрузки/-2-main/data sorted/70.txt",  "r") as f:
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
    #print(distance)
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
            color='y')
    ax.plot(distance, vals70,
            linestyle='-',
            linewidth=1,
            # markevery=markers_on,
            color='aquamarine')
    ax.set_title('Зависимость скорости потока от расстояния ', style='italic')
    ax.legend(labels=("0","10","20" ,"30" ,"40" ,"50" ,"60" ,"70"), loc="upper right")
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
    
    index_0 = 0
    index_10 = 0
    counter = 0
    for i in distance:
        if i > 0:
            index_0 = counter
            continue
        counter += 1
    for i in distance:
        if i > 5:
            index_10 = counter
            continue
        counter += 1
    print(index_0)
    print(index_10)

    dx = (distance[-1] - distance[0]) / len(distance)

    results00 = 2 * np.pi * 1.2 * np.array(integrate.simps(vals00[index_0:index_10] * distance[index_0:index_10], distance[index_0:index_10] *1e-3, dx))
    print(results00)
    results10 = 2 * np.pi * 1.2 * np.array(integrate.simps(vals10[index_0:index_10] * distance[index_0:index_10], distance[index_0:index_10] *1e-3, dx))
    print(results10)
    results20 = 2 * np.pi * 1.2 * np.array(integrate.simps(vals20[index_0:index_10] * distance[index_0:index_10], distance[index_0:index_10] *1e-3, dx))
    print(results20)
    results30 = 2 * np.pi * 1.2 * np.array(integrate.simps(vals30[index_0:index_10] * distance[index_0:index_10], distance[index_0:index_10] *1e-3, dx))
    print(results30)
    results40 = 2 * np.pi * 1.2 * np.array(integrate.simps(vals40[index_0:index_10] * distance[index_0:index_10], distance[index_0:index_10] *1e-3, dx))
    print(results40)
    results50 = 2 * np.pi * 1.2 * np.array(integrate.simps(vals50[index_0:index_10] * distance[index_0:index_10], distance[index_0:index_10] *1e-3, dx))
    print(results50)
    results60 = 2 * np.pi * 1.2 * np.array(integrate.simps(vals60[index_0:index_10] * distance[index_0:index_10], distance[index_0:index_10] *1e-3, dx))
    print(results60)
    results70 = 2 * np.pi * 1.2 * np.array(integrate.simps(vals70[index_0:index_10] * distance[index_0:index_10], distance[index_0:index_10] *1e-3, dx))
    print(results70)

    results00 = round(results00, 2)
    results10 = round(results10, 2)
    results20 = round(results20, 2)
    results30 = round(results30, 2)
    results40 = round(results40, 2)
    results50 = round(results50, 2)
    results60 = round(results60, 2)
    results70 = round(results70, 2)

    print(results00)
    print(results10)
    print(results20)
    print(results30)
    print(results40)
    print(results50)
    print(results60)
    print(results70)
    