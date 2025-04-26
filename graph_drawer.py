import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(tasks, critical_path):
    G = nx.DiGraph()


    layers = {}
    for name, task in tasks.items():
        if name == 'START':
            layers[name] = 0
        elif not task.prev:
            layers[name] = 1
        else:
            layers[name] = max(layers[p] for p in task.prev) + 1

    for name, task in tasks.items():
        label = f"{name}\n{task.early_start}-{task.early_finish}\nReserve: {task.reserve}"
        G.add_node(name, label=label, layer=layers[name])

    for name, task in tasks.items():
        for nxt in task.nxt:
            G.add_edge(name, nxt)


    layer_nodes = {}
    for node, data in G.nodes(data=True):
        layer = data['layer']
        if layer not in layer_nodes:
            layer_nodes[layer] = []
        layer_nodes[layer].append(node)

    pos = {}
    for layer, nodes in layer_nodes.items():
        for i, node in enumerate(nodes):
            pos[node] = (layer, -i * 2)


    edge_colors = []
    for u, v in G.edges():
        if tasks[u] in critical_path and tasks[v] in critical_path:
            edge_colors.append('red')
        else:
            edge_colors.append('black')

    labels = nx.get_node_attributes(G, 'label')


    nx.draw(G, pos, with_labels=False, arrows=True, node_color='pink', edge_color=edge_colors, node_size=2000)
    nx.draw_networkx_labels(G, pos, labels, font_size=8)

    plt.title("CPM Diagram - START osobna kolumna")
    plt.show()
