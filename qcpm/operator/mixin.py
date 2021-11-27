class operatorMixin:

    op_type_map = {
        'id': 'I',
        
        'cx': 'c',
        'cz': 'e',

        'tdg': 'T',
        'sdg': 'S',

        'rx': 'X',
        'ry': 'Y',
        'rz': 'Z',
    }
    # {'I': 'id' ...}
    op_type_map_reversed = {v:k for (k,v) in op_type_map.items()}

    rotation_gates = ['rx', 'ry', 'rz']

    multi_qubits_gate = {
        'cx': 2,
        'cz': 2,
    }

    @classmethod
    def convert_type(cls, op_type, reverse=False):
        """
        Example: 
            reverse=False: cx => c, id => I...
            reverse=True: c => cx, I => id...
        """
        try:
            if not reverse:
                return cls.op_type_map[op_type]
            else:
                return cls.op_type_map_reversed[op_type]
        except KeyError:
            # op_type is not in op_type_map/op_type_map_reversed
            return op_type

    @classmethod
    def count_qubits(cls, op):
        # get original op_type
        if op not in cls.op_type_map:
            op = cls.convert_type(op, True)

        # default qubits size: 1
        return cls.multi_qubits_gate.get(op, 1)

    @classmethod
    def is_rotation(cls, op):
        # get original op_type
        if op not in cls.op_type_map:
            op = cls.convert_type(op, True)

        return op in cls.rotation_gates