import sys


def task_405():
    for line in sys.stdin.read().splitlines():
        if line.strip():
            numbers = list(map(int, line.split()))
            print(*numbers[len(numbers) // 2:])


def task_446():
    for line in sys.stdin.read().splitlines():
        if line.strip():
            numbers = list(map(int, line.split()))
            counts = {}
            for number in numbers:
                counts[number] = counts.get(number, 0) + 1
            pairs = sum(count * (count - 1) // 2 for count in counts.values())
            print(pairs)


def task_454():
    numbers = list(map(int, sys.stdin.read().split()))
    result = [number for number in numbers if number % 2 != 0]
    print(result)


def task_469():
    numbers = sys.stdin.read().split()
    reversed_numbers = numbers[::-1]
    print("".join(reversed_numbers))


def task_484():
    n = int(sys.stdin.read().strip())
    matrix = [[0] * n for _ in range(n)]

    top, bottom = 0, n - 1
    left, right = 0, n - 1
    number = 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            matrix[top][col] = number
            number += 1
        top += 1

        for row in range(top, bottom + 1):
            matrix[row][right] = number
            number += 1
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = number
                number += 1
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = number
                number += 1
            left += 1

    for row in matrix:
        print(*row)


def task_485():
    lines = sys.stdin.read().splitlines()
    shift = int(lines[0]) % 80
    message = lines[1]
    first = 0x1F600
    last = 0x1F64F

    encrypted = []
    for char in message:
        code = ord(char)
        if first <= code <= last:
            encrypted.append(chr(first + (code - first + shift) % 80))
        else:
            encrypted.append(char)

    print("".join(encrypted))


def main():
    print("Варіант 13 — Лабораторна робота 5")
    print("Оберіть завдання: 405, 446, 454, 469, 484 або 485")
    choice = input("Номер завдання: ").strip()

    tasks = {
        "405": task_405,
        "446": task_446,
        "454": task_454,
        "469": task_469,
        "484": task_484,
        "485": task_485,
    }

    if choice in tasks:
        tasks[choice]()
    else:
        print("Неправильний номер завдання.")


if __name__ == "__main__":
    main()
