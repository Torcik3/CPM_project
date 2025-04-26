import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(tasks, critical_path):
    G = nx.DiGraph()

    for name, task in tasks.items():
        label = f"{name}\n{task.early_start}-{task.early_finish}"
        G.add_node(name, label=label)

    for name, task in tasks.items():
        for nxt in task.nxt:
            G.add_edge(name, nxt)

    pos = nx.spring_layout(G)

    edge_colors = []
    for u, v in G.edges():
        if tasks[u] in critical_path and tasks[v] in critical_path:
            edge_colors.append('red')
        else:
            edge_colors.append('black')

    labels = nx.get_node_attributes(G, 'label')

    nx.draw(G, pos, with_labels=False, arrows=True, node_color='pink', edge_color=edge_colors, node_size=1500)
    nx.draw_networkx_labels(G, pos, labels, font_size=8)

    plt.title("Wykres CPM")
    plt.show()