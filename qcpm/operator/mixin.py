class operatorMixin:

    op_type_map = {
        'id': 'I',
        'cx': 'c',
        'tdg': 'T',
        'sdg': 'S',
        'rz': 'R',
    }
    # {'I': 'id' ...}
    op_type_map_reversed = {v:k for (k,v) in op_type_map.items()}

    multi_qubits_gate = {
        'cx': 2
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