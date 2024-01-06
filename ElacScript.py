import pyaudio
import numpy as np

# Определение параметров аудио
sample_rate = 44100  # Частота дискретизации
duration = 1.0  # Продолжительность пустого звукового сигнала (в секундах)

# Создание пустого звукового сигнала
samples = np.zeros(int(sample_rate * duration), dtype=np.float32)

# Инициализация PyAudio
p = pyaudio.PyAudio()

# Получение ID устройства вывода (USB DAC)
device_index = None
for i in range(p.get_device_count()):
    #print(i, p.get_device_info_by_index(i)['name'])
    device_info = p.get_device_info_by_index(i)
    if 'Elac DCB41' in device_info['name']:  # Замените 'USB DAC' на имя вашего устройства
        device_index = device_info['index']
        break

if device_index is None:
    print("Устройство вывода USB DAC не найдено.")
    exit()

# Открытие аудиоустройства для вывода
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=sample_rate,
                output=True,
                output_device_index=device_index)

# Воспроизведение пустого звукового сигнала в бесконечном цикле
while True:
    stream.write(samples)