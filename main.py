# ------------------------- Версия скрипта 1.0.0

# import serial
#
# # Открываем COM порт для чтения данных
# com_port = serial.Serial('COM4', 921600)
#
# # Открываем файл для записи данных в бинарном режиме
# file_name = 'received_data.txt'
# with open(file_name, 'wb') as file:
#     while True:
#         # Читаем блок данных размером 50 байт
#         data_block = com_port.read(50)
#
#         # Ищем индекс символов \r\n в блоке данных
#         end_index = data_block.find(b'\r\n')
#         if end_index != -1:
#             # Если найдены символы \r\n, обрезаем данные до них и записываем в файл
#             line = data_block[:end_index]
#             if line.startswith(b';;;'):
#                 file.write(line[3:] + b'\n')
#                 print("GOOD!")
#         else:
#             # Если символы \r\n не найдены, записываем все данные в файл
#             # if data_block.startswith(b';;;'):
#             #     file.write(data_block[3:] + b'\n')
#             print("FAIL!")
#
# # Закрываем COM порт
# com_port.close()
#
# print(f"Данные успешно записаны в файл {file_name}.")

# ------------------------- Версия скрипта 1.1.0

# import serial
#
# # Открываем COM порт для чтения данных
# com_port = serial.Serial('COM18', 921600)
#
# # Открываем файл для записи данных в текстовом режиме
# file_name = 'received_data.txt'
# with open(file_name, 'wb') as file:
#     buffer = b''
#     while True:
#         # Читаем блок данных размером 50 байт
#         data_block = com_port.read(100)
#         buffer += data_block
#
#         # Ищем индекс символов \r\n в буфере данных
#         end_index = buffer.find(b'\r\n')
#         while end_index != -1:
#             # Если найдены символы \r\n, обрабатываем строку
#             line = buffer[:end_index]
#             if b';;;' in line:
#                 start_index = line.index(b';;;')
#                 file.write(line[start_index + 3:] + b'\r\n')
#                 print("GOOD!")
#             else:
#                 print("FAIL!")
#
#             # Обрезаем обработанную строку из буфера
#             buffer = buffer[end_index + 2:]
#
#             # Ищем следующий индекс символов \r\n в оставшейся части буфера
#             end_index = buffer.find(b'\r\n')
#
# # Закрываем COM порт
# com_port.close()
#
# print(f"Данные успешно записаны в файл {file_name}.")

# ------------------------- Версия скрипта 1.2.0

# import serial
#
# class Data:
#     def __init__(self):
#         self.Accel_X_RAW = 0
#         self.Accel_Y_RAW = 0
#         self.Accel_Z_RAW = 0
#         self.temp = 0
#         self.Gyro_X_RAW = 0
#         self.Gyro_Y_RAW = 0
#         self.Gyro_Z_RAW = 0
#
#     def calculate(self):
#         Ax = self.Accel_X_RAW / 16384.0
#         Ay = self.Accel_Y_RAW / 16384.0
#         Az = self.Accel_Z_RAW / 16384.0
#         Temperature = (self.temp / 340.0) + 36.53
#         Gx = self.Gyro_X_RAW / 131.0
#         Gy = self.Gyro_Y_RAW / 131.0
#         Gz = self.Gyro_Z_RAW / 131.0
#         return Ax, Ay, Az, Gx, Gy, Gz, Temperature
#
#
# # Открываем COM порт для чтения данных
# com_port = serial.Serial('COM18', 921600)
#
# # Открываем файл для записи данных в текстовом режиме
# file_name = 'received_data.txt'
# with open(file_name, 'wb') as file:
#     buffer = b''
#     while True:
#         # Читаем блок данных размером 128 байт
#         data_block = com_port.read(128)
#         buffer += data_block
#
#         # Ищем индекс символов \r\n в буфере данных
#         end_index = buffer.find(b'\r\n')
#         while end_index != -1:
#             # Если найдены символы \r\n, обрабатываем строку
#             line = buffer[:end_index]
#             if b';;;' in line:
#                 start_index = line.index(b';;;')
#                 raw_values = line[start_index + 3:].split()
#
#                 if len(raw_values) == 7:
#                     data = Data()
#                     data.Accel_X_RAW = int(raw_values[0])
#                     data.Accel_Y_RAW = int(raw_values[1])
#                     data.Accel_Z_RAW = int(raw_values[2])
#                     data.Gyro_X_RAW = int(raw_values[3])
#                     data.Gyro_Y_RAW = int(raw_values[4])
#                     data.Gyro_Z_RAW = int(raw_values[5])
#                     data.temp = int(raw_values[6])
#
#                     Ax, Ay, Az, Gx, Gy, Gz, Temperature = data.calculate()
#                     calculated_line = f"{Ax:.2f} {Ay:.2f} {Az:.2f} {Gx:.2f} {Gy:.2f} {Gz:.2f} {Temperature:.2f}\r\n"
#                     file.write(calculated_line.encode())
#                     print("GOOD!")
#                 else:
#                     print("FAIL!")
#             else:
#                 print("FAIL!")
#
#             # Обрезаем обработанную строку из буфера
#             buffer = buffer[end_index + 2:]
#
#             # Ищем следующий индекс символов \r\n в оставшейся части буфера
#             end_index = buffer.find(b'\r\n')
#
# # Закрываем COM порт
# com_port.close()
#
# print(f"Данные успешно записаны в файл {file_name}.")


