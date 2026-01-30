from AssignmentProblem import AssignmentProblem


if __name__ == "__main__":
    N = 4

    problem = AssignmentProblem(N)
    problem.print_cost_matrix()

    flow, min_cost = problem.solve()

    print("\nРезультат:")
    print("Максимальный поток:", flow)
    print("Минимальная стоимость:", min_cost)
