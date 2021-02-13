def line(x1, y1, x2, y2, x):
    a = (y2 - y1) / (x2 - x1)
    b = y1 - a * x1
    res = a * x + b
    return res

if __name__ == "__main__":
    print(line(x1, y1, x2, y2, x))