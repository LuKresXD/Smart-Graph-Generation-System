import re


def parse_text(text):
    graph_type = None
    graph_params = {}

    if "обычный" in text:
        graph_type = "обычный"
        vertices = re.search(r"количество вершин: (\d+)", text)
        if vertices:
            graph_params["vertices"] = int(vertices.group(1))

        # Добавьте остальные параметры и их парсинг здесь

    # Добавьте проверки и парсинг для других типов графов здесь

    return graph_type, graph_params
