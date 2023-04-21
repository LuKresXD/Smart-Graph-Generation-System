from graph_classes import GraphVertices  # Import other graph classes as well
from graph_parser import GraphParser
from graph_visualizer import GraphVisualizer

def main():
    input_string = input("Enter the graph description: ")
    parser = GraphParser(input_string)
    graph_type, parameters = parser.parse()

    if graph_type == "Граф_вершины":
        graph = GraphVertices(**parameters)
    # Add cases for other graph types

    graph.generate()
    visualizer = GraphVisualizer(graph.visualize())
    visualizer.visualize()

if __name__ == "__main__":
    main()
