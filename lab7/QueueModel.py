import math

# Данные задачи
arrival_rate = 10  # Скорость поступления запросов (z), заявок в час
service_rate = 12  # Скорость обслуживания (b), заявок в час

# 1. Вероятность того, что в системе нет запросов (P0)
P0 = 1 - (arrival_rate / service_rate)

# 2. Среднее число запросов в очереди (Lq)
Lq = (arrival_rate ** 2) / (service_rate * (service_rate - arrival_rate))

# 3. Среднее время ожидания (Wq)
Wq = Lq / arrival_rate

# 4. Среднее время, которое запрос проводит в системе (Ws)
Ws = 1 / (service_rate - arrival_rate)

# 5. Вероятность того, что запросу придётся ждать обслуживания (Pw)
Pw = arrival_rate / service_rate

# Результаты
results = {
    "P0 (вероятность, что в системе нет запросов)": P0,
    "Lq (среднее число запросов в очереди)": Lq,
    "Wq (среднее время ожидания, часы)": Wq,
    "Ws (среднее время в системе, часы)": Ws,
    "Pw (вероятность ожидания обслуживания)": Pw
}

# Вывод результатов
for key, value in results.items():
    print(f"{key}: {value:.4f}")
