import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from collections import namedtuple

class DecisionTreeSolver:
    def __init__(self):
        # Определение вариантов решений и их вероятностей
        self.Decision = namedtuple("Decision", ["name", "outcomes", "probabilities"])
        self.decisions = [
            self.Decision("Без расширения", [0, 0], [1.0, 0.0]),
            self.Decision("Малое расширение", [90, -45], [0.7, 0.3]),
            self.Decision("Крупное расширение", [250, -120], [0.7, 0.3])
        ]

    def calculate_expected_values(self):
        """Вычисление ожидаемой денежной оценки (ОДО) для всех решений."""
        expected_values = {}
        for decision in self.decisions:
            expected_value = sum(
                prob * outcome
                for prob, outcome in zip(decision.probabilities, decision.outcomes)
            )
            expected_values[decision.name] = expected_value
        return expected_values

    def plot_decision_tree(self):
        """Графическое представление дерева решений."""
        fig, ax = plt.subplots(figsize=(12, 8))
        y_base = 0
        x_base = 0

        for i, decision in enumerate(self.decisions):
            x = x_base
            y = y_base - i * 2

            # Рисуем узел решения
            ax.text(x, y, decision.name, fontsize=12,
                    bbox=dict(facecolor='lightblue', edgecolor='black', boxstyle='round,pad=0.3'))

            for j, (outcome, prob) in enumerate(zip(decision.outcomes, decision.probabilities)):
                x_new = x + 2
                y_new = y - j * 1

                ax.add_patch(FancyArrowPatch((x + 0.5, y), (x_new - 0.2, y_new), arrowstyle="->"))
                ax.text(x_new, y_new, f"p={prob*100:.0f}%: {outcome} тыс. руб.",
                        fontsize=10, va="center", ha="left")

        ax.axis('off')
        plt.title("Дерево решений", fontsize=14)
        plt.show()

    def plot_expected_values(self, expected_values):
        """График ОДО для каждого варианта решения."""
        decisions = list(expected_values.keys())
        values = list(expected_values.values())

        plt.figure(figsize=(8, 5))
        plt.bar(decisions, values, color=['blue', 'green', 'orange'])
        plt.title("Ожидаемая прибыль для каждого решения", fontsize=14)
        plt.xlabel("Решение")
        plt.ylabel("Ожидаемая прибыль (тыс. руб.)")
        plt.show()

    def solve(self):
        """Основной метод для решения задачи."""
        expected_values = self.calculate_expected_values()
        print("Ожидаемая денежная оценка (ОДО):")
        for name, value in expected_values.items():
            print(f"{name}: {value:.2f} тыс. руб.")

        # Визуализация
        self.plot_decision_tree()
        self.plot_expected_values(expected_values)

# Использование класса
solver = DecisionTreeSolver()
solver.solve()
