import serial

# Открываем COM порт для чтения данных
com_port = serial.Serial('COM4', 921600)

# Открываем файл для записи данных в бинарном режиме
file_name = 'received_data.txt'
with open(file_name, 'wb') as file:
    while True:
        # Читаем блок данных размером 50 байт
        data_block = com_port.read(50)

        # Ищем индекс символов \r\n в блоке данных
        end_index = data_block.find(b'\r\n')
        if end_index != -1:
            # Если найдены символы \r\n, обрезаем данные до них и записываем в файл
            line = data_block[:end_index]
            if line.startswith(b';;;'):
                file.write(line[3:] + b'\n')
                print("GOOD!")
        else:
            # Если символы \r\n не найдены, записываем все данные в файл
            # if data_block.startswith(b';;;'):
            #     file.write(data_block[3:] + b'\n')
            print("FAIL!")

# Закрываем COM порт
com_port.close()

print(f"Данные успешно записаны в файл {file_name}.")
