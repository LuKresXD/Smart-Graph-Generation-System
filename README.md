# Smart Graph Generation System

Система создания графов с визуализацией на основе текстового описания. Она позволяет генерировать графы разных типов,
таких как Граф_вершины, Граф_компоненты_связанности, Дерево_листы, Дерево_вершины, Полный_граф и Случайный граф.

## Установка

1. Клонируйте репозиторий:

```
git clone https://github.com/your_username/Smart-Graph-Generation-System.git
```

2. Перейдите в директорию проекта:

```
cd Smart-Graph-Generation-System
```

3. Установите все необходимые зависимости:

```
pip install -r requirements.txt
```

## Использование

Запустите главный скрипт `visualization.py`:

```
python visualization.py
```

В открывшемся окне введите текстовое описание графа, и программа сгенерирует и визуализирует граф, соответствующий
вашему описанию.

## Примеры ввода

- Граф_вершины (количество вершин): "граф 5 вершин"
- Граф_компоненты_связанности (количество компонент связанности): "граф 3 компоненты связанности"
- Дерево_листы (количество листьев): "дерево 7 листьев"
- Дерево_вершины (количество вершин): "дерево 10 вершин"
- Полный_граф (количество вершин): "полный граф 6 вершин"
- Случайный граф: "случайный граф"

## Структура файла .sgg

- Тип графа
- Количество вершин
- Параметры графа
- Список ребер
  Каждый элемент разделен символом новой строки.