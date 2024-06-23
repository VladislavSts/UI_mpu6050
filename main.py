import serial

class Data:
    def __init__(self):
        self.Accel_X_RAW = 0
        self.Accel_Y_RAW = 0
        self.Accel_Z_RAW = 0
        self.temp = 0
        self.Gyro_X_RAW = 0
        self.Gyro_Y_RAW = 0
        self.Gyro_Z_RAW = 0

    def calculate(self):
        Ax = self.Accel_X_RAW / 16384.0
        Ay = self.Accel_Y_RAW / 16384.0
        Az = self.Accel_Z_RAW / 16384.0
        Temperature = (self.temp / 340.0) + 36.53
        Gx = self.Gyro_X_RAW / 131.0
        Gy = self.Gyro_Y_RAW / 131.0
        Gz = self.Gyro_Z_RAW / 131.0
        return Ax, Ay, Az, Gx, Gy, Gz, Temperature


# Открываем COM порт для чтения данных
com_port = serial.Serial('COM18', 921600)

# Открываем файл для записи данных в текстовом режиме
file_name = 'received_data.txt'
with open(file_name, 'wb') as file:
    buffer = b''
    while True:
        # Читаем блок данных размером 128 байт
        data_block = com_port.read(128)
        buffer += data_block

        # Ищем индекс символов \r\n в буфере данных
        end_index = buffer.find(b'\r\n')
        while end_index != -1:
            # Если найдены символы \r\n, обрабатываем строку
            line = buffer[:end_index]
            if b';;;' in line:
                start_index = line.index(b';;;')
                raw_values = line[start_index + 3:].split()

                if len(raw_values) == 7:
                    data = Data()
                    data.Accel_X_RAW = int(raw_values[0])
                    data.Accel_Y_RAW = int(raw_values[1])
                    data.Accel_Z_RAW = int(raw_values[2])
                    data.Gyro_X_RAW = int(raw_values[3])
                    data.Gyro_Y_RAW = int(raw_values[4])
                    data.Gyro_Z_RAW = int(raw_values[5])
                    data.temp = int(raw_values[6])

                    Ax, Ay, Az, Gx, Gy, Gz, Temperature = data.calculate()
                    calculated_line = f"{Ax:.2f} {Ay:.2f} {Az:.2f} {Gx:.2f} {Gy:.2f} {Gz:.2f} {Temperature:.2f}\r\n"
                    file.write(calculated_line.encode())
                    print("GOOD!")
                else:
                    print("FAIL!")
            else:
                print("FAIL!")

            # Обрезаем обработанную строку из буфера
            buffer = buffer[end_index + 2:]

            # Ищем следующий индекс символов \r\n в оставшейся части буфера
            end_index = buffer.find(b'\r\n')

# Закрываем COM порт
com_port.close()

print(f"Данные успешно записаны в файл {file_name}.")
