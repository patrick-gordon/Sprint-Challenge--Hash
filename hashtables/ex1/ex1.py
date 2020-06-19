def get_indices_of_item_weights(weights, length, limit):

    weight_map = dict()
    for i, weight in enumerate(weights):
        diff_weight = limit - weight
        j = weight_map.get(diff_weight)
        if j is not None:
            return tuple(sorted([i, j], reverse=True))
        weight_map[weight] = i
    return None