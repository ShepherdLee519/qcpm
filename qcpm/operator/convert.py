_op_type_map = {
    'id': 'I',
    'cx': 'c',
    'tdg': 'T',
    'sdg': 'S',
}

def convert_type(op_type):
    if op_type not in _op_type_map:
        return op_type
    else:
        return _op_type_map[op_type]