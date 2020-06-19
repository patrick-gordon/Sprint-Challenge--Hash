def finder(paths, queries):

    file_map = dict()
    for path in paths:
        file = path.split('/')[-1]
        if file in file_map:
            file_map[file].append(path)
        else:
            file_map[file] = [path]
    result = []
    for query in queries:
        if query in file_map:
            result.extend(file_map[query])
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
