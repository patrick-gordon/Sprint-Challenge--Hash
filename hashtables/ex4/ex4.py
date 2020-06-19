def has_negatives(a):
    result = []
    num_map = dict()
    for num in a:
        if -num in num_map:
            num_map[num] = True
        else:
            num_map[num] = False
    result = [abs(num_tuple[0]) for num_tuple in num_map.items() if num_tuple[1]]
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))