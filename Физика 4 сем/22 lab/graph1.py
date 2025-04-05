import matplotlib.pyplot as plt
import numpy as np

# Данные для графика
alpha = np.array([0, 21, 56, 79, 108, 131, 157, 178])  # Значения угла α (градусы)
I_cp = np.array([609, 561, 504, 405, 207, 106, 54, 0])  # Значения I_cp (мА)

# Создаем фигуру и оси
plt.figure(figsize=(8, 6))  # Размер графика

# Строим график
plt.plot(alpha, I_cp, label='$I_{cp}$', color='blue', marker='o', linestyle='-', linewidth=2)

# Подписываем оси
plt.xlabel('$\\alpha$ (градусы)')  # Подпись оси X
plt.ylabel('$I_{cp}$ (mA)')  # Подпись оси Y

# Добавляем заголовок графика
plt.title('Зависимость $I_{cp}$ от $\\alpha$')  # Заголовок графика

# Включаем сетку
plt.grid(True, linestyle='--', alpha=1)  # Включаем сетку с пунктирной линией

# Добавляем легенду
plt.legend(loc='upper right')  # Легенда графика (loc указывает расположение)

# Отображаем график
plt.show()