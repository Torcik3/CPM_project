import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def draw_graph(tasks, critical_path, project_duration):
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


    window = tk.Tk()
    window.title("CPM Diagram")


    frame_plot = ttk.Frame(window)
    frame_plot.pack(side="top", fill="both", expand=True)


    frame_text = ttk.Frame(window)
    frame_text.pack(side="bottom", fill="x")


    fig = plt.Figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    nx.draw(G, pos, with_labels=False, arrows=True, node_color='pink', edge_color=edge_colors, node_size=2000, ax=ax)
    nx.draw_networkx_labels(G, pos, labels, font_size=8, ax=ax)
    ax.set_title("Diagram CPM")
    ax.axis('off')


    canvas = FigureCanvasTkAgg(fig, master=frame_plot)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill="both", expand=True)


    critical_path_str = " -> ".join([task.name for task in critical_path])
    info_text = f"Ścieżka krytyczna:\n{critical_path_str}\n\nMinimalny czas realizacji projektu: {project_duration} dni"
    label = ttk.Label(frame_text, text=info_text, justify="center", font=("Arial", 10))
    label.pack(pady=10)

    window.mainloop()
