x, y = map(int, input().split())
a = 0
b = 0
c = 0

for i in range(x):
    for j in range(i, -1, -1):
        print(f"({j + 1} * {y})", end="")
        if j > 0:
            print(" + ", end="")
    a = (i + 1) * y
    b = b + a
    print(f" = {b}")

    c = c + b

print(c)
