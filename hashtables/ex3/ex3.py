def intersection(arrays):
    num_count = dict()
    for i, array in enumerate(arrays):
        added = False
        for num in array:
            if num in num_count:
                added = True
                num_count[num] += 1
            elif i == 0:
                num_count[num] = 1
        if i > 0 and not added:
            break
    result = [num[0] for num in num_count.items() if num[1] == len(arrays)]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))