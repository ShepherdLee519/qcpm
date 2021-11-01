_op_type_map = {
    'id': 'I',
    'cx': 'c',
    'tdg': 'T',
    'sdg': 'S',
    'rz': 'R',
}

def _reverseMap(map):
    return {v:k for (k,v) in map.items()}

# {'I': 'id' ...}
_op_type_map_reverse = _reverseMap(_op_type_map)


def convert_type(op_type, reverse=False):
    """
    reverse=False: cx => c, id => I...
    reverse=True: c => cx, I => id...
    """
    if not reverse:
        if op_type not in _op_type_map:
            return op_type
        else:
            return _op_type_map[op_type]
    else:
        if op_type not in _op_type_map_reverse:
            return op_type
        else:
            return _op_type_map_reverse[op_type]

_multi_qubits_gate = {
    'cx': 2
}

def count_qubits(op):
    if op not in _op_type_map:
        op = convert_type(op, True)

    return _multi_qubits_gate.get(op, 1)
    