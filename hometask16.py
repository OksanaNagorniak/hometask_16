A = {'key': 'good', 'key1': 'hello', 'key2': 'hi'}
B = {'key': 'morning', 'key1': 'world', 'key2': 'Ukraine'}


def combine_dicts(A, B):
    for k, v in B.items():
        if A.get(k):
            A[k] = [A[k], v]
        else:
            A[k] = v
    return A


C = combine_dicts(A, B)

import json
dict_json = C
with open('result.json', 'w') as f:
    f.write(json.dumps(dict_json))
