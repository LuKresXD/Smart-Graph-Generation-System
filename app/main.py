import sys
from parser import parse_text
from graph import RegularGraph, Tree, CompleteGraph, RandomGraph
from visualizer import visualize_graph


def main():
    text = input("Введите текстовое описание графа: ")
    graph_type, graph_params = parse_text(text)

    if graph_type == "обычный":
        graph = RegularGraph(**graph_params)
    elif graph_type == "дерево":
        graph = Tree(**graph_params)
    elif graph_type == "полный":
        graph = CompleteGraph(**graph_params)
    elif graph_type == "случайный":
        graph = RandomGraph(**graph_params)
    else:
        print("Неизвестный тип графа")
        sys.exit(1)

    graph.generate()
    visualize_graph(graph)


if __name__ == "__main__":
    main()
