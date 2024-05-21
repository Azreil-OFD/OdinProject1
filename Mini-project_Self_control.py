from datetime import datetime, timedelta
from playsound import playsound
import time

# Функция для получения временного интервала от пользователя
def get_time_interval():
    while True:
        time_str = input("Введите временной интервал в формате ЧЧ:ММ:СС: ")
        try:
            h, m, s = map(int, time_str.split(':'))
            return timedelta(hours=h, minutes=m, seconds=s)
        except ValueError:
            print("Неверный формат времени. Попробуйте еще раз.")

# Основная функция таймера
def timer(sound_file):
    time_interval = get_time_interval()
    end_time = datetime.now() + time_interval
    print(f"Таймер запущен на {time_interval}. Ожидайте...")

    # Ожидание до конца времени
    while datetime.now() < end_time:
        time.sleep(1)
    
    # Воспроизведение звука по истечении времени
    print("Время вышло! Воспроизвожу звук...")
    playsound(sound_file)

# Путь к звуковому файлу
sound_file = 'sound.mp3'

# Запуск таймера
timer(sound_file)
