import json
import csv

# Открываем и читаем входной JSON файл
with open('in.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Фильтруем привычки с проявлением не больше 2
filtered_data = [habit for habit in data if habit["проявление"] <= 2]

# Сортируем по вредоносности, а затем по алфавиту в случае одинаковой вредности
filtered_data.sort(key=lambda x: (x["вредность"], x["привычка"]))

# Записываем данные в выходной CSV файл
with open('out.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    
    # Пишем заголовки
    writer.writerow(["номер", "привычка", "вредоносность", "проявление", "длительность"])
    
    # Пишем данные
    for i, habit in enumerate(filtered_data, start=1):
        writer.writerow([i, habit["привычка"], habit["вредность"], habit["проявление"], habit["длительность"]])
