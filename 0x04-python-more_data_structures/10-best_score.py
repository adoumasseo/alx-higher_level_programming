#!/usr/bin/python3
def best_score(a_dictionary):
    if not (a_dictionary):
        return None
    max_v, max_k = 0, ""
    for k, v in a_dictionary.items():
        if max_v < v:
            max_v = v
            max_k = k
    return max_k
