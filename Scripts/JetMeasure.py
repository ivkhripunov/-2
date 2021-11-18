import jetFunctions as jet
import numpy as np
import time

try:
    
    jet.initStepMotorGpio()
    measures = []
    x = []
    i = 1
    jet.initSpiAdc()
    x0 = -30
    #number of steps: 536
    for i in range(100):
        adc = jet.getAdc()
        measures.append(adc)
        x.append(x0)
        x0 += 0.6 #идем с шагом 0.6mm от -30 mm
        jet.stepForward(11) #моторчик двигаем на 11
    #данная часть скрипта для получения показаний при включенном и выключенном вентиляторе
    # a = 0
    # for i in range(500):
    #     adc = jet.getAdc()
    #     measures.append(adc) затем эти массивы отдельно выводим в файлы "00Pa.txt" и "50Pa.txt"
    #     a += adc
    # meanv = a / 500 среднее значение
        
    
    motorSteps = 10
    samplesInMeasure = 100
    count = 100
    with open("/home/gr106/Desktop/Scripts/X.txt", "w") as f:
        np.savetxt(f, np.array(x)) #это массив для координат точек(ось X)
    with open("/home/gr106/Desktop/Scripts/70.txt", "w") as outfile: #здесь каждый раз меняем название файла в засисимости от расстояния - "расстояние.txt"
        outfile.write('- Jet Lab\n\n')
        outfile.write('- Experiment date = {}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
        outfile.write('- Number of samples in measure = {}\n'.format(samplesInMeasure)) # с этим нужно  разобраться, что это такое
        outfile.write('- Number of motor steps between measures = {}\n'.format(motorSteps))
        outfile.write('- Measures count = {}\n\n'.format(count))
        
        outfile.write('- adc12bit\n')
        np.savetxt(outfile, np.array(measures).T, fmt='%d')



finally:
    jet.deinitStepMotorGpio()