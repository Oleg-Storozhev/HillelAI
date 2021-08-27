def remove_duplicate_ids(obj):
    out, seen = {}, {}
    for i in sorted(obj.keys(), key=int, reverse=True):
        uniques = []
        for v in obj[i]:
            if v not in seen:
                uniques.append(v)
                seen[v] = 1
        out[i] = uniques
    return out


answer = {
    "1": ["A", "B", "C"],
    "2": ["A", "B", "D", "A"],
}
results = {
    "1": ["C"],
    "2": ["A", "B", "D"]
}
assert remove_duplicate_ids(answer) == results
