from qcpm.candidate.plan import Plan, Plans


def filterCandidates(candidates):
    """ filter candidates(without conflict occurance) and generate Plans.

    Args: 
        candidates: list of Candidate object.
    -------
    Returns:
        Plans object contains <ALL> possible mapping plans.
    """
    count = 0 # plan's total number
    size = len(candidates)
    plans = []

    for i in range(size):
        target = candidates[i]
        temp = [target]
        s = set(target.pos) # eg. like {1, 4}
        delta_cost = target.pattern.delta

        for j in range(i + 1, size):
            # if no conflict => add this candidate
            if not (candidates[j] & s):
                temp.append(candidates[j])
                delta_cost += candidates[j].pattern.delta
                # eg. [1, 4] no conflict with [3, 7]
                #   => {1, 4} | {3, 7} => {1, 3, 4, 7}
                # 
                s = s | set(candidates[j].pos)
        
        count += 1

        # generate new Plan.
        plans.append(
            Plan(temp, delta_cost)
        )

    # generate Plans object and return.
    return Plans(plans)