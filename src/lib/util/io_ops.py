def load_array_from_file(path: str, strip = False) -> [str]:
    with open(path, "r") as f:
        if not strip:
            return f.readlines()
        else:
            return [l.strip() for l in f.readlines()]


def dump_array_to_file(path : str, arr : [object]):
    with open(path, "w") as f:
        for e in arr:
            print(e, file = f)

