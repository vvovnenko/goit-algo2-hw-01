def find_min_max(arr: list[int]) -> tuple[int, int]:
    if not arr:
        raise ValueError("Масив не може бути порожнім")

    def divide_and_conquer(start: int, end: int) -> tuple[int, int]:
        if start == end:
            return arr[start], arr[start]

        if end - start == 1:
            return min(arr[start], arr[end]), max(arr[start], arr[end])

        mid = (start + end) // 2
        left_min, left_max = divide_and_conquer(start, mid)
        right_min, right_max = divide_and_conquer(mid + 1, end)

        return min(left_min, right_min), max(left_max, right_max)

    # Виклик рекурсивної функції для всього масиву
    return divide_and_conquer(0, len(arr) - 1)

examples = [
    [3, 5, 1, 8, 2, -4, 7],
    [10, 20, 30, 40, 50],
    [-5, -10, -3, -1],
    [100],
    [15, 15, 15, 15],
    [1, -1, 2, -2, 3, -3],
    [0],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [-100, 0, 100],
    [5, 4, 3, 2, 1, -1, -2, -3, -4, -5],
    [],
]

for array in examples:
    try:
        result = find_min_max(array)
        print(f"{array} -> Min: {result[0]}, Max: {result[1]}")
    except ValueError as e:
        print(f"{array} -> Error: {e}")

