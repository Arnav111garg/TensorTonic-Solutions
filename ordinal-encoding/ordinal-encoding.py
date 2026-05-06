def ordinal_encoding(values, ordering):
    mapping = {val: i for i, val in enumerate(ordering)}

    return [mapping[v] for v in values]