# ------------------------- Версия скрипта 1.3.0

import serial
import tkinter as tk
from tkinter import ttk
from itertools import cycle
import time

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

def read_data():
    global buffer, data_count, start_time
    data_block = com_port.read(128)
    buffer += data_block
    end_index = buffer.find(b'\r\n')
    while end_index != -1:
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
                data_count += 1
                if data_count % 10 == 0:
                    ax_var.set(f"{Ax:.2f}")
                    ay_var.set(f"{Ay:.2f}")
                    az_var.set(f"{Az:.2f}")
                    gx_var.set(f"{Gx:.2f}")
                    gy_var.set(f"{Gy:.2f}")
                    gz_var.set(f"{Gz:.2f}")
                    temp_var.set(f"{Temperature:.2f}")

                calculated_line = f"{Ax:.2f} {Ay:.2f} {Az:.2f} {Gx:.2f} {Gy:.2f} {Gz:.2f} {Temperature:.2f}\r\n"
                file.write(calculated_line.encode())
                status_canvas.itemconfig(status_indicator, fill="green")
                print("GOOD!")
            else:
                status_canvas.itemconfig(status_indicator, fill="red")
                print("FAIL!")
        else:
            status_canvas.itemconfig(status_indicator, fill="red")
            print("FAIL!")

        buffer = buffer[end_index + 2:]
        end_index = buffer.find(b'\r\n')

    root.after(1, read_data)

def animate_indicator():
    next_color = next(animation_colors)
    status_canvas.itemconfig(status_indicator, outline=next_color, width=2)
    root.after(100, animate_indicator)

def update_runtime():
    elapsed_time = time.time() - start_time
    elapsed_var.set(f"Elapsed Time: {elapsed_time:.2f} s")
    root.after(100, update_runtime)

# Открываем COM порт для чтения данных
com_port = serial.Serial('COM18', 921600)

buffer = b''
data_count = 0
start_time = time.time()

# Открываем файл для записи данных в текстовом режиме
file_name = 'received_data.txt'
file = open(file_name, 'wb')

# Создаем графический интерфейс
root = tk.Tk()
root.title("Data Display")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Exit", command=root.quit)

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

font_size = 20  # Размер шрифта

ttk.Label(mainframe, text="Ax:", font=('Helvetica', font_size)).grid(column=1, row=1, sticky=tk.W)
ttk.Label(mainframe, text="Ay:", font=('Helvetica', font_size)).grid(column=1, row=2, sticky=tk.W)
ttk.Label(mainframe, text="Az:", font=('Helvetica', font_size)).grid(column=1, row=3, sticky=tk.W)
ttk.Label(mainframe, text="Gx:", font=('Helvetica', font_size)).grid(column=1, row=4, sticky=tk.W)
ttk.Label(mainframe, text="Gy:", font=('Helvetica', font_size)).grid(column=1, row=5, sticky=tk.W)
ttk.Label(mainframe, text="Gz:", font=('Helvetica', font_size)).grid(column=1, row=6, sticky=tk.W)
ttk.Label(mainframe, text="Temperature:", font=('Helvetica', font_size)).grid(column=1, row=7, sticky=tk.W)

ax_var = tk.StringVar()
ay_var = tk.StringVar()
az_var = tk.StringVar()
gx_var = tk.StringVar()
gy_var = tk.StringVar()
gz_var = tk.StringVar()
temp_var = tk.StringVar()
elapsed_var = tk.StringVar()

ttk.Label(mainframe, textvariable=ax_var, font=('Helvetica', font_size)).grid(column=2, row=1, sticky=(tk.W, tk.E))
ttk.Label(mainframe, textvariable=ay_var, font=('Helvetica', font_size)).grid(column=2, row=2, sticky=(tk.W, tk.E))
ttk.Label(mainframe, textvariable=az_var, font=('Helvetica', font_size)).grid(column=2, row=3, sticky=(tk.W, tk.E))
ttk.Label(mainframe, textvariable=gx_var, font=('Helvetica', font_size)).grid(column=2, row=4, sticky=(tk.W, tk.E))
ttk.Label(mainframe, textvariable=gy_var, font=('Helvetica', font_size)).grid(column=2, row=5, sticky=(tk.W, tk.E))
ttk.Label(mainframe, textvariable=gz_var, font=('Helvetica', font_size)).grid(column=2, row=6, sticky=(tk.W, tk.E))
ttk.Label(mainframe, textvariable=temp_var, font=('Helvetica', font_size)).grid(column=2, row=7, sticky=(tk.W, tk.E))

# Индикатор состояния
ttk.Label(mainframe, text="Status:", font=('Helvetica', font_size)).grid(column=1, row=8, sticky=tk.W)
status_canvas = tk.Canvas(mainframe, width=20, height=20)
status_canvas.grid(column=2, row=8, sticky=tk.W)
status_indicator = status_canvas.create_oval(5, 5, 20, 20, outline="green", width=2)

animation_colors = cycle(["green", "lightgreen", "darkgreen"])
animate_indicator()

# Добавляем отображение времени работы скрипта
ttk.Label(mainframe, textvariable=elapsed_var, font=('Helvetica', font_size)).grid(column=1, row=9, columnspan=2, sticky=(tk.W, tk.E))
update_runtime()

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.after(1, read_data)
root.mainloop()

com_port.close()
file.close()

print(f"Данные успешно записаны в файл {file_name}.")
