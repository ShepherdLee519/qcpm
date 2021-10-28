from qcpm import operator
from qcpm.optimization.reduction import reduction
from qcpm.optimization.commutation import commutation


def optimizer(operators):
    """
        reduce -> commutate -> reduce
    """

    return reduction(
        commutation(
            reduction(operators)
        )
    )