import matplotlib.pyplot as plt
import numpy as np

# Данные для графика
angle = np.array([0, 27, 52, 78, 103, 129, 154, 179])  # Значения угла (градусы)
I_sr = np.array([0, 503, 1011, 1255, 1252, 206, 51, 0])  # Значения I_sr (мА)

# Создаем фигуру и оси
plt.figure(figsize=(8, 6))  # Размер графика

# Строим график
plt.plot(angle, I_sr, label='$I_{ср}$ (mA)', color='blue', marker='o', linestyle='-', linewidth=2)

# Подписываем оси
plt.xlabel('Угол (градусы)')  # Подпись оси X
plt.ylabel('$I_{ср}$ (mA)')  # Подпись оси Y

# Добавляем заголовок графика
plt.title('Зависимость $I_{ср}$ от угла')  # Заголовок графика

# Включаем сетку
plt.grid(True, linestyle='--', alpha=0.7)  # Включаем сетку с пунктирной линией

# Добавляем легенду
plt.legend(loc='upper right')  # Легенда графика (loc указывает расположение)

# Отображаем график
plt.show()