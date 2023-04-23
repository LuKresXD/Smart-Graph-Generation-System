import re


class GraphParser:
    def __init__(self, input_string):
        self.input_string = input_string

    def parse(self):
        graph_type = self.get_graph_type(self.input_string)
        parameters = self.extract_parameters(self.input_string)
        return graph_type, parameters

    def get_graph_type(self, graph_string):
        graph_types = {
            "Полный_граф": (r"полн\w*?",),
            "Граф_вершины": (r"вершин\w*?", r"граф\w*?"),
            "Граф_компоненты_связанности": (r"компонент\w*?", r"связанност\w*?"),
            "Дерево_листы": (r"лист\w*?",),
            "Дерево_вершины": (r"дерев\w*?", r"вершин\w*?"),
            "Случайный": (r"случайн\w*?|рандомн\w*?|произвольн\w*?",)}

        for key, values in graph_types.items():
            if all(re.search(keyword, graph_string, re.IGNORECASE) for keyword in values):
                return key
        raise ValueError("Неизвестный тип графа")

    def extract_parameters(self, graph_string):
        pattern = r'\d+'
        matches = re.findall(pattern, graph_string)
        if matches:
            return {"num": int(matches[0])}
        return {}
