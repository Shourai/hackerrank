def staircase(n):
    for i in range(1, n + 1):
        print(f'{i * "#":>{n}}')


staircase(5)
