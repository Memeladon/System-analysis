import numpy as np
import matplotlib.pyplot as plt

class DynamicProgrammingSolver:
    def __init__(self, budget:int=100, investment_options=None, profit_matrix=None):
        """
        Инициализация задачи.
        :param budget: Общий бюджет (целое число)
        :param investment_options: Возможные вложения (массив)
        :param profit_matrix: Матрица прибылей (двумерный массив)
        """
        if investment_options is None:
            investment_options = [20, 40, 60, 80, 100]
        if profit_matrix is None:
            profit_matrix = np.array([
                [10, 31, 42, 62, 76],
                [12, 26, 36, 54, 78],
                [11, 36, 45, 60, 77],
                [16, 37, 46, 63, 80]
            ])
        self.budget = budget
        self.investment_options = investment_options
        self.profit_matrix = profit_matrix
        self.num_projects = profit_matrix.shape[0]
        self.dp_table = None  # Таблица динамического программирования
        self.solution = []

    def solve(self):
        """
        Решение задачи методом динамического программирования.
        """
        num_steps = len(self.investment_options)
        dp = np.zeros((self.num_projects + 1, self.budget // 20 + 1))
        backtrack = np.zeros_like(dp, dtype=int)

        # Основной цикл динамического программирования
        for i in range(1, self.num_projects + 1):
            for b in range(self.budget // 20 + 1):
                for k in range(num_steps):
                    if self.investment_options[k] // 20 <= b:
                        current_profit = self.profit_matrix[i - 1, k] + dp[i - 1, b - self.investment_options[k] // 20]
                        if current_profit > dp[i, b]:
                            dp[i, b] = current_profit
                            backtrack[i, b] = self.investment_options[k]

        # Восстановление пути
        self.dp_table = dp
        self.solution = []
        remaining_budget = self.budget // 20
        for i in range(self.num_projects, 0, -1):
            invest = backtrack[i, remaining_budget]
            self.solution.append((i, invest))
            remaining_budget -= invest // 20

        self.solution.reverse()
        return dp[self.num_projects, self.budget // 20]

    def plot_solution(self):
        """
        Визуализация решения.
        """
        projects = [f"Проект {s[0]}" for s in self.solution]
        investments = [s[1] for s in self.solution]

        plt.figure(figsize=(8, 6))
        bars = plt.barh(projects, investments, color='skyblue')
        plt.xlabel("Инвестиции (млн ден. ед.)")
        plt.title("Оптимальное распределение инвестиций")
        plt.grid(True, linestyle='--', alpha=0.7)

        for bar in bars:
            plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{bar.get_width()}',
                     va='center', ha='left', fontsize=10)

        plt.show()


# Решение задачи
solver = DynamicProgrammingSolver()
max_profit = solver.solve()
solver.plot_solution()

print(max_profit)
