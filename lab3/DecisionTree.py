import numpy as np
import matplotlib.pyplot as plt
from anytree import Node, LevelOrderIter

class DecisionTree:
    def __init__(self, probabilities=None):
        # Узлы дерева решений
        if probabilities is None:
            probabilities = [0.5, 0.5]
        self.root = Node("Дерево решений")
        self.large_expansion = Node("Крупное расширение", parent=self.root)
        self.small_expansion = Node("Малое расширение", parent=self.root)
        self.no_expansion = Node("Никакого расширения", parent=self.root)

        # Исходы
        Node("Рост населения: +250 тыс.", parent=self.large_expansion)
        Node("Нет роста: -120 тыс.", parent=self.large_expansion)

        Node("Рост населения: +90 тыс.", parent=self.small_expansion)
        Node("Нет роста: -45 тыс.", parent=self.small_expansion)

        Node("Рост населения: 0 тыс.", parent=self.no_expansion)
        Node("Нет роста: 0 тыс.", parent=self.no_expansion)

        self.results = {
            "Крупное расширение": [250, -120],
            "Малое расширение": [90, -45],
            "Никакого расширения": [0, 0],
        }
        self.probabilities = probabilities  # Вероятности событий (50% на рост и нет роста)

    def calculate_expected_values(self):
        expected_values = {}
        for decision, outcomes in self.results.items():
            expected_value = np.dot(outcomes, self.probabilities)
            expected_values[decision] = expected_value
        return expected_values

    def plot_decision_tree(self):
        # Собираем узлы дерева и их координаты
        levels = {node.depth: [] for node in LevelOrderIter(self.root)}
        for node in LevelOrderIter(self.root):
            levels[node.depth].append(node.name)

        # Создание координат для отрисовки дерева
        fig, ax = plt.subplots(figsize=(10, 6))
        x_positions = {}
        y_level = len(levels) - 1
        for depth, nodes in levels.items():
            x_positions[depth] = np.linspace(0, 1, len(nodes))
            for i, node in enumerate(nodes):
                ax.text(x_positions[depth][i], y_level, node, fontsize=10, ha='center', bbox=dict(facecolor='lightblue', edgecolor='black', boxstyle='round,pad=0.5'))
            y_level -= 1

        # Соединение узлов линиями
        for node in LevelOrderIter(self.root):
            if node.is_root:
                continue
            parent_depth = node.parent.depth
            parent_index = levels[parent_depth].index(node.parent.name)
            child_depth = node.depth
            child_index = levels[child_depth].index(node.name)
            ax.plot(
                [x_positions[parent_depth][parent_index], x_positions[child_depth][child_index]],
                [len(levels) - parent_depth - 1, len(levels) - child_depth - 1],
                'k-', lw=1
            )

        ax.axis('off')
        plt.title("Дерево решений")
        plt.show()

    def plot_expected_values(self, expected_values):
        decisions = list(expected_values.keys())
        values = list(expected_values.values())

        plt.bar(decisions, values, color=['blue', 'green', 'orange'])
        plt.title("Ожидаемая прибыль для каждого решения")
        plt.xlabel("Решение")
        plt.ylabel("Ожидаемая прибыль (тыс. руб.)")
        plt.show()


# Создание и расчет дерева решений (По умолчанию 50/50 рост населения)
tree = DecisionTree()
expected_values = tree.calculate_expected_values()
print("Ожидаемые прибыли для решений:")
for decision, value in expected_values.items():
    print(f"{decision}: {value} тыс. руб.")

# Визуализация
tree.plot_decision_tree()
tree.plot_expected_values(expected_values)
