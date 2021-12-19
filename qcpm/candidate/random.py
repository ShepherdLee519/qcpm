import random

from qcpm.candidate.plan import Plan, Plans


def RandomlySearchPlan(circuit, candidates, metric):
    """ filter candidates(without conflict occurance) and generate Plans.

    args are corresponding to the args in SearchPlan(circuit, candidates, metric):

    Args: 
        circuit: Circuit object, just may be used in calculate delta_depth.
        candidates: list of Candidate object.
        metric: cycle or depth which used to calculate value of candidate.
    -------
    Returns:
        Plans object contains <ALL> possible mapping plans.
    """
    size = len(candidates)
    delta_cost = 0
    selected = []

    for i in range(size):
        target = candidates[i]
        next_target = None if i == size - 1 else candidates[i + 1]
        if not (target & selected):
            if not (target & next_target):
                selected.append(target)
                delta_cost += target.delta(metric, circuit)
            else:
                # randomly decide to choose current candidate or not.
                rand = random.random()
                if rand >= 0.5:
                    selected.append(target)
                    delta_cost += target.delta(metric, circuit)

    return Plans([ Plan(selected, delta_cost) ])