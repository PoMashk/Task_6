class DependencyManager:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.visiting = set()  # для обнаружения циклов
        self.install_order = []

    def dfs(self, lib):
        if lib in self.visiting:
            raise Exception(f"Обнаружен цикл зависимостей с библиотекой {lib}")

        if lib in self.visited:
            return

        self.visiting.add(lib)

        for dependency in self.graph.get(lib, []):
            self.dfs(dependency)

        self.visiting.remove(lib)
        self.visited.add(lib)
        self.install_order.append(lib)

    def resolve(self, root):
        self.dfs(root)
        return self.install_order

dependencies = {
    "Проект": ["Lib1", "Lib2", "Lib3"],
    "Lib1": ["Lib4"],
    "Lib4": ["Lib5", "Lib6"],
    "Lib2": ["Lib6", "Lib7"],
    "Lib3": [],
    "Lib5": [],
    "Lib6": [],
    "Lib7": []
}

manager = DependencyManager(dependencies)

try:
    order = manager.resolve("Проект")
    print("Порядок установки библиотек:")
    for lib in order:
        print(lib)
except Exception as e:
    print(e)
