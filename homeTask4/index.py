from typing import List
from math import sqrt


def pearson_correlation(array_1: List[float], array_2: List[float]) -> float:

    # Проверка длины
    if len(array_1) != len(array_2):
        raise ValueError("Массивы разной длины")

    n = len(array_1)

    # Расчет среднего значения
    avg_2 = sum(array_2) / n

    # Вычисление ковариации и дисперсии
    covariance = sum((array_1[i] - avg_1) *
                     (array_2[i] - avg_2) for i in range(n))
    variance_array_1 = sum((x - avg_1) ** 2 for x in array_1)
    variance_array_2 = sum((y - avg_2) ** 2 for y in array_2)

    # Расчет корреляции Пирсона
    correlation = covariance / \
        (sqrt(variance_array_1) * sqrt(variance_array_2))

    return round(correlation)


arr_1 = [9, 7, 5, 3, 1]
arr_2 = [1, 3, 5, 7, 9]

correlation = pearson_correlation(arr_1, arr_2)

# Печать результата
print(f"Корреляция Пирсона: {correlation}")
