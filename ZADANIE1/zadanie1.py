def dodaj_element(wejscie):
    # najpierw znajdujemy maksymalną głębokość i zbieramy odwołania do list na tej głębokości
    max_depth = -1
    deepest_lists = []  # list of list references at max depth

    def find_deepest(obj, depth=0):
        nonlocal max_depth, deepest_lists

        # jeśli to lista, aktualizujemy stan
        if isinstance(obj, list):
            if depth > max_depth:
                max_depth = depth
                deepest_lists = [obj]
            elif depth == max_depth:
                deepest_lists.append(obj)

        # rekurencyjnie przeszukujemy wszelkie struktury
        if isinstance(obj, list) or isinstance(obj, tuple):
            for elem in obj:
                find_deepest(elem, depth + 1)
        elif isinstance(obj, dict):
            for value in obj.values():
                find_deepest(value, depth + 1)

    # najpierw wyszukaj najgłębsze listy
    find_deepest(wejscie)

    # dla każdej z nich dodaj kolejny element
    for lst in deepest_lists:
        lst.append(len(lst) + 1)

    return wejscie

if __name__ == '__main__':
    input_list = [
        1, 2, [3, 4, [5, {"klucz": [5, 6], "tekst": [1, 2]}], 5],
        "hello", 3, [4, 5], 5, (6, (1, [7, 8]))
    ]
    output_list = dodaj_element(input_list)
    print(output_list)
