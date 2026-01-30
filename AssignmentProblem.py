import random
from FlowNetwork import FlowNetwork
class AssignmentProblem:
    def __init__(self, n):
        self.n = n
        self.cost_matrix = self._generate_costs()

    def _generate_costs(self):
        return [[random.randint(1, 20) for _ in range(self.n)]
                for _ in range(self.n)]

    def solve(self):
        # Вершины:
        # 0 — источник
        # 1..n — заказы
        # n+1..2n — станки
        # 2n+1 — сток
        source = 0
        sink = 2 * self.n + 1

        network = FlowNetwork(sink + 1)

        # Исток → заказы
        for i in range(self.n):
            network.add_edge(source, 1 + i, 1, 0)

        # Заказы → станки
        for i in range(self.n):
            for j in range(self.n):
                network.add_edge(
                    1 + i,
                    1 + self.n + j,
                    1,
                    self.cost_matrix[i][j]
                )

        # Станки → сток
        for j in range(self.n):
            network.add_edge(1 + self.n + j, sink, 1, 0)

        flow, min_cost = network.min_cost_max_flow(source, sink)
        return flow, min_cost

    def print_cost_matrix(self):
        print("Матрица стоимостей:")
        for row in self.cost_matrix:
            print(row)