print("Hello, it's a graphic!")

import matplotlib.pyplot as plt

# Списки для хранения данных
time = []
accel_x = []
accel_y = []
accel_z = []
gyro_x = []
gyro_y = []
gyro_z = []
temperature = []

# Чтение данных из файла
with open('C:/QtWorkSpace/SensorQT5/output.txt', 'r') as file:
# with open('C:/QtWorkSpace/SensorQT5/release/output.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:

        if line.startswith('time'):
            continue  # Пропускаем заголовок

        if 'Дата эксперимента:' in line:
            continue  # Пропускаем Дата эксперимента

        values = line.strip().split(';')
        time.append(float(values[0]))
        accel_x.append(float(values[1]))
        accel_y.append(float(values[2]))
        accel_z.append(float(values[3]))
        gyro_x.append(float(values[4]))
        gyro_y.append(float(values[5]))
        gyro_z.append(float(values[6]))
        temperature.append(float(values[7]))

# Построение графиков
plt.figure(num='Mpu6050', figsize=(10, 6))

# График Accel_x, Accel_y, Accel_z
plt.subplot(2, 2, 1)
plt.plot(time, accel_x, label='Accel_x')
plt.plot(time, accel_y, label='Accel_y')
plt.plot(time, accel_z, label='Accel_z')
plt.xlabel('Time')
plt.ylabel('Acceleration')
plt.legend(loc='upper right')  # перемещаем легенду в правый верхний угол

# График Gyro_x, Gyro_y, Gyro_z
plt.subplot(2, 2, 2)
plt.plot(time, gyro_x, label='Gyro_x')
plt.plot(time, gyro_y, label='Gyro_y')
plt.plot(time, gyro_z, label='Gyro_z')
plt.xlabel('Time')
plt.ylabel('Gyroscope')
plt.legend(loc='upper right')  # перемещаем легенду в правый верхний угол

# График Temperature
plt.subplot(2, 1, 2)
plt.plot(time, temperature, label='Temperature')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.ylim(20, 50)  # Задаем диапазон оси y
plt.legend(loc='upper right')  # перемещаем легенду в правый верхний угол

# Отображение графиков
plt.tight_layout()
plt.show()
