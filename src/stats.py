from typing import List, Optional


def mean(numbers: List[float]) -> Optional[float]:
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def median(numbers: List[float]) -> Optional[float]:
    if not numbers:
        return None
    numbers.sort()
    mid = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2.0
    return numbers[mid]
