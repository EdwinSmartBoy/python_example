def triangles(n):
    array = [1]
    while True:
        yield array
        array = [array[x] + array[x + 1] for x in range(len(array) - 1)]
        array.insert(0, 1)
        array.append(1)
        if len(array) > n:
            break


if __name__ == '__main__':
    for value in triangles(10):
        print(value)
