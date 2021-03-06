import numpy as np

def sim_rank(graph, C=0.9, n_iter=100, epison=1e-5):
    num_node = len(graph.nodes)
    S = np.identity(num_node)

    for _ in range(n_iter):
        last_S = S.copy()

        for a in range(1, num_node + 1):
            for b in range(1, num_node + 1):
                len_a = len(graph.targets[a])
                len_b = len(graph.targets[b])
                if a == b or len_a == 0 or len_b == 0:
                    continue

                tmp = 0
                for sa in graph.targets[a]:
                    for sb in graph.targets[b]:
                        tmp += last_S[sa - 1][sb - 1]

                S[a - 1][b - 1] = C / (len_a * len_b) * tmp

        delta = 0
        for i in range(num_node):
            for j in range(num_node):
                delta += abs(S[i][j] - last_S[i][j])
        if delta < epison:
            break


    for i in range(num_node):
        for j in range(num_node):
            value = S[i][j]
            S[i][j] = float(format(value, '.4f'))

    return S


        