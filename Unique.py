def unique(sequence):
    seen = set()
    # return [x for x in sequence if not (x in seen or seen.add(x))]
    return [x for x in sequence if not (tuple(x) in seen or seen.add(tuple(x)))]