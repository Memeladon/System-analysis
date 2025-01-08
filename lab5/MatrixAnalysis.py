import numpy as np
import matplotlib.pyplot as plt

class MatrixAnalysis:
    def __init__(self, npmatrix=None):
        if npmatrix is None:
            npmatrix = np.array([
                [-2, 4, 4, 7],
                [0, -1, 3, 8],
                [10, 6, 10, 9],
                [12, 5, 6, 7],
                [6, 4, -2, 2]
            ])
        self.matrix = npmatrix
        self.R = None

    def wald_criterion(self):
        """Критерий Вальда: выбираем максимум из минимальных значений."""
        min_values = np.min(self.matrix, axis=1)
        strategy = np.argmax(min_values)
        return strategy, min_values[strategy]

    def savage_criterion(self):
        """Критерий Сэвиджа: выбираем минимум из максимальных рисков."""
        self.R = np.max(self.matrix, axis=0) - self.matrix  # Матрица рисков
        max_risks = np.max(self.R, axis=1)
        strategy = np.argmin(max_risks)
        return strategy, max_risks[strategy], self.R

    def hurwicz_criterion(self, rho):
        """Критерий Гурвица: взвешенное среднее между пессимизмом и оптимизмом."""
        max_values = np.max(self.matrix, axis=1)
        min_values = np.min(self.matrix, axis=1)
        hurwicz_values = rho * max_values + (1 - rho) * min_values
        strategy = np.argmax(hurwicz_values)
        return strategy, hurwicz_values[strategy]

    def plot_strategies(self):
        # Построение графика для сравнения стратегий по разным критериям
        strategies = ['1', '2', '3', '4', '5']

        # Значения критериев для каждой стратегии
        wald_values = np.min(self.matrix, axis=1)  # Вальд
        savage_values = np.max(self.R, axis=1)  # Сэвидж

        # График критериев Вальда и Сэвиджа
        plt.figure(figsize=(10, 6))

        plt.bar(strategies, wald_values, alpha=0.6, label="Критерий Вальда (min выигрышей)", color="blue")
        plt.bar(strategies, savage_values, alpha=0.6, label="Критерий Сэвиджа (max рисков)", color="red")

        plt.xlabel("Стратегии")
        plt.ylabel("Значения критериев")
        plt.title("Сравнение стратегий по критериям Вальда и Сэвиджа")
        plt.legend()
        plt.show()

        # Построение матрицы рисков (графическое представление)
        plt.figure(figsize=(8, 6))
        plt.imshow(R, cmap='viridis', interpolation='none', aspect='auto')
        plt.colorbar(label="Риски")
        plt.title("Матрица рисков для критерия Сэвиджа")
        plt.xlabel("Состояния природы")
        plt.ylabel("Стратегии")
        plt.xticks(np.arange(self.R.shape[1]), [f"Состояние {i + 1}" for i in range(self.R.shape[1])])
        plt.yticks(np.arange(self.R.shape[0]), [f"Стратегия {i + 1}" for i in range(self.R.shape[0])])
        plt.show()

matrix_solve = MatrixAnalysis()
# 1. Решение по критерию Вальда
wald_strategy, wald_value = matrix_solve.wald_criterion()

# 2. Решение по критерию Сэвиджа
savage_strategy, savage_value, R = matrix_solve.savage_criterion()

# 3. Решение по критерию Гурвица для разных значений ρ
hurwicz_results = []
for rho in [0, 0.5, 1]:
    strategy, value = matrix_solve.hurwicz_criterion(rho)
    hurwicz_results.append((rho, strategy, value))

# Вывод результатов
results = {
    "Вальд": (wald_strategy, wald_value),
    "Сэвидж": (savage_strategy, savage_value),
    "Гурвиц": hurwicz_results
}

print(results)
matrix_solve.plot_strategies()