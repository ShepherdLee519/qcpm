from qcpm.optimization.reduction import reduction
from qcpm.optimization.commutation import commutation


def optimizer(operators):
    """ Optimizer which call both the reduction and commutation.

    Optimizer steps: reduce -> commutate

    Example: 
        call: optimizer(preprocess(path))
    """

    return commutation(
        reduction(operators)
    )