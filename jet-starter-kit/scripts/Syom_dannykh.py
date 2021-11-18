import matplotlib.pyplot as plt
import numpy as np
import spidev
import time
import jetFunctions as jet

maxvoltage = 3.3
values = []
dist = []
jet.initStepMotorGpio()
#Массив маркеров настроишь на основании полученных данных
#markers_on = [int(i) for i in range(0,20000,100)]

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1600000

print("Трубка должна находится в положении 0!!!!!!!!")
print("Введите необходимое значение расстояния в мм, если закончили, введите 1000")
mm = int(input())

def getAdc():
    adcResponse = spi.xfer2([0, 0])
    return ((adcResponse[0] & 0x1F) << 8 | adcResponse[1]) >> 1

try:
    
    while mm != 1000:

        with open("/home/gr106/Desktop/jet-starter-kit/data/" + str(mm) + " mm.txt", "w") as f:
            f.write('- Jet Lab\n')
            f.write('- Date: {}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
            f.write('- Step: {} mm\n'.format(10))

        jet.stepForward(int(10 * (((((18.98807792963072))))) - 0.43617330619395706))
        jet.stepBackward(int(20 * (((((18.98807792963072))))) -0.43617330619395706))
        
        for i in range(10000):
            value = (getAdc() * (((((0.15353028816454084))))) + (((1057.0927272727272))) )
            values.append(value)
            with open("/home/gr106/Desktop/jet-starter-kit/data/" + str(mm) + " mm.txt", "a") as f:
                f.write(str(value) + '\n')
        
        
        
        jet.stepForward(int(10 * (((((18.98807792963072))))) - 0.43617330619395706))
        print("Введите необходимое значение расстояния в мм, если закончили, введите 1000")
        mm = int(input())
    values = np.array(values)

    fig, ax = plt.subplots(figsize=(12, 9))
    ax.plot(values,
            linestyle='-',
            linewidth=1,
            color='darkmagenta')
    ax.set_title('График давления от расстояния', style='italic')
    ax.legend(labels=("давление"), loc="upper right")
    ax.set_xlabel('значения ')
    ax.set_ylabel('давление (мм рт ст)')
    ax.axes.grid(
        which="major",
        linewidth="0.4",
    )
    ax.minorticks_on()
    ax.axes.grid(
       which = "minor",
       linewidth = "0.2"
    )
    plt.savefig('/home/gr106/Desktop/jet-starter-kit/plots/pressures.png')
finally:
    jet.deinitStepMotorGpio()
    plt.show()
    spi.close()
