class Edge:
    def __init__(self, to, capacity, cost):
        self.to = to                  # куда ведёт ребро
        self.capacity = capacity      # пропускная способность
        self.cost = cost              # стоимость
        self.rev = None               # обратное ребро