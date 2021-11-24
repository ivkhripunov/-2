import matplotlib.pyplot as plt
import numpy as np
import time



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
    with open("E:\общеинженерная подготовка\лабораторная 2\-2-main\Scripts\\40.txt", "r") as f:
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
    with open("E:\общеинженерная подготовка\лабораторная 2\-2-main\Scripts\\70.txt", "r") as f:
        for a in f.readlines():
            vals70.append(float(int(a) * 0.15353028816454084 - 160)) # + 1057.0927272727272
    vals70 = np.array(vals70)
    vals70 = 2 * vals70 / 1.184
    vals70 = np.sqrt(abs(vals70))
    '''with open("E:\общеинженерная подготовка\лабораторная 2\-2-main\Scripts\\10.txt", "r") as f:
        for a in f.readlines():
            vals.append(float(int(a) * 0.15353028816454084)) # + 1057.0927272727272
    vals = np.array(vals)
    vals = 2 * vals / 1.184
    vals = np.sqrt(vals)
    start_time = time.time()
    for i in range(360000):
        value = getAdc()
        vals.append(value)
        timer = time.time() - start_time
        times.append(timer)

    vals = np.array(vals)
    times = np.array(times)

    vals = vals * 0.104154818757622 - 13.66429084810035
    '''
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
