from typing import Tuple, List
import matplotlib.pyplot as plt
import numpy as np


class FarmProblem:
    def __init__(self, costs: Tuple[int, int] = (16, 12), daily_feed=None, limit_feed=None):
        if limit_feed is None:
            limit_feed = [180, 240, 426]
        if daily_feed is None:
            daily_feed = [
                (2, 3),  # Корм 1
                (4, 1),  # Корм 2
                (6, 7)  # Корм 3
            ]
        self.costs = costs  # Стоимость шкурок
        self.daily_feed = daily_feed
        self.limit_feed = limit_feed

        self.__max_profit = 0

    def solve_farm_problem(self) -> Tuple[int, int, int]:
        optimal_x1 = 0
        optimal_x2 = 0

        x1_values = []
        x2_values = []
        profits = []

        for x1 in range(0, self.limit_feed[0] // self.daily_feed[0][0] + 1):
            for x2 in range(0, self.limit_feed[0] // self.daily_feed[0][1] + 1):
                if (self.daily_feed[0][0] * x1 + self.daily_feed[0][1] * x2 <= self.limit_feed[0] and
                        self.daily_feed[1][0] * x1 + self.daily_feed[1][1] * x2 <= self.limit_feed[1] and
                        self.daily_feed[2][0] * x1 + self.daily_feed[2][1] * x2 <= self.limit_feed[2]):

                    profit = self.costs[0] * x1 + self.costs[1] * x2

                    x1_values.append(x1)
                    x2_values.append(x2)
                    profits.append(profit)

                    if profit > self.__max_profit:
                        self.__max_profit = profit
                        optimal_x1 = x1
                        optimal_x2 = x2

        self.plot_results(x1_values, x2_values, profits, optimal_x1, optimal_x2)

        if self.__max_profit != 0:
            print(f"Оптимальное количество лисиц (A): {optimal_x1}")
            print(f"Оптимальное количество песцов (B): {optimal_x2}")
            print(f"Максимальная прибыль: {self.__max_profit} руб.")
        else:
            print("Не удалось найти оптимальное решение.")

        return optimal_x1, optimal_x2, self.__max_profit

    def plot_results(self, x1_values: List[int], x2_values: List[int], profits: List[int], optimal_x1: int,
                     optimal_x2: int):
        plt.figure(figsize=(10, 6))
        scatter = plt.scatter(x1_values, x2_values, c=profits, cmap='viridis', s=100, edgecolor='k')
        plt.colorbar(scatter, label='Прибыль')
        plt.scatter(optimal_x1, optimal_x2, color='red', s=200, label='Оптимальное решение', edgecolor='k')

        plt.title('Допустимые решения и оптимальная прибыль')
        plt.xlabel('Количество лисиц (x1)')
        plt.ylabel('Количество песцов (x2)')
        plt.legend()
        plt.grid(True)
        plt.show()


# Запуск задачи
Farm = FarmProblem()
Farm.solve_farm_problem()
