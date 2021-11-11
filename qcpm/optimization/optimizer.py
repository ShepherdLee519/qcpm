from qcpm.optimization.reduction import reduction
from qcpm.optimization.commutation import commutation


def optimizer(operators):
    """ Optimizer which call both the reduction and commutation.

    Optimizer steps: reduce -> commutate -> reduce

    Example: 
        call: optimizer(preprocess(path))
    """

    return reduction(
        commutation(
            reduction(operators)
        )
    